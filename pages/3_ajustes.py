import streamlit as st
from utils.auth2 import check_auth, logout


def main():
    if not check_auth():
        st.warning("Por favor, inicie sesión para acceder a esta página")
        st.stop()
    
    st.title("Ajustes")
    st.write("Settings Page")

    logout()

if __name__ == "__main__":
    main()