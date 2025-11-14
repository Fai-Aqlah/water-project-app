import streamlit as st
import time
import re

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")


st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #e8f5f1, #dff1ff);
    font-family: 'Poppins', sans-serif !important;
}

/* == LOGIN CARD == */
.login-card {
    background: white;
    padding: 40px;
    max-width: 450px;
    margin: 80px auto;
    border-radius: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
}

/* العنوان الرئيسي */
.login-title {
    font-size: 36px;
    font-weight: 800;
    color: #0277bd;
    text-align: center;
    margin-bottom: 5px;
}

/* النص تحت العنوان */
.sub-text {
    font-size: 16px;
    color: #1ba85a;
    text-align: center;
    margin-bottom: 28px;
}

/* == حقول الإدخال == */
.stTextInput > div > div > input {
    font-size: 18px !important;
    padding: 14px !important;
    border-radius: 12px !important;
    border: 2px solid #0277bd !important;
}

/* العين داخل مربع الباسورد */
.eye-btn {
    position: relative;
    top: 8px;
    right: 12px;
    background: #e3f2fd !important;
    color: #0277bd !important;
    border-radius: 50%;
    width: 36px !important;
    height: 36px !important;
    border: 1px solid #0277bd !important;
    font-size: 18px !important;
    padding: 0 !important;
}

/* زر الدخول */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #1ba85a, #0277bd);
    color: white !important;
    font-size: 20px !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    padding: 12px !important;
    margin-top: 15px;
    border: none;
}

.stButton>button:hover {
    transform: scale(1.04);
}

/* رسالة الترحيب */
.welcome-msg {
    font-size: 26px;
    color: #1ba85a;
    text-align: center;
    font-weight: 700;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =================== STATE ===================
if "show_password" not in st.session_state:
    st.session_state.show_password = False
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# =================== LOGIN CARD ===================
st.markdown('<div class="login-card">', unsafe_allow_html=True)

st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)

# =============== USERNAME FIELD ==================
username = st.text_input("Enter username", key="username_input")

# =============== PASSWORD FIELD ==================
col1, col2 = st.columns([10, 1])

with col1:
    password = st.text_input(
        "Enter password",
        type="text" if st.session_state.show_password else "password",
        key="password_input"
    )

with col2:
    eye = st.button("👁", key="eye_btn")
    if eye:
        st.session_state.show_password = not st.session_state.show_password


# ================== VALIDATION ==================
def show_rules():
    st.error("""
**Username Requirements:**
• Must not be empty  
• Must contain no spaces  
• Must be at least 3 characters  
• English only (No Arabic letters)
""")

# ================= LOGIN BUTTON ==================
if st.button("Login"):

    if username.strip() == "":
        show_rules()

    elif " " in username:
        show_rules()

    elif len(username) < 3:
        show_rules()

    elif any('\u0600' <= c <= '\u06FF' for c in username):
        show_rules()

    else:
        st.success(f"<div class='welcome-msg'>Welcome, {username}! 👋</div>", unsafe_allow_html=True)
        st.session_state.logged_in = True
        st.session_state.username = username
        time.sleep(1)
        st.switch_page("app.py")

st.markdown("</div>", unsafe_allow_html=True)


   

   
   
