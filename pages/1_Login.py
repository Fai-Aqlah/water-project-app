import streamlit as st
import re
import time
def load_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_local_css("pages/style_login.css")
st.set_page_config(page_title="Login", layout="centered")

# ------------------ HEADER ------------------
st.markdown("""
<div style="
    text-align:center;
    margin-top:20px;
    margin-bottom:40px;
">
    <h1 style="color:#1b4d3e; font-size:48px; font-weight:900;">
        Smart Water System 💧 – Login Portal 
    </h1>
</div>
""", unsafe_allow_html=True)


username = st.text_input("Username (English only)", key="username_input")
password = st.text_input("Password", type="password", key="password_input")


username_errors = []
password_errors = []

if st.button("Login", type="secondary"):

    # ------------------ USERNAME RULES ------------------
    if (
        username.strip() == "" or
        not re.match(r'^[A-Za-z0-9]+$', username) or
        re.search(r'[\u0600-\u06FF]', username) or
        " " in username or
        re.search(r'[!@#$%^&*]', username)
    ):
        username_errors.append("English letters and numbers only")
        username_errors.append("No Arabic characters")
        username_errors.append("No spaces")
        username_errors.append("No symbols (!@#$%^&*)")
        username_errors.append("Cannot be empty")

    # ------------------ PASSWORD RULES ------------------
    if (
        password.strip() == "" or
        len(password) < 8 or
        not re.search(r'[A-Za-z]', password) or
        not re.search(r'[0-9]', password) or
        re.search(r'[\u0600-\u06FF]', password)
    ):
        password_errors.append("Password must be at least 8 characters")
        password_errors.append("Must include letters and numbers")
        password_errors.append("No Arabic characters")
        password_errors.append("No spaces allowed")
        password_errors.append("Cannot be empty")

    # ------------------ SHOW USERNAME ERRORS ------------------
    if username_errors:
        st.markdown(
            f"""
            <div class="error-box">
                <div class="error-title">❌ Username Errors</div>
                <ul class="error-list">
                    {"".join(f"<li>{e}</li>" for e in username_errors)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ------------------ SHOW PASSWORD ERRORS ------------------
    if password_errors:
        st.markdown(
            f"""
            <div class="warning-box">
                <div class="warning-title">⚠️ Password Errors</div>
                <ul class="warning-list">
                    {"".join(f"<li>{e}</li>" for e in password_errors)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ------------------ SUCCESS ------------------
    if not username_errors and not password_errors:
        st.session_state.logged_in = True
        st.session_state.username = username

        st.success("Login Successful!")

        st.markdown(
            f"""
            <div style="text-align:center; margin-top:20px;">
                <h2 style="color:#1b4d3e; font-size:32px; font-weight:900;">
                    Welcome, {st.session_state.username}! 👋💧
                </h2>
                <p style="color:#1b4d3e; font-size:20px; font-weight:600;">
                    Glad to have you here — let’s start predicting your water consumption 🌿
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(5)
        st.switch_page("home.py")



   
