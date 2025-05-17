# 🔐 AI-Powered Sales Assistant (Secure Streamlit App)

## 🚀 Overview
This project is an **AI-powered Streamlit web app** designed to assist the sales team by retrieving data from a **PostgreSQL database using Natural Language Processing (NLP)** to give data access to employees and handling prospect/client information

### 🔑 Security-Focused Authentication
The app features a **hardened authentication system** to ensure controlled access and data integrity, preventing unauthorized access and brute-force attacks.

## 🛡️ Security Features
This project includes two authentication implementations:
- **`utils/auth2.py` (Hardened)** ✅: A secure authentication system with robust security measures.
- **`utils/auth.py` (Unsafe Example)** ❌: A weak authentication system provided for comparison.

### 🔍 Key Security Enhancements in `auth2.py`
✅ **Bcrypt for Secure Password Hashing:**
   - Uses `bcrypt` with **14 rounds** of salting for strong password encryption.
   - Ensures that even if passwords are leaked, they remain resistant to attacks.

✅ **Rate Limiting & Lockout Protection:**
   - Implements **rate limiting** (max **5 login attempts**) before locking the user for **15 minutes** to prevent brute-force attacks.
   - Uses session-based tracking to monitor failed login attempts.

✅ **Secure Input Validation:**
   - Restricts input length to **50 characters** to prevent buffer overflows.
   - Only allows **alphanumeric characters and underscores** to mitigate SQL injection and XSS attacks.

✅ **Secure Session Management:**
   - Generates a **random session token** using `secrets.token_hex(16)`.
   - Ensures the session token is **stored server-side** and validated during user interaction.

✅ **Logging & Error Handling:**
   - Implements **logging** to track authentication attempts and potential security threats.
   - Includes **retry logic** for database queries to ensure system resilience.

## 📥 Installation
Ensure you have the required dependencies installed:
using `uv`:
```bash
uv install
```

## ▶️ Usage
Run the Streamlit app:
```bash
uv run python3 streamlit run app.py
```
This will:
1. ✅ Prompt users to **securely log in**.
2. 🛡️ **Validate user credentials** against the PostgreSQL database.
3. 🤖 Allow users to **retrieve data using Natural Language queries**.

## 📊 Core Feature: NLP-Powered Data Retrieval (pending)
Once authenticated, users can ask the AI **natural language questions** about the database (e.g., "What were the total sales last quarter?") and receive relevant results.
In this case, we are migrating data from many Excel files into a PostgreSQL database. To achieve this, we might know the business processes, their main mission, and recognize the entities (tables) of our new database. Here is a basic example of how to model and normalize data:

![image](https://github.com/Miyagi55/sea-cargo-app/blob/main/Blank%20diagram%20(4).png)

## 🔥 Why This Matters
- **Prevents unauthorized access** 🔐
- **Strengthens authentication security** 🛡️
- **Reduces brute-force risks** 🚫
- **Ensures data integrity** 📊

---
💡 *This project demonstrates a real-world implementation of secure authentication vs. an insecure one to highlight best practices in web app security!*

