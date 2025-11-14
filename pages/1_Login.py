import streamlit as st
import time

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# ============================
#          CUSTOM CSS
# ============================
st.markdown("""
<style>

/* ===== خلفية متدرجة مع حركة ===== */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #dff3ec, #ffffff, #e7f6ff);
    background-size: 300% 300%;
    animation: bgMove 10s ease infinite;
}

@keyframes bgMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ===== صندوق تسجيل الدخول ===== */
.login-container {
    background: #ffffffd9;
    padding: 40px;
    width: 430px;
    margin: auto;
    margin-top: 60px;
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(50, 150, 120, 0.25);
    border: 1.5px solid #cce8e0;
    backdrop-filter: blur(6px);
    transition: 0.3s ease;
}

/* ضوء ناعم حول الصندوق عند المرور */
.login-container:hover {
    box-shadow: 0 0 35px rgba(50, 150, 120, 0.32);
}

/* ===== عنوان الصفحة ===== */
.login-title {
    text-align: center;
    font-size: 34px;
    font-weight: 700;
    color: #1b8a5a;
    margin-bottom: 5px;
}

/* ===== النص التحتي ===== */
.login-subtext {
    text-align: center;
    color: #555;
    font-size: 16px;
    margin-bottom: 25px;
}

/* ===== تنسيق حقول الإدخال ===== */
.stTextInput input {
    height: 48px !important;
    border-radius: 12px !important;
    border: 2px solid #1b8a5a !important;
    font-size: 18px !important;
    padding-left: 42px !important;
    background-color: #f7fffb !important;
    background-repeat: no-repeat;
    background-position: 12px center;
    background-size: 20px;
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
    height: 48px !important;
    background: linear-gradient(90deg, #1b8a5a, #0277bd);
    color: #fff !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    border-radius: 12px !important;
    border: none;
    transition: 0.25s ease-in-out;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0px 4px 14px rgba(0, 60, 100, 0.25);
}

</style>
""", unsafe_allow_html=True)

# ============================
#        LOGIN BOX
# ============================
st.markdown("<div class='login-container'>", unsafe_allow_html=True)

st.markdown("<div class='login-title'>🔐 Login</div>", unsafe_allow_html=True)
st.markdown("<div class='login-subtext'>Welcome to Smart Water Consumption System</div>", unsafe_allow_html=True)

# الحقول مع المفاتيح للأيقونات
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
        if username == "Fai" and password == "192837":
            st.session_state.logged_in = True
            st.session_state.username = username

            st.success(f"Welcome, {username}! 🎉")
            time.sleep(1)
            st.switch_page("app.py")
        else:
            st.error("❌ Wrong username or password")

st.markdown("</div>", unsafe_allow_html=True)


            
