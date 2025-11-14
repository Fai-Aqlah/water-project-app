import streamlit as st
import time

# إعداد الصفحة
st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# ===========================
#        CSS STYLE
# ===========================
st.markdown("""
<style>

/* ===== خلفية الصفحة ===== */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(145deg, #eaf3ec, #f8fbf9);
}

/* ===== شريط الوزارة ===== */
.header-bar {
    background-color: #1b5e20;
    padding: 12px;
    border-radius: 10px;
    text-align: center;
    font-size: 24px;
    color: white;
    font-weight: bold;
    margin-bottom: 25px;
}

/* ===== صندوق تسجيل الدخول ===== */
.login-box {
    background-color: #ffffff;
    padding: 35px;
    border-radius: 18px;
    width: 430px;
    margin: auto;
    box-shadow: 0px 6px 22px rgba(0,0,0,0.12);
    animation: fadeSlide 0.7s ease both;
}

/* حركة الدخول */
@keyframes fadeSlide {
    from { opacity: 0; transform: translateY(25px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ===== عنوان Login ===== */
.login-title {
    color: #1b5e20;
    font-size: 30px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 8px;
}

/* ===== النص التحتي ===== */
.sub-text {
    text-align: center;
    color: #444;
    margin-bottom: 25px;
    font-size: 15px;
}

/* ===== مدخلات النص ===== */
.stTextInput input {
    height: 50px !important;
    border-radius: 12px !important;
    border: 1px solid #88a98f !important;
    font-size: 17px !important;
    padding-left: 38px !important;
    background-color: #f8faf8 !important;
    background-size: 18px;
    background-repeat: no-repeat;
    background-position: 10px center;
}

/* ===== أيقونة اسم المستخدم ===== */
#username_input {
    background-image: url("https://img.icons8.com/ios-filled/50/1b5e20/user.png");
}

/* ===== أيقونة كلمة المرور ===== */
#password_input {
    background-image: url("https://img.icons8.com/ios-glyphs/30/1b5e20/lock--v1.png");
}

/* ===== زر تسجيل الدخول ===== */
.stButton > button {
    background-color: #1b5e20 !important;
    color: white !important;
    width: 100%;
    padding: 12px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: bold;
    border: none;
    cursor: pointer;
    transition: 0.25s ease-in-out;
}

.stButton > button:hover {
    background-color: #145218 !important;
    transform: translateY(-2px);
}

/* ===== رسائل الخطأ ===== */
.stAlert {
    border-radius: 12px !important;
    font-size: 16px !important;
}

</style>
""", unsafe_allow_html=True)

# ===========================
#        واجهة الصفحة
# ===========================

st.markdown(
    '<div class="header-bar">Ministry of Environment, Water & Agriculture</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)

# حقول الإدخال
username = st.text_input("Enter username", key="username_input")
password = st.text_input("Enter password", type="password", key="password_input")

# ===========================
#        VALIDATION
# ===========================
if st.button("Login"):

    # 1 — فارغ؟
    if username.strip() == "":
        st.error("❌ Username cannot be empty.")

    # 2 — مسافات؟
    elif " " in username:
        st.error("❌ Username cannot contain spaces.")

    # 3 — الحد الأدنى
    elif len(username) < 3:
        st.error("❌ Username must be at least 3 characters.")

    # 4 — العربية ممنوعة
    elif any('\u0600' <= c <= '\u06FF' for c in username):
        st.error("❌ Arabic is not allowed in the username.")

    else:
        # التحقق النهائي
        if username == "Fai" and password == "192837":
            st.session_state.logged_in = True
            st.session_state.username = username

            st.success(f"Welcome, {username}! 👋")
            time.sleep(1.2)
            st.switch_page("app.py")

        else:
            st.error("❌ Wrong username or password")

st.markdown('</div>', unsafe_allow_html=True)

   


    


   


