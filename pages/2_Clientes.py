import streamlit as st
from utils.auth2 import check_auth, logout


def main():
    if not check_auth():
        st.warning("Por favor, inicie sesión para acceder a esta página")
        st.stop()
    
    
    st.write("Página para manejar clientes")
    logout()

if __name__ == "__main__":
    st.set_page_config(page_title="Clientes - Sea Cargo App", layout="wide")
    main()