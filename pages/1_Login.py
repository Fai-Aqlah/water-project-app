import streamlit as st
import re

# إعداد الصفحة
st.set_page_config(page_title="Login", layout="centered")

# ---------------------------------------------------
#                SESSION STATE
# ---------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "show_pass" not in st.session_state:
    st.session_state.show_pass = False

# إذا المستخدم مسجّل دخول: انقليه لصفحة التنبؤ مباشرة
if st.session_state.logged_in:
    st.switch_page("app.py")


# ---------------------------------------------------
#                      CSS
# ---------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #f5f7fb;
}

/* عنوان الصفحة */
.login-title {
    text-align:center;
    font-size: 32px;
    font-weight: bold;
    color: #2b4c7e;
    margin-bottom: 25px;
}

/* مربعات الإدخال */
.stTextInput > div > div > input {
    border: 1.6px solid #c9d6e8 !important;
    border-radius: 10px !important;
    padding: 12px !important;
    font-size: 16px !important;
}

/* زر الدخول */
.stButton > button {
    width: 100%;
    background-color: #2b4c7e !important;
    color: white !important;
    padding: 10px;
    border-radius: 10px;
    font-size: 17px;
    border: none !important;
}

/* الحاوية الخاصة بالعين داخل المستطيل */
.password-wrapper {
    position: relative;
}

/* أيقونة العين داخل البوكس */
.eye-icon {
    position: absolute;
    right: 14px;
    top: 45px;
    font-size: 18px;
    cursor: pointer;
    color: #2b4c7e;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
#              دالة التحقق من الاسم
# ---------------------------------------------------
def is_valid_username(u):
    return re.match(r'^[A-Za-z0-9_]+$', u)


# ---------------------------------------------------
#                    واجهة الدخول
# ---------------------------------------------------
st.markdown("<div class='login-title'>🔐 Login Page</div>", unsafe_allow_html=True)

username = st.text_input("Username (English only)", placeholder="Enter username...")


# ------------------ كلمة المرور + زر العين داخل المربع ------------------
st.markdown('<div class="password-wrapper">', unsafe_allow_html=True)

password = st.text_input(
    "Password",
    type="text" if st.session_state.show_pass else "password",
    placeholder="Enter password..."
)

# زر العين داخل المستطيل
eye_icon = "&#128065;" if st.session_state.show_pass else "&#128065;&#x0336;"
# 👁️ عند ظهور الباسورد — 👁̶ عند إخفائها

# نجعل الأيقونة زر قابل للضغط
eye_clicked = st.button("", key="eye_toggle")
st.markdown(f'<span class="eye-icon">{eye_icon}</span>', unsafe_allow_html=True)

if eye_clicked:
    st.session_state.show_pass = not st.session_state.show_pass
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------------------
#               LOGIN BUTTON ACTION
# ---------------------------------------------------
if st.button("Login", key="login_btn"):
    if username.strip() == "":
        st.error("❌ Please enter a username.")
    elif not is_valid_username(username):
        st.error("❌ Username must contain English letters or numbers only.")
    elif password.strip() == "":
        st.error("❌ Please enter your password.")
    else:
        st.success(f"🎉 Welcome, {username}!")
        st.session_state.logged_in = True
        st.switch_page("app.py")

       
       




   



