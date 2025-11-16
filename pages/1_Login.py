import streamlit as st
import re
import time

st.set_page_config(page_title="Login", layout="centered")

# ---------------- HEADER ----------------
header_html = """
<div style="
    width:75%;
    margin:auto;
    padding:25px;
    border-radius:20px;
    background:#ffffff;
    box-shadow:0px 6px 18px rgba(0,0,0,0.15);
    text-align:center;
">
    <h1 style="
        font-size:48px;
        font-weight:900;
        color:#1b4d3e;
        margin:0;
    ">
        Smart Water System — Login Portal 🔐💧
    </h1>

    <p style="
        font-size:18px;
        font-weight:600;
        margin-top:12px;
        color:#87CEFA;
    ">
        Please log in to continue
    </p>

</div>
"""

st.markdown(header_html, unsafe_allow_html=True)
st.write("")
st.write("")

# ---------------- INPUTS ----------------
st.markdown('<div class="login-input">', unsafe_allow_html=True)

# ---------------- INPUTS ----------------
st.markdown('<div class="login-input">', unsafe_allow_html=True)

username = st.text_input("Username (English only)", key="username")
password = st.text_input("Password", type="password", key="password")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- BUTTON ----------------
if st.button("Login"):

    username_errors = []
    password_errors = []

    # ---------------- USERNAME RULES ----------------
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

    # ---------------- PASSWORD RULES ----------------
    if (
        password.strip() == "" or
        len(password) < 8 or
        not re.search(r'[A-Za-z]', password) or
        not re.search(r'[0-9]', password) or
        " " in password or
        re.search(r'[\u0600-\u06FF]', password)
    ):
        password_errors.append("Password must be at least 8 characters")
        password_errors.append("Must include letters and numbers")
        password_errors.append("No spaces allowed")
        password_errors.append("No Arabic characters")
        password_errors.append("Cannot be empty")

    # ---------------- SHOW ERRORS ----------------
    if username_errors:
        for err in username_errors:
            st.error(err)

    if password_errors:
        for err in password_errors:
            st.error(err)

    # ---------------- SUCCESS ----------------
    if not username_errors and not password_errors:
        st.success("✅ Login successful!")
        time.sleep(1)
        st.session_state.logged_in = True
        st.session_state.username = username
        st.switch_page("Home.py")


      
