import streamlit as st
import re
import time

def load_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# حمّلي CSS من داخل مجلد pages
load_local_css("pages/style_login.css")

st.set_page_config(page_title="Login", layout="centered")

# ---------------- HEADER ----------------
header_html = """
<div style="width:75%; margin:auto; padding:25px; border-radius:20px; background:#ffffff;
            box-shadow:0px 6px 18px rgba(0,0,0,0.15); text-align:center;">
    <h1 style="font-size:48px; font-weight:900; color:#1b4d3e; margin:0;">
        Smart Water System — Login Portal 🔐💧
    </h1>
    <p style="font-size:18px; font-weight:600; margin-top:12px; color:#87CEFA;">
        Please log in to continue
    </p>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

st.write("")  
st.write("")  

# ---------------- INPUTS ----------------
st.markdown('<div class="login-input">', unsafe_allow_html=True)
username = st.text_input("Username (English only)", key="username")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="login-input">', unsafe_allow_html=True)
password = st.text_input("Password", type="password", key="password")
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
        re.search(r'[\u0600-\u06FF]', password) or
        re.search(r'[!@#$%^&*]', password)
    ):
        password_errors.append("Minimum 8 characters")
        password_errors.append("Must contain letters and numbers")
        password_errors.append("No spaces")
        password_errors.append("No Arabic characters")
        password_errors.append("No symbols allowed (!@#$%^&*)")
        password_errors.append("Cannot be empty")

    # ---------------- SHOW ERRORS ----------------
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

 # ---------------- SUCCESS: username & password valid ----------------
if not username_errors and not password_errors:

    # ضعي الجلسة أول شيء قبل أي طباعة
    st.session_state.logged_in = True
    st.session_state.username = username

    # بعدين اطبعي الرسالة
    st.markdown(
        f"""
        <div style="
            background:#f0fff4;
            padding:25px;
            border-radius:15px;
            border-left:7px solid #1b4d3e;
            margin-top:20px;
            text-align:center;">
            
            <h2 style="color:#1b4d3e; font-size:40px; margin:0;">
                Welcome, {username}! 👋💧
            </h2>

            <p style="color:#1b4d3e; font-size:22px; font-weight:600; margin-top:10px;">
                Glad to have you here — let's start predicting your water consumption 🌱
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # الانتقال بعد 3 ثوانٍ
    time.sleep(3)
    st.switch_page("pages/app.py")


       
        
    


   
       
