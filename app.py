import streamlit as st
from utils.auth import login, check_auth

def main():
    if not check_auth():
        login()
    else:
        st.sidebar.title(f"Welcome, {st.session_state.username}")
        st.sidebar.write(f"Role: {st.session_state.role}")
        st.write("Please select a page from the sidebar.")

if __name__ == "__main__":
    st.set_page_config(page_title="Sea Cargo App", layout="wide")
    main()