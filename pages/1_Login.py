import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Login", page_icon="🔐")

st.markdown("<h2 style='text-align:center;'>🔐 Login Page</h2>", unsafe_allow_html=True)

# إدخال البيانات
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# زر الدخول
if st.button("Login"):
    if username == "Fai" and password == "1929837":
        st.success("Login Successful 🎉")
        st.session_state.logged_in = True
        st.switch_page("app")   # ينقلك للصفحة الرئيسية
    else:
        st.error("Wrong username or password ❌")
