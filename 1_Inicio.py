import streamlit as st
from utils.auth import check_auth, logout, login 
from utils.theme import set_theme

def main():
    if not check_auth():
        login()
        st.stop()
    else:
        st.title("Inicio")
        st.write("Welcome to the Home page!")
        st.sidebar.title(f"User: {st.session_state.username}")
        st.sidebar.write(f"Role: {st.session_state.role}")
        set_theme()
        logout()

if __name__ == "__main__":
    st.set_page_config(page_title="Sea Cargo App", layout="wide")
    main()