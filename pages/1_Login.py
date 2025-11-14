import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

# عنوان صفحة تسجيل الدخول
st.markdown("<h1 style='text-align:center;'>🔐 Login Page</h1>", unsafe_allow_html=True)

# مربعات الإدخال
username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")

# زر تسجيل الدخول
if st.button("Login"):
    if username == "Fai" and password == "1929837":
        st.success("Login successful! 🎉")
        st.session_state.logged_in = True
        st.session_state.username = username
        st.switch_page("app.py")  
    else:
        st.error("Wrong username or password!")

