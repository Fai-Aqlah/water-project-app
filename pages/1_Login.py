import streamlit as st
import time

# إعداد الصفحة
st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# =========  CSS (نفس تصميم صفحة التنبؤ) =========
st.markdown("""
<style>
.header-bar {
    background-color: #1b5e20; 
    padding: 12px;
    border-radius: 10px;
    text-align: center;
    color: white;
    font-size: 24px;
    font-weight: bold;
}

.login-box {
    background-color: #ffffff;
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
    width: 450px;
    margin: auto;
}

.login-title {
    color: #1b5e20;
    font-size: 30px;
    font-weight: 900;
    text-align: center;
}

.sub-text {
    text-align: center;
    color: #333;
    margin-bottom: 25px;
}

.stTextInput > div > div > input {
    height: 50px;
    font-size: 18px;
    border-radius: 10px;
}

.stButton > button {
    background-color: #1b5e20 !important;
    color: white !important;
    width: 100%;
    padding: 12px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========  حالة تسجيل الدخول =========
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# لو هو أصلاً مسجل دخول من قبل → روحي مباشرة لصفحة app
if st.session_state.logged_in:
    st.switch_page("app.py")

# =========  الواجهة =========
st.markdown('<div class="header-bar">Ministry of Environment, Water & Agriculture</div>', unsafe_allow_html=True)
st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)

username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")

# =========  التحقق من الإدخال =========
if st.button("Login"):

    # شرط 1 — لا يكون فاضي
    if username.strip() == "":
        st.error("❌ Username cannot be empty.")

    # شرط 2 — لا يحتوي مسافات
    elif " " in username:
        st.error("❌ Username cannot contain spaces.")

    # شرط 3 — على الأقل 3 حروف
    elif len(username) < 3:
        st.error("❌ Username must be at least 3 characters.")

    # شرط 4 — منع العربية
    elif any('\u0600' <= c <= '\u06FF' for c in username):
        st.error("❌ Arabic is not allowed in the username.")

    # التحقق النهائي لاسم المستخدم وكلمة المرور
    else:
        if username == "Fai" and password == "192837":
            st.session_state.logged_in = True
            st.session_state.username = username

            # ✅ هنا تظهر رسالة الترحيب في صفحة تسجيل الدخول
            st.success(f"Welcome, {username}! 👋")

            # ننتظر ثانية ثم ننتقل لصفحة التنبؤ
            time.sleep(1.5)
            st.switch_page("app.py")
        else:
            st.error("❌ Wrong username or password")

st.markdown("</div>", unsafe_allow_html=True)

   


