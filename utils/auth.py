import streamlit as st
import bcrypt
from dotenv import load_dotenv
import os
import logging
from utils.database import get_db_connection

logging.basicConfig(level=logging.ERROR)

load_dotenv()


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def check_auth():

    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        return False
    return True

def fetch_user_data(username):
    """Fetch user data from the database."""
    

    try:
        cur = None
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT password, role FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        return result

    except Exception as e:
        logging.error(f"Database error occurred: {e}")
        return None

    finally:
        if cur is not None:  # Only close if cur was successfully created
            cur.close()
            conn.close()


def authenticate_user(result, password):
    """Authenticate user based on fetched data and provided password."""

    if result is None:
        st.error("An error occurred. Please try again.")
        return False

    if verify_password(password, result[0]):
        return True

    st.error("Invalid credentials")
    return False


def set_session(username, role):
    """Set session state upon successful authentication."""

    st.session_state.authenticated = True
    st.session_state.username = username
    st.session_state.role = role

    st.success("Logged in successfully!")
    st.rerun()


def login():

    st.title("Iniciar sesión")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        result = fetch_user_data(username)
        if authenticate_user(result, password):
            set_session(username, result[1])


def logout():

    if st.button("Logout"):
        st.session_state.authenticated = False

        st.session_state.pop('username', None)
        st.session_state.pop('role', None)

        st.rerun()