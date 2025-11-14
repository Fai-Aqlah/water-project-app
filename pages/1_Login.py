import streamlit as st
import re

# إعداد الصفحة
st.set_page_config(page_title="Login", layout="centered")

# -----------------------------------
#     SESSION STATE
# -----------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# إذا مسجل دخول → تحويل للتنبؤ
if st.session_state.logged_in:
    st.switch_page("app.py")


# -----------------------------------
#     CSS بسيط للتجميل
# -----------------------------------
st.markdown("""
<style>

body {
    background-color: #f5f7fb;
}

/* عنوان الصفحة */
.login-title {
    text-align:center;
    font-size: 30px;
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

</style>
""", unsafe_allow_html=True)


# -----------------------------------
#    دالة التحقق من اسم المستخدم
# -----------------------------------
def is_valid_username(u):
    return re.match(r'^[A-Za-z0-9_]+$', u)


# -----------------------------------
#     واجهة تسجيل الدخول
# -----------------------------------
st.markdown("<div class='login-title'>🔐 Login Page</div>", unsafe_allow_html=True)

# اسم المستخدم
username = st.text_input(
    "Username (English only)",
    placeholder="Enter username..."
)

# كلمة المرور (بدون عين)
password = st.text_input(
    "Password",
    type="password",
    placeholder="Enter password..."
)


# -----------------------------------
#        زر تسجيل الدخول
# -----------------------------------
if st.button("Login"):
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



