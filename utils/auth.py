import streamlit as st
import bcrypt
from dotenv import load_dotenv
import os
from utils.database import get_db_connection

load_dotenv()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def check_auth():
    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        return False
    return True

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT password, role FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        
        if result and verify_password(password, result[0]):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.role = result[1]
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid credentials")
        cur.close()
        conn.close()

def logout():
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.pop('username', None)
        st.session_state.pop('role', None)
        st.rerun()