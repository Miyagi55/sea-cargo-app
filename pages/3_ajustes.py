import streamlit as st
from utils.auth import check_auth, logout
from utils.theme import set_theme

def main():
    if not check_auth():
        st.warning("Por favor, inicie sesión para acceder a esta página")
        st.stop()
    
    st.title("Ajustes")
    st.write("Settings Page")
    set_theme()
    logout()

if __name__ == "__main__":
    main()