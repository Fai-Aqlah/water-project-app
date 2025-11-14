import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

# عنوان تسجيل الدخول
st.markdown("<h2 style='text-align:center;'>🔐 Login Page</h2>", unsafe_allow_html=True)

# مسافة
st.write("")

# صناديق الإدخال
username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")

# زر تسجيل الدخول
if st.button("Login"):
    if username == "Fai" and password == "192837":
        st.session_state.logged_in = True
        st.success("Login successful! 🎉")
        
        # الانتقال للصفحة الرئيسية
        st.switch_page("app.py")
    else:
        st.error("Wrong username or password 😢")
