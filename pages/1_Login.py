import streamlit as st
import re

st.set_page_config(page_title="Login", layout="centered")

# ------------------ HEADER ------------------
st.markdown("""
<div style="
    text-align:center;
    margin-top:20px;
    margin-bottom:40px;
">
    <h1 style="color:#1b4d3e; font-size:48px; font-weight:900;">
        Welcome 👋💧
    </h1>
    <p style="color:#1b4d3e; font-size:22px; font-weight:600;">
        Glad to have you here — let's start predicting your water consumption 🌿
    </p>
</div>
""", unsafe_allow_html=True)


# ------------------ INPUTS ------------------
username = st.text_input("Username (English only)", key="username_input")
password = st.text_input("Password", type="password", key="password_input")

# القوائم اللي نجمع فيها الشروط
username_errors = []
password_errors = []

# ------------------ BUTTON ------------------
if st.button("Login"):

    # =======================
    # USERNAME RULES (مثل القديم بالضبط)
    # =======================
    if username.strip() == "":
        username_errors.append("Username cannot be empty.")
    if not re.match(r'^[A-Za-z0-9]+$', username):
        username_errors.append("Username must contain only English letters and numbers.")
    if " " in username:
        username_errors.append("Spaces are not allowed in username.")
    if re.search(r'[\u0600-\u06FF]', username):
        username_errors.append("Arabic letters are not allowed in username.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', username):
        username_errors.append("Special characters are not allowed.")

    # =======================
    # PASSWORD RULES (نفس الشروط القديمة)
    # =======================
    if password.strip() == "":
        password_errors.append("Password cannot be empty.")
    if len(password) < 6:
        password_errors.append("Password must be at least 6 characters.")
    if " " in password:
        password_errors.append("Spaces are not allowed in password.")

    # هنا الفكرة المهمة:
    # حتى لو كان فيه شرط واحد غلط، نظهر كل الشروط
    if username_errors:
        st.error("Please fix the following username rules:\n\n" + "\n".join([f"• {e}" for e in username_errors]))

    if password_errors:
        st.warning("Please fix the following password rules:\n\n" + "\n".join([f"• {e}" for e in password_errors]))

    # إذا ما فيه ولا خطأ
    if not username_errors and not password_errors:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Login successful! Redirecting...")
        st.switch_page("app.py")  # عدّلي الاسم حسب صفحة التنبؤ

      
   
      
