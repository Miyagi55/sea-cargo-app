import streamlit as st
from utils.auth2 import check_auth, logout, login 


def main():
    if not check_auth():
        login()
        st.stop()
    else:
        st.title("Inicio")
        st.write("Bienvenido a la aplicación de Sea Cargo!")
        st.sidebar.title(f"User: {st.session_state.username}")
        st.sidebar.write(f"Role: {st.session_state.role}")
        logout()

if __name__ == "__main__":
    st.set_page_config(page_title="Sea Cargo App", layout="wide")
    main()