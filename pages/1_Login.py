import streamlit as st
import time
from style import load_style
load_style()

# إعداد الصفحة
st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")


#        واجهة الصفحة
# ===========================

st.markdown(
    '<div class="header-bar">Ministry of Environment, Water & Agriculture</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)

# حقول الإدخال
username = st.text_input("Enter username", key="username_input")
password = st.text_input("Enter password", type="password", key="password_input")

# ===========================
#        VALIDATION
# ===========================
if st.button("Login"):

    # 1 — فارغ؟
    if username.strip() == "":
        st.error("❌ Username cannot be empty.")

    # 2 — مسافات؟
    elif " " in username:
        st.error("❌ Username cannot contain spaces.")

    # 3 — الحد الأدنى
    elif len(username) < 3:
        st.error("❌ Username must be at least 3 characters.")

    # 4 — العربية ممنوعة
    elif any('\u0600' <= c <= '\u06FF' for c in username):
        st.error("❌ Arabic is not allowed in the username.")

    else:
        # التحقق النهائي
        if username == "Fai" and password == "192837":
            st.session_state.logged_in = True
            st.session_state.username = username

            st.success(f"Welcome, {username}! 👋")
            time.sleep(1.2)
            st.switch_page("app.py")

        else:
            st.error("❌ Wrong username or password")

st.markdown('</div>', unsafe_allow_html=True)

   


    


   


