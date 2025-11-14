import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# CSS للتصميم
st.markdown("""
<style>
body {
    background-color: #f3f7f9;
}

.login-box {
    background-color: white;
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    width: 380px;
    margin: auto;
    text-align: center;
}

.login-title {
    font-size: 28px;
    font-weight: bold;
    color: #1b5e20;
    margin-bottom: 5px;
}

.login-sub {
    font-size: 14px;
    color: #444;
    margin-bottom: 25px;
}

.stButton > button {
    width: 100%;
    border-radius: 8px;
    background-color: #1b5e20 !important;
    color: white !important;
    height: 45px;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# حالة تسجيل الدخول
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# صندوق تسجيل الدخول
st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="login-sub">Welcome to Smart Water Prediction System</div>', unsafe_allow_html=True)

username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")

if st.button("Login"):
    if username.strip() == "":
        st.error("❌ Username cannot be empty.")
    elif " " in username:
        st.error("❌ Username cannot contain spaces.")
    elif len(username) < 3:
        st.error("❌ Username must be at least 3 characters.")
    elif any('\u0600' <= c <= '\u06FF' for c in username):
        st.error("❌ Arabic is not allowed in the username.")
    else:
        if username == "Fai" and password == "192837":
            st.session_state.logged_in = True
            st.success("Login successful! 🎉")
            st.rerun()
        else:
            st.error("❌ Wrong username or password")

st.markdown('</div>', unsafe_allow_html=True)

# الانتقال
if st.session_state.logged_in:
    st.switch_page("app.py")
