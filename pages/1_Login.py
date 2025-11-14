import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# ========== STYLE EXACTLY LIKE HOME PAGE ==========
st.markdown("""
<style>

body {
    background-color: #f4f9f6;
}

/* نفس تنسيق العنوان الرئيسي */
.header-bar {
    background-color: #1b5e20; 
    padding: 12px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 25px;
    color: white;
    font-size: 24px;
    font-weight: bold;
}

/* صندوق الدخول مثل صندوق التنبؤ */
.login-box {
    background-color: #ffffff;
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
    width: 500px;
    margin: auto;
}

/* العناوين */
.login-title {
    color: #1b5e20;
    font-size: 30px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 10px;
}

.sub-text {
    text-align: center;
    color: #333;
    margin-bottom: 25px;
}

/* تنسيق حقول الإدخال */
.stTextInput > div > div > input {
    height: 50px;
    font-size: 18px;
    border-radius: 10px;
    border: 1px solid #8fb89c;
}

/* زر تسجيل الدخول نفس أزرار صفحة التنبؤ */
.stButton > button {
    background-color: #1b5e20 !important;
    color: white !important;
    width: 100%;
    padding: 12px 0px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ========== LOGIC ==========
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ========== HEADER (نفس شريط صفحة التنبؤ) ==========
st.markdown('<div class="header-bar">Ministry of Environment, Water & Agriculture</div>', unsafe_allow_html=True)

# ========== LOGIN BOX ==========
st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)

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
        st.error("❌ Arabic is not allowed.")
    else:
        if username == "Fai" and password == "192837":
            st.session_state.logged_in = True
            st.success("Login successful! 🎉")
            st.rerun()
        else:
            st.error("❌ Wrong username or password")

st.markdown("</div>", unsafe_allow_html=True)

# ========== REDIRECT ==========
if st.session_state.logged_in:
    st.switch_page("app.py")


    
