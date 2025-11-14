import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# حالة إظهار/إخفاء كلمة المرور
if "show_password" not in st.session_state:
    st.session_state.show_password = False

# -------------------------------------------------------
#                        CSS
# -------------------------------------------------------
st.markdown("""
<style>

body {
    font-family: 'Poppins', sans-serif !important;
}

/* العنوان */
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #0277bd;
    text-align: center;
}

/* النص تحت العنوان */
.sub-text {
    text-align: center;
    color: #1ba85a;
    font-size: 20px;
    margin-bottom: 40px;
}

/* حقول الإدخال */
.stTextInput > div > div > input {
    font-size: 20px !important;
    padding: 14px !important;
    border-radius: 12px !important;
    border: 2px solid #0277bd !important;
}

/* زر تسجيل الدخول */
.stButton>button {
    background: linear-gradient(90deg, #1ba85a, #0277bd);
    color: white !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    padding: 12px 35px !important;
    border-radius: 10px !important;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
#                      واجهة الصفحة
# -------------------------------------------------------
st.markdown('<div class="main-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)

# حقل اسم المستخدم
username = st.text_input("Enter username")

# حقل كلمة المرور + زر العين
col1, col2 = st.columns([10, 1])

with col1:
    password = st.text_input(
        "Enter password",
        type="text" if st.session_state.show_password else "password"
    )

with col2:
    eye_icon = "👁️" if not st.session_state.show_password else "👁️‍🗨️"
    if st.button(eye_icon):
        st.session_state.show_password = not st.session_state.show_password

# زر الدخول
if st.button("Login"):
    if username.strip() == "":
        st.error("Username cannot be empty")
    else:
        st.success(f"Welcome, {username}! 👋")
        st.rerun()





   



