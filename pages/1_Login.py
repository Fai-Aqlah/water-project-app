import streamlit as st
import time
import re

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# ===================== CUSTOM CSS =====================
st.markdown("""
<style>

body {
    font-family: 'Poppins', sans-serif !important;
}

/* العنوان */
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #0277bd;
    text-align: center;
}

/* النص تحت العنوان */
.sub-text {
    text-align: center;
    color: #1ba5a5;
    font-size: 20px;
    margin-bottom: 30px;
}

/* حقول الإدخال */
.stTextInput > div > div > input {
    font-size: 20px !important;
    padding: 12px !important;
    border-radius: 12px !important;
    border: 2px solid #0277bd !important;
    text-align: left !important;
}

/* زر الدخول */
.stButton > button {
    background: linear-gradient(90deg, #1ba5a5, #0277bd);
    color: white !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    padding: 10px 40px !important;
    border-radius: 12px !important;
    border: none;
    transition: 0.2s;
}

.stButton > button:hover {
    transform: scale(1.05);
}

/* زر العين داخل الحقل */
.eye-btn {
    width: 35px !important;
    height: 35px !important;
    border-radius: 50% !important;
    background: #e3f2fd !important;
    color: #0277bd !important;
    border: 1px solid #0277bd !important;
    font-size: 17px !important;
}

/* رسالة الترحيب */
.welcome-big {
    font-size: 30px;
    font-weight: 800;
    color: #1ba5a5;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ===================== STATE =====================
if "show_password" not in st.session_state:
    st.session_state.show_password = False

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ===================== PAGE HEADER =====================
st.markdown('<div class="main-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)

st.write("")

# ===================== USERNAME FIELD =====================
username = st.text_input("Enter username", key="username_input")

# ===================== PASSWORD FIELD WITH EYE =====================
col1, col2 = st.columns([10, 1])

with col1:
    password = st.text_input(
        "Enter password",
        type="text" if st.session_state.show_password else "password",
        key="password_input"
    )

with col2:
    eye_clicked = st.button("👁", key="eye_btn")
    if eye_clicked:
        st.session_state.show_password = not st.session_state.show_password

# ===================== VALIDATION RULES =====================
def show_rules():
    st.error("""
**Username Requirements:**  
- Must not be empty  
- Must contain NO spaces  
- Must be at least 3 characters  
- English only (No Arabic letters)  
""")

# ===================== LOGIN BUTTON =====================
if st.button("Login"):
    
    # شروط الاسم
    if username.strip() == "":
        show_rules()

    elif " " in username:
        show_rules()

    elif len(username) < 3:
        show_rules()

    elif any('\u0600' <= c <= '\u06FF' for c in username):
        show_rules()

    else:
        # قبول أي اسم وأي كلمة مرور
        st.session_state.logged_in = True
        st.session_state.username = username

        st.success(f"Welcome, {username}! 👋")
        time.sleep(1)
        st.switch_page("app.py")

   

    



   
