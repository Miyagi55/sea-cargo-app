import streamlit as st

def set_theme():
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'
    
    theme_options = {'light': 'Light Theme', 'dark': 'Dark Theme'}
    selected_theme = st.selectbox("Select Theme", options=list(theme_options.keys()), 
                                format_func=lambda x: theme_options[x])
    
    if selected_theme != st.session_state.theme:
        st.session_state.theme = selected_theme
        st.rerun()

    if st.session_state.theme == 'dark':
        st.markdown("""
            <style>
            .stApp {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .stApp {
                background-color: #FFFFFF;
                color: #000000;
            }
            </style>
            """, unsafe_allow_html=True)