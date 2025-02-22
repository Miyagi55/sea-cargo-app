import streamlit as st
from utils.auth import check_auth, logout
from utils.theme import set_theme

def main():
    if not check_auth():
        st.warning("Por favor, inicie sesión para acceder a esta página")
        st.stop()
    
    
    st.write("This is the Clients page")
    set_theme()
    logout()

if __name__ == "__main__":
    st.set_page_config(page_title="Clientes - Sea Cargo App", layout="wide")
    main()