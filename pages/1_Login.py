import streamlit as st
import re

# إعداد الصفحة بدون عنوان مكرر
st.set_page_config(page_title="Login", layout="centered")

# تنسيق CSS جميل

    st.markdown("""
<style>

    /* تنسيق مربع الإدخال */
    .stTextInput > div > div > input {
        background-color: #ffffff !important;
        border: 1.5px solid #c9d6e8 !important;
        border-radius: 8px !important;
        padding: 10px !important;
        font-size: 16px !important;
    }

    /* زر العين داخل مربع الباسورد */
    .eye-btn {
        background-color: transparent !important;
        border: none !important;
        font-size: 20px !important;
        color: #2b4c7e !important;
        cursor: pointer;
        margin-top: 32px;  /* يحاذي العين مع مربع الباسورد */
    }

    .eye-btn:hover {
        color: #1e3559 !important;
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

# =======================
#     زر العين الصحيح
# =======================

col1, col2 = st.columns([0.9, 0.1])

with col1:
    password = st.text_input(
        "Password",
        type="text" if st.session_state.show_pass else "password",
        placeholder="Enter password..."
    )

with col2:
    eye_clicked = st.button("👁️", key="eye", help="Show/Hide password")
    if eye_clicked:
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



   






   



