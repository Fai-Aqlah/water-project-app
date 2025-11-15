import streamlit as st
import re
import time

st.set_page_config(page_title="Login", layout="centered")

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

# ---------------- INPUTS ----------------
username = st.text_input("Username (English only)", "")
password = st.text_input("Password", type="password")

# ---------------- BUTTON ----------------
if st.button("Login"):
    
    username_errors = []
    password_errors = []

    # Username validation
    if (
        username.strip() == "" or
        not re.match(r"^[A-Za-z0-9]+$", username)
    ):
        username_errors.append("Use English letters and numbers only (no spaces / no Arabic).")

    # Password validation
    if (
        password.strip() == "" or
        len(password) < 8 or
        not re.search(r"[A-Za-z]", password) or
        not re.search(r"[0-9]", password)
    ):
        password_errors.append("Password must contain letters + numbers and be at least 8 characters.")

    # Show username errors
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

    # Show password errors
    if password_errors:
        st.markdown(
            f"""
            <div style="background:#fff4cc;padding:15px;border-radius:10px;">
                <h4 style="color:#bb8800;">⚠️ Invalid Password</h4>
                <ul>{"".join(f"<li>{e}</li>" for e in password_errors)}</ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # SUCCESS
    if not username_errors and not password_errors:
        st.success("Login successful! Redirecting...")
        st.session_state.logged_in = True
        st.session_state.username = username
        time.sleep(1)
        st.switch_page("app.py")


  
   

          

   
               
      
