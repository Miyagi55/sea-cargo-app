import streamlit as st
import bcrypt
from dotenv import load_dotenv
import os
import logging
from utils.database import get_db_connection
import secrets
import time

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# Constants
MAX_INPUT_LENGTH = 50
ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
LOGIN_ATTEMPTS_LIMIT = 5
LOCKOUT_DURATION = 900  # 15 minutes

def hash_password(password):
    # Higher work factor for 2025
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=14))

def verify_password(password, hashed):
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))  # Hashed should be bytes from DB
    except ValueError:
        return False

def validate_input(text):
    """Ensure input is safe and reasonable."""
    return (len(text) <= MAX_INPUT_LENGTH and 
            all(char in ALLOWED_CHARS for char in text))

def check_auth():
    """Verify session with server-side check."""
    if 'session_token' not in st.session_state or not st.session_state.session_token:
        return False
    # Ideally, validate token against a server-side store (simplified here)
    return True

def fetch_user_data(username):
    """Fetch user data with retry logic."""
    for attempt in range(3):
        conn = None
        cur = None
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT passw_hash, role FROM usuarios WHERE username = %s", (username,))
            result = cur.fetchone()
            return result
        except Exception as e:
            logger.error(f"DB error (attempt {attempt + 1}): {e}")
            time.sleep(1)  # Backoff
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    return None

def check_rate_limit(username):
    """Simple rate-limiting using session state (replace with DB for prod)."""
    key = f"login_attempts_{username}"
    if key not in st.session_state:
        st.session_state[key] = {'count': 0, 'lockout_time': 0}
    
    attempts = st.session_state[key]
    if time.time() < attempts['lockout_time']:
        st.error(f"Muchos intentos. Intenta de nuevo en {int((attempts['lockout_time'] - time.time()) / 60)} minutes.")
        return False
    return True

def update_rate_limit(username, success):
    key = f"login_attempts_{username}"
    attempts = st.session_state.get(key, {'count': 0, 'lockout_time': 0})
    
    if success:
        attempts['count'] = 0
    else:
        attempts['count'] += 1
        if attempts['count'] >= LOGIN_ATTEMPTS_LIMIT:
            attempts['lockout_time'] = time.time() + LOCKOUT_DURATION
    st.session_state[key] = attempts

def authenticate_user(result, password):
    if not result:
        return False
    if verify_password(password, result[0]):
        return True
    return False

def set_session(username, role):
    # Generate a secure token (simplified; use JWT in prod)
    token = secrets.token_hex(16)
    st.session_state.session_token = token
    st.session_state.username = username
    st.session_state.role = role
    st.success("Has iniciado sesión exitosamente!")
    st.rerun()

def login():
    st.title("Iniciar sesión")
    
    username = st.text_input("Username", max_chars=MAX_INPUT_LENGTH)
    password = st.text_input("Password", type="password", max_chars=MAX_INPUT_LENGTH)
    
    if st.button("Login"):
        if not (username and password):
            st.error("Por favor, ingresa un nombre de usuario y contraseña.")
            return
        
        if not (validate_input(username) and validate_input(password)):
            st.error("Caracteres inválidos en el usuario o contraseña.")
            return
        
        if not check_rate_limit(username):
            return
        
        result = fetch_user_data(username)
        authenticated = authenticate_user(result, password)
        update_rate_limit(username, authenticated)
        
        if authenticated:
            set_session(username, result[1])
        else:
            st.error("Credenciales inválidas")

def logout():
    if st.button("Logout"):
        st.session_state.clear()  # Nuke everything
        st.rerun()