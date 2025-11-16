import streamlit as st
import re
import time

# ----------------------------- LOAD CSS -----------------------------
def load_css(file_name):
    with open(file_name) as f:
        st.markdown("<style>" + f.read() + "</style>", unsafe_allow_html=True)

load_css("pages/style_login.css")


# ----------------------------- PAGE CONFIG -----------------------------
st.set_page_config(page_title="Login", layout="centered")


# ----------------------------- HEADER -----------------------------
header_html = """
<div class="login-header">
    <h1>Smart Water System — Login Portal 🔐💧</h1>
    <p>Please log in to continue</p>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)


# ----------------------------- INPUTS -----------------------------
username = st.text_input("Username (English only)", key="login_username")  
password = st.text_input("Password", type="password", key="login_password")


   
                  
if st.button("Login"):

    username_errors = []
    password_errors = []

    # ================= USERNAME RULES =================
    if (
        username.strip() == "" or
        not re.match(r'^[A-Za-z0-9]+$', username) or
        " " in username or
        re.search(r'[\u0600-\u06FF]', username) or
        re.search(r'[!@#$%^&*]', username)
    ):
        username_errors.append("English letters and numbers only")
        username_errors.append("No Arabic characters")
        username_errors.append("No spaces")
        username_errors.append("No symbols (!@#$%^&*)")
        username_errors.append("Cannot be empty")

    # ================= PASSWORD RULES =================
    if (
        password.strip() == "" or
        len(password) < 8 or
        not re.search(r'[A-Za-z]', password) or
        not re.search(r'[0-9]', password) or
        " " in password or
        re.search(r'[\u0600-\u06FF]', password) or
        re.search(r'[!@#$%^&*]', password)
    ):
        password_errors.append("Minimum 8 characters")
        password_errors.append("Must contain letters and numbers")
        password_errors.append("No spaces")
        password_errors.append("No Arabic characters")
        password_errors.append("No symbols (!@#$%^&*)")
        password_errors.append("Cannot be empty")

    # ================= SUCCESS =================
    if not username_errors and not password_errors:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.rerun()
        time.sleep(3)
        st.switch_page("main/app.py")
