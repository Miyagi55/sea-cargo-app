import streamlit as st
from utils.auth import check_auth, logout
from utils.theme import set_theme

def main():
    if not check_auth():
        st.warning("Please login to access this page")
        st.stop()
    
    st.title("Ajustes")
    st.write("Settings Page")
    set_theme()
    logout()

if __name__ == "__main__":
    main()