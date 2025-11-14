import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# إنشاء حالة الجلسة لو غير موجودة
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# لو المستخدم بالفعل مسجل دخول → تحويل للصفحة الرئيسية (app.py)
if st.session_state.logged_in:
    st.switch_page("app.py")

# -----------------------
# واجهة تسجيل الدخول
# -----------------------

st.markdown("<h1 style='text-align:center;'>🔐 Login Page</h1>", unsafe_allow_html=True)

username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")

if st.button("Login"):
    if username == "Fai" and password == "1929837":
        st.session_state.logged_in = True
        st.success("Login successful 🎉")
        st.experimental_rerun()
    else:
        st.error("Wrong username or password ❌")
