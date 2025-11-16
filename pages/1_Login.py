import streamlit as st
import re
def load_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_local_css("pages/style_login.css")
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

     # ---------------- USERNAME RULES ----------------
    if (
        username.strip() == "" or
        not re.match(r'^[A-Za-z0-9]+$', username) or
        " " in username or
        re.search(r'[\u0600-\u06FF]', username) or
        re.search(r'[!@#$%^&*]', username)
    ):
        username_errors.append("English letters and numbers only")
        username_errors.append("No Arabic characters")
        username_errors.append("No spaces")
        username_errors.append("No symbols (!@#$%^&*)")
        username_errors.append("Cannot be empty")

    # ---------------- PASSWORD RULES ----------------
    if (
        password.strip() == "" or
        len(password) < 8 or
        not re.search(r'[A-Za-z]', password) or
        not re.search(r'[0-9]', password) or
        " " in password or
        re.search(r'[\u0600-\u06FF]', password)
    ):
        password_errors.append("Password must be at least 8 characters")
        password_errors.append("Must include letters and numbers")
        password_errors.append("No spaces allowed")
        password_errors.append("No Arabic characters")
        password_errors.append("Cannot be empty")

    if password_errors:
        st.warning("Please fix the following password rules:\n\n" + "\n".join([f"• {e}" for e in password_errors]))

    # إذا ما فيه ولا خطأ
    if not username_errors and not password_errors:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Login successful! Redirecting...")
        st.markdown("""
            <p style="font-size:20px; font-weight:600; color:#1b4d3e; margin-top:20px;">
                Glad to have you here — let’s start predicting your water consumption 🌿💧
            </p>
        """, unsafe_allow_html=True)

       
        

        

        st.switch_page("app.py")  # عدّلي الاسم حسب صفحة التنبؤ

      
   
      
