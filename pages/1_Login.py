import streamlit as st
import time

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# ============================
#          CUSTOM CSS
# ============================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* ===== خلفية متدرجة مع حركة ===== */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #dff3ec, #ffffff, #e7f6ff);
    background-size: 300% 300%;
    animation: bgMove 8s ease infinite;
    font-family: 'Poppins', sans-serif;
}

@keyframes bgMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ===== صندوق تسجيل الدخول ===== */
.login-container {
    background: #ffffffec;
    padding: 40px;
    width: 450px;
    margin: auto;
    margin-top: 40px;
    border-radius: 20px;
    box-shadow: 0 0 30px rgba(60, 140, 110, 0.25);
    border: 1.5px solid #cce8e0;
    backdrop-filter: blur(5px);
    transition: 0.3s ease;
}

/* ضوء ناعم حول الصندوق */
.login-container:hover {
    box-shadow: 0 0 40px rgba(50, 150, 120, 0.32);
}

/* ===== عنوان الصفحة ===== */
.login-title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    color: #1b8a5a;
    margin-bottom: 10px;
}

/* ===== النص التحتي ===== */
.login-subtext {
    text-align: center;
    color: #444;
    font-size: 18px;
    margin-bottom: 30px;
}

/* ===== تنسيق حقول الإدخال ===== */
.stTextInput input {
    height: 50px !important;
    border-radius: 12px !important;
    border: 2px solid #1b8a5a !important;
    font-size: 20px !important;
    padding-left: 45px !important;
    background-color: #f5fff9 !important;
    background-repeat: no-repeat;
    background-position: 12px center;
    background-size: 22px;
    font-weight: 500;
}

/* أيقونة المستخدم */
#username_input {
    background-image: url("https://img.icons8.com/ios-filled/50/1b8a5a/user.png");
}

/* أيقونة القفل */
#password_input {
    background-image: url("https://img.icons8.com/ios-glyphs/30/1b8a5a/lock--v1.png");
}

/* ===== زر تسجيل الدخول ===== */
.stButton>button {
    width: 100%;
    height: 50px !important;
    background: linear-gradient(90deg, #1b8a5a, #0277bd);
    color: #fff !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    border: none;
    transition: 0.25s ease-in-out;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0px 4px 14px rgba(0, 60, 100, 0.3);
}

</style>
""", unsafe_allow_html=True)

# ============================
#        LOGIN BOX
# ============================

st.markdown("<div class='login-container'>", unsafe_allow_html=True)

st.markdown("<div class='login-title'>🔐 Login</div>", unsafe_allow_html=True)
st.markdown("<div class='login-subtext'>Welcome to Smart Water Consumption System</div>", unsafe_allow_html=True)

username = st.text_input("Enter username", key="username_input")
password = st.text_input("Enter password", type="password", key="password_input")

# ============================
#        VALIDATION
# ============================
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
        if username == "Fai" and password == "1929837":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}! 🎉")
            time.sleep(1)
            st.switch_page("app.py")
        else:
            st.error("❌ Wrong username or password")

st.markdown("</div>", unsafe_allow_html=True)

  

           
