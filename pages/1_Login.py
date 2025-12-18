import streamlit as st
import re
import time    
def load_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_local_css("pages/style_login.css")
st.set_page_config(page_title="Login", layout="centered")



st.markdown("""
<div style="
    text-align:center;
    margin-top:20px;
    margin-bottom:40px;
">
    <h1 style="color:#1b4d3e; font-size:48px; font-weight:900;">
        Smart Water System 💧 – Login Portal 
    </h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    header {
        visibility: hidden;
    }

    .block-container {
        padding-top: 0.3rem !important;
    }
</style>
""", unsafe_allow_html=True)

# inputs
username = st.text_input("Username (English only)")
password = st.text_input("Password", type="password")

# قوائم الأخطاء
username_errors = []
password_errors = []

# زر واحد فقط
if st.button("Login", type="secondary"):

    # إعادة تهيئة الأخطاء عند كل ضغطة
    username_errors.clear()
    password_errors.clear()

    # ---------- Username validation ----------
    if username.strip() == "":
        username_errors.append("Cannot be empty")

    if len(username) < 8:
        username_errors.append("Username must be at least 8 characters")

    if not re.match(r'^[A-Za-z0-9]+$', username):
        username_errors.append("English letters and numbers only")

    if re.search(r'[\u0600-\u06FF]', username):
        username_errors.append("No Arabic characters")

    if " " in username:
        username_errors.append("No spaces allowed")

    if re.search(r'[!@#$%^&*]', username):
        username_errors.append("No symbols (!@#$%^&*)")

    # ---------- Password validation ----------
    if password.strip() == "":
        password_errors.append("Cannot be empty")

    if len(password) < 8:
        password_errors.append("Password must be at least 8 characters")

    if not re.search(r'[A-Za-z]', password):
        password_errors.append("Must include letters")

    if not re.search(r'[0-9]', password):
        password_errors.append("Must include numbers")

    if re.search(r'[\u0600-\u06FF]', password):
        password_errors.append("No Arabic characters")

    if " " in password:
        password_errors.append("No spaces allowed")

    # ---------- Show errors ----------
    if username_errors:
        st.error("❌ Username Errors")
        for e in username_errors:
            st.write(f"- {e}")

    if password_errors:
        st.warning("⚠️ Password Errors")
        for e in password_errors:
            st.write(f"- {e}")

    # ---------- FINAL VALIDATION ----------
    if not username_errors and not password_errors:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Login Successful!")





      
# بعد نجاح الدخول فقط
if st.session_state.get("logged_in"):
    st.markdown(
        f"""
        <div style="text-align:center; margin-top:20px;">
            <h2 style="color:#1b4d3e; font-size:32px; font-weight:900;">
                Welcome, {st.session_state.username}! 👋💧
            </h2>
            <p style="color:#008B8B; font-size:30px; font-weight:800;">
                ⭐ Great! Let's take you to your Home page 🌿💧
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(4)
    st.switch_page("pages/home.py")

     



  
