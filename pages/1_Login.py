import streamlit as st
import time
import re

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")


# ================= CUSTOM CSS =================
st.markdown("""
<style>

body {
    font-family: 'Poppins', sans-serif !important;
}

/* عنوان الصفحة */
.main-title {
    font-size: 46px;
    font-weight: 800;
    color: #0277bd;  /* أزرق */
    text-align: center;
    margin-bottom: -5px;
}

/* النص تحت العنوان */
.sub-text {
    text-align: center;
    color: #1ba85a; /* أخضر */
    font-size: 20px;
    margin-bottom: 25px;
}

/* حقول الإدخال */
.stTextInput > div > div > input {
    font-size: 22px !important;
    padding: 12px !important;
    border-radius: 12px !important;
    border: 2px solid #0277bd !important;
    text-align: left !important;
}

/* زر تسجيل الدخول */
.stButton>button {
    background: linear-gradient(90deg, #1ba85a, #0277bd);
    color: white !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    padding: 12px 45px !important;
    border-radius: 12px !important;
    border: none;
    transition: 0.2s;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* زر العين داخل مربع الإدخال */
.eye-btn {
    width: 36px !important;
    height: 36px !important;
    padding: 0 !important;
    border-radius: 50% !important;
    background: #e3f2fd !important;
    color: #0277bd !important;
    border: 1px solid #0277bd !important;
    font-size: 18px !important;
    margin-top: 32px !important;
}

/* رسالة الترحيب */
.welcome-big {
    font-size: 30px;
    font-weight: 800;
    color: #1ba85a;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ================= STATE FOR PASSWORD TOGGLE =================
if "show_password" not in st.session_state:
    st.session_state.show_password = False


# ================= PAGE HEADER =================
st.markdown('<div class="main-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)
st.write("")


# ================= USERNAME FIELD =================
username = st.text_input("Enter username", key="username_input")


# ================= PASSWORD FIELD + EYE =================
col1, col2 = st.columns([10, 1])

with col1:
    password = st.text_input(
        "Enter password",
        type="text" if st.session_state.show_password else "password",
        key="password_input"
    )

with col2:
    eye_clicked = st.button("👁️", key="eye_btn", help="Show / Hide Password")
    if eye_clicked:
        st.session_state.show_password = not st.session_state.show_password


# ================= VALIDATION RULES =================
def show_rules():
    st.error(
        "**Username Requirements:**\n"
        "- Must not be empty\n"
        "- Must contain no spaces\n"
        "- Must be at least 3 characters\n"
        "- English only (No Arabic letters)"
    )


# ================= LOGIN BUTTON =================
if st.button("Login"):
    # الشروط
    if username.strip() == "":
        show_rules()

    elif " " in username:
        show_rules()

    elif len(username) < 3:
        show_rules()

    elif any('\u0600' <= c <= '\u06FF' for c in username):
        show_rules()

    else:
        # نجاح
        st.markdown(
            f"<div class='welcome-big'>Welcome, {username}! 👋</div>",
            unsafe_allow_html=True
        )
        st.session_state.logged_in = True
        st.session_state.username = username

        time.sleep(1)
        st.switch_page("app.py")

    
    
    
    
       
