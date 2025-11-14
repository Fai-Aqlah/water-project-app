 import streamlit as st

# إعداد الصفحة

st.markdown("<h2 style='text-align:center;'>🔐 Login Page</h2>", unsafe_allow_html=True)

# إدخال اسم المستخدم
username = st.text_input("Enter username")

# منع العربية
if any('\u0600' <= c <= '\u06FF' for c in username):
    st.error("❌ Arabic letters are not allowed. Please use English only.")

# إدخال الرقم السري
password = st.text_input("Enter password", type="password")

# زر تسجيل الدخول
if st.button("Login"):

    # التحقق من الشروط
    if username.strip() == "":
        st.error("❌ Username cannot be empty.")
    elif " " in username:
        st.error("❌ Username cannot contain spaces.")
    elif len(username) < 4:
        st.error("❌ Username must be at least 4 characters.")
    elif any('\u0600' <= c <= '\u06FF' for c in username):
        st.error("❌ Arabic is not allowed in the username.")
    else:
        # التحقق من بيانات الدخول
        if username == "Fai" and password == "1929837":
            st.success("Login successful 🎉")
            st.session_state.logged_in = True
            st.switch_page("app.py")
        else:
            st.error("❌ Wrong username or password.")
