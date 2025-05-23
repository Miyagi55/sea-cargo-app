import streamlit as st
from utils.auth2 import check_auth, logout
from utils.database import get_db_connection


def main():
    if not check_auth():
        st.warning("Por favor, inicie sesión para acceder a esta página")
        st.stop()
    
    st.title("Consultas")
    st.write("Database Queries Page")
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM info_prospectos LIMIT 10")  # Example query
        data = cur.fetchall()
        st.write(data)
        cur.close()
        conn.close()
    except Exception as e:
        st.error(f"Database error: {e}")
    
    
    logout()

if __name__ == "__main__":
    main()