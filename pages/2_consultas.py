import streamlit as st
from utils.auth import check_auth, logout
from utils.database import get_db_connection
from utils.theme import set_theme

def main():
    if not check_auth():
        st.warning("Please login to access this page")
        st.stop()
    
    st.title("Consultas")
    st.write("Database Queries Page")
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM your_table LIMIT 10")  # Example query
        data = cur.fetchall()
        st.write(data)
        cur.close()
        conn.close()
    except Exception as e:
        st.error(f"Database error: {e}")
    
    set_theme()
    logout()

if __name__ == "__main__":
    main()