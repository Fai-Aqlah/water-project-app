 
       import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

st.markdown("<h2 style='text-align:center;'>🔐 Login Page</h2>", unsafe_allow_html=True)

# تعريف الحالة أول مرة
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# إدخال اسم المستخدم
username = st.text_input("Enter username")

# إدخال كلمة المرور
password = st.text_input("Enter password", type="password")

# زر تسجيل الدخول
if st.button("Login"):

    # 1) التحقق: الحقل فارغ
    if username.strip() == "":
        st.error("❌ Username cannot be empty.")

    # 2) التحقق: وجود مسافات
    elif " " in username:
        st.error("❌ Username cannot contain spaces.")

    # 3) التحقق: الحد الأدنى 4 حروف
    elif len(username) < 4:
        st.error("❌ Username must be at least 4 characters.")

    # 4) التحقق: منع العربية
    elif any('\u0600' <= c <= '\u06FF' for c in username):
        st.error("❌ Arabic is not allowed in the username.")

    else:
        # التحقق النهائي الصحيح
        if username == "Fai" and password == "192837":
            st.session_state.logged_in = True
            st.success("Login successful! 🎉")
            st.rerun()  # ❗ تحديث الصفحة للانتقال
        else:
            st.error("❌ Wrong username or password")

# بعد تسجيل الدخول → الانتقال
if st.session_state.logged_in:
    st.switch_page("app.py")     # ← يعمل الآن بعد rerun
