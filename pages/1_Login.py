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


# ----------------------------- BUTTON -----------------------------
if st.button("Login"):

    username_errors = []
    password_errors = []

    # ----------------------- USERNAME RULES -----------------------
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

    # ----------------------- PASSWORD RULES -----------------------
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
        password_errors.append("No symbols allowed (!@#$%^&*)")
        password_errors.append("Cannot be empty")


    # -------------------------- SHOW ERRORS --------------------------
    if username_errors:
        st.markdown(
            f"""
            <div class="error-box">
                <div class="error-title">❌ Invalid Username</div>
                <ul class="error-list">
                    {''.join(f"<li>{e}</li>" for e in username_errors)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    if password_errors:
        st.markdown(
            f"""
            <div class="warning-box">
                <div class="warning-title">⚠️ Invalid Password</div>
                <ul class="warning-list">
                    {''.join(f"<li>{e}</li>" for e in password_errors)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )


   # ------------------------ SUCCESS CASE ------------------------
if not username_errors and not password_errors:

    st.session_state.logged_in = True
    st.session_state.username = username

    # ========= WELCOME MESSAGE (exact design like the image) =========
    welcome_html = f"""
        <h2 style="color:#1b4d3e; font-size:48px; font-weight:900; margin-top:10px;">
            Welcome, {username}! 👋💧
        </h2>

        <p style="color:#1b4d3e; font-size:26px; font-weight:600; margin-top:5px;">
            Glad to have you here — let's start predicting your water consumption 🍃
        </p>
    """

    st.markdown(welcome_html, unsafe_allow_html=True)

    time.sleep(3)
    st.switch_page("main/app.py")
