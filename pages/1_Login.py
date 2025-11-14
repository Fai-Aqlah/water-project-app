import streamlit as st
import re

# إعداد الصفحة
st.set_page_config(page_title="Login", layout="centered")

# -----------------------------------
#        SESSION STATE
# -----------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# لو المستخدم مسجل دخول → حوله مباشرة لصفحة التنبؤ
if st.session_state.logged_in:
    st.switch_page("app.py")


# -----------------------------------
#             CSS
# -----------------------------------
st.markdown("""
<style>

    body {
        background-color: #f6f8fc;
    }

    .login-title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #2b4c7e;
        margin-bottom: 25px;
    }

    .stTextInput > div > div > input {
        border: 1.6px solid #c9d6e8 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-size: 16px !important;
    }

    /* زر الدخول */
    .stButton > button {
        width: 100%;
        background-color: #2b4c7e !important;
        color: white !important;
        padding: 10px;
        border-radius: 10px;
        font-size: 17px;
    }

    /* مربع كلمة المرور + زر العين */
    .password-box {
        position: relative;
    }

    .eye-icon {
        position: absolute;
        right: 15px;
        top: 43px;
        font-size: 20px;
        cursor: pointer;
        color: #2b4c7e;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------------
#       FUNCTIONS
# -----------------------------------
def is_valid_username(u):
    return re.match(r'^[A-Za-z0-9_]+$', u)


# -----------------------------------
#       LOGIN UI
# -----------------------------------
st.markdown("<div class='login-title'>🔐 Login Page</div>", unsafe_allow_html=True)

username = st.text_input(
    "Username (English only)",
    placeholder="Enter username..."
)


# -------- Password + Eye Button --------
if "show_pass" not in st.session_state:
    st.session_state.show_pass = False

pass_col1, pass_col2 = st.columns([0.9, 0.1])

with pass_col1:
    password = st.text_input(
        "Password",
        type="password" if not st.session_state.show_pass else "text",
        placeholder="Enter password..."
    )

with pass_col2:
    eye_icon = "👁️" if not st.session_state.show_pass else "👁️‍🗨️"
    if st.button(eye_icon, key="toggle_eye"):
        st.session_state.show_pass = not st.session_state.show_pass
        st.experimental_rerun()

# -----------------------------------
#       LOGIN BUTTON ACTION
# -----------------------------------
if st.button("Login", key="login_btn"):
    if username.strip() == "":
        st.error("❌ Please enter a username.")
    elif not is_valid_username(username):
        st.error("❌ Username must be English letters or numbers only.")
    elif password.strip() == "":
        st.error("❌ Please enter your password.")
    else:
        st.success(f"🎉 Welcome, {username}!")
        st.session_state.logged_in = True
        
        # التحويل الصحيح لصفحة التنبؤ (app.py)
        st.switch_page("app.py")


        
   



