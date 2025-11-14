import streamlit as st
import re

# إعداد الصفحة بدون عنوان مكرر
st.set_page_config(page_title="Login", layout="centered")

# تنسيق CSS جميل
st.markdown("""
<style>

    /* خلفية خفيفة */
    .main {
        background-color: #f8faff;
    }

    /* عنوان الصفحة */
    .title-login {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #2b4c7e;
        margin-bottom: 20px;
    }

    /* مربعات الإدخال */
    .stTextInput > div > div > input {
        background-color: #ffffff !important;
        border: 1.5px solid #c9d6e8 !important;
        border-radius: 8px !important;
        padding: 10px !important;
        font-size: 16px !important;
    }

    /* زر Login */
    .stButton > button {
        background-color: #2b4c7e !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 22px !important;
        font-size: 16px !important;
        width: 100%;
        border: none;
    }

    .stButton > button:hover {
        background-color: #1e3559 !important;
        color: #fff !important;
    }

</style>
""", unsafe_allow_html=True)


# ----------------------------
#    دوال التحقق
# ----------------------------
def is_valid_username(u):
    return re.match(r'^[A-Za-z0-9_]+$', u)


# ----------------------------
#     واجهة تسجيل الدخول
# ----------------------------

st.markdown("<div class='title-login'>🔐 Login Page</div>", unsafe_allow_html=True)

username = st.text_input("Username (English only)", placeholder="Enter username...")

# =======================
#     زر العين الصحيح
# =======================
if "show_pass" not in st.session_state:
    st.session_state.show_pass = False

col1, col2 = st.columns([0.85, 0.15])
with col1:
    password = st.text_input(
        "Password",
        type="text" if st.session_state.show_pass else "password",
        placeholder="Enter password..."
    )

with col2:
    if st.button("👁️"):
        st.session_state.show_pass = not st.session_state.show_pass
        st.experimental_rerun()


# ----------------------------
#         زر تسجيل الدخول
# ----------------------------
if st.button("Login"):
    if username.strip() == "":
        st.error("❌ Please enter a username.")
    elif not is_valid_username(username):
        st.error("❌ Username must contain English letters or numbers only.")
    elif password.strip() == "":
        st.error("❌ Please enter your password.")
    else:
        st.success(f"🎉 Welcome, **{username}**! Login successful.")



   






   



