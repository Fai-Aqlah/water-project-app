import streamlit as st
import re
import time

st.set_page_config(page_title="Login", layout="centered")

# ---------------- HEADER ----------------
header_html = """
<div style="width:75%; margin:auto; padding:25px; border-radius:20px; background:#ffffff; box-shadow:0px 6px 18px rgba(0,0,0,0.15); text-align:center;">
    <h1 style="font-size:48px; font-weight:900; color:#1b4d3e; margin:0;">
        Smart Water System — Login Portal 🔐💧
    </h1>
    <p style="font-size:18px; font-weight:600; margin-top:12px; color:#87CEFA;">
        Please log in to continue
    </p>
</div>
"""


st.markdown(header_html, unsafe_allow_html=True)

# ---------------- INPUTS ----------------
username = st.text_input("Username (English only)", "")
password = st.text_input("Password", type="password")

# ---------------- BUTTON ----------------
if st.button("Login"):

    username_errors = []
    password_errors = []

    # ---------------- USERNAME RULES ----------------
    if username.strip() == "" or not re.match(r"^[A-Za-z0-9]+$", username):
        username_errors.append("English letters and numbers only.")
    if " " in username:
        username_errors.append("No spaces allowed.")
    if re.search(r"[\u0600-\u06FF]", username):
        username_errors.append("No Arabic characters allowed.")
    if not any(c.isalpha() for c in username):
        username_errors.append("Must contain at least one letter.")
    if not any(c.isdigit() for c in username):
        username_errors.append("Must contain at least one number.")

    # ---------------- PASSWORD RULES ----------------
    if password.strip() == "":
        password_errors.append("Password cannot be empty.")
    if len(password) < 8:
        password_errors.append("Minimum length: 8 characters.")
    if " " in password:
        password_errors.append("No spaces allowed.")
    if not re.search(r"[A-Za-z]", password):
        password_errors.append("Password must contain letters.")
    if not re.search(r"[0-9]", password):
        password_errors.append("Password must contain numbers.")
    if re.search(r"[\u0600-\u06FF]", password):
        password_errors.append("No Arabic allowed.")
    if re.search(r"[!@#$%^&*]", password):
        password_errors.append("Symbols not allowed (!@#$%^&*).")

    # ---------------- SHOW ERRORS ----------------
    if username_errors:
        st.markdown(
            f"""
            <div style="background:#ffdddd;padding:15px;border-radius:10px;">
                <h4 style="color:#b00000;">⚠️ Invalid Username</h4>
                <ul>{"".join(f"<li>{e}</li>" for e in username_errors)}</ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    if password_errors:
        st.markdown(
            f"""
            <div style="background:#fff4cc;padding:15px;border-radius:10px;">
                <h4 style="color:#b88600;">⚠️ Invalid Password</h4>
                <ul>{"".join(f"<li>{e}</li>" for e in password_errors)}</ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------------- SUCCESS ----------------
    if not username_errors and not password_errors:
        st.success("Login successful! Redirecting...")
        st.session_state.logged_in = True
        st.session_state.username = username
        time.sleep(4)
        st.switch_page("app.py")

   
       
