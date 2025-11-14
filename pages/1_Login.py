  import streamlit as st
  import re

# --------- CSS DESIGN ---------
page_css = """
<style>
    body {
        background-color: #f5f7fa;
    }
    .login-title {
        text-align: center;
        font-size: 34px;
        font-weight: bold;
        margin-top: 30px;
        color: #2b6777;
    }
    .login-box {
        background-color: white;
        padding: 30px;
        border-radius: 12px;
        width: 380px;
        margin: auto;
        margin-top: 40px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    .stTextInput > div > div > input {
        border: 1px solid #2b6777 !important;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #2b6777;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        font-size: 17px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #204b57;
    }
</style>
"""
st.markdown(page_css, unsafe_allow_html=True)

# --------- FUNCTIONS ---------

# منع الأحرف العربية
def contains_arabic(text):
    return re.search(r'[\u0600-\u06FF]', text) is not None

# --------- PAGE START ---------

# عنوان الصفحة
st.markdown('<div class="login-title">🔐 Login Page</div>', unsafe_allow_html=True)

# صندوق تسجيل الدخول
with st.container():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    username = st.text_input("Enter username")
    password = st.text_input("Enter password", type="password")

    if st.button("Login"):
        
        # 1) منع الفراغ
        if username.strip() == "" or password.strip() == "":
            st.error("❌ Username and password cannot be empty.")

        # 2) منع العربية
        elif contains_arabic(username) or contains_arabic(password):
            st.error("❌ Arabic is not allowed. Use English only.")

        # 3) يسمح فقط بالحروف الإنجليزية + الأرقام + _
        elif not re.match(r'^[A-Za-z0-9_]+$', username):
            st.error("❌ Username can contain only English letters, numbers, and _")

        # تسجيل دخول صحيح
        elif username == "Fai" and password == "1929837":
            st.session_state.logged_in = True
            st.success("Login successful 🎉")
            st.switch_page("app.py")

        # خطأ في اسم المستخدم أو كلمة المرور
        else:
            st.error("❌ Wrong username or password 😔")

    st.markdown('</div>', unsafe_allow_html=True)

      
