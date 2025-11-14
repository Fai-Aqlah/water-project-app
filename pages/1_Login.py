import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# ========== STYLE ==========
st.markdown("""
<style>

.header-bar {
    background-color: #1b5e20; 
    padding: 12px;
    border-radius: 10px;
    text-align: center;
    color: white;
    font-size: 24px;
    font-weight: bold;
}

.login-box {
    background-color: #ffffff;
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
    width: 450px;
    margin: auto;
}

.login-title {
    color: #1b5e20;
    font-size: 30px;
    font-weight: 900;
    text-align: center;
}

.sub-text {
    text-align: center;
    color: #333;
    margin-bottom: 25px;
}

.stTextInput > div > div > input {
    height: 50px;
    font-size: 18px;
    border-radius: 10px;
}

.stButton > button {
    background-color: #1b5e20 !important;
    color: white !important;
    width: 100%;
    padding: 12px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ========== LOGIC ==========
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.markdown('<div class="header-bar">Ministry of Environment, Water & Agriculture</div>', unsafe_allow_html=True)
st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)

username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")

# ========== VALIDATION ==========
if st.button("Login"):

    # شرط 1 — عدم ترك الحقل فارغ
    if username.strip() == "":
        st.error("❌ Username cannot be empty.")

    # شرط 2 — يمنع المسافات
    elif " " in username:
        st.error("❌ Username cannot contain spaces.")

    # شرط 3 — الحد الأدنى 3 حروف
    elif len(username) < 3:
        st.error("❌ Username must be at least 3 characters.")

    # شرط 4 — يمنع العربية
    elif any('\u0600' <= c <= '\u06FF' for c in username):
        st.error("❌ Arabic is not allowed in the username.")

   # التحقق النهائي
else:
    if username == "Fai" and password == "192837":
        st.session_state.logged_in = True
        st.session_state.username = username   # حفظ اسم المستخدم

        # رسالة ترحيب تظهر في صفحة تسجيل الدخول نفسها
        st.success(f"Welcome, {username}! 👋")

        # الانتقال بعد ثانية
        st.experimental_sleep(1)
        st.switch_page("app.py")

    else:
        st.error("❌ Wrong username or password")

 


              st.success("Login successful! 🎉")
              st.rerun()
        else:
             st.error("❌ Wrong username or password")

st.markdown("</div>", unsafe_allow_html=True)

# الانتقال
if st.session_state.logged_in:
    st.switch_page("app.py")

    
   
