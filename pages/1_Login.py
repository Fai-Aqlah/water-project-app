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

# ================== INPUTS ==================
username = st.text_input("Username (English only)")
password = st.text_input("Password", type="password")

# ================== SESSION STATE ==================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ================== SHOW REQUIREMENTS (قبل الدخول فقط) ==================
if not st.session_state.logged_in:

    st.subheader("Username Requirements")
    st.write("- At least 8 characters")
    st.write("- English letters and numbers only")
    st.write("- No Arabic characters")
    st.write("- No spaces")
    st.write("- No symbols")

    st.subheader("Password Requirements")
    st.write("- At least 8 characters")
    st.write("- Must include letters")
    st.write("- Must include numbers")
    st.write("- No Arabic characters")
    st.write("- No spaces")

# ================== ERRORS LIST ==================
username_errors = []
password_errors = []

# ================== LOGIN BUTTON ==================
if st.button("Login", type="secondary"):

    username_errors.clear()
    password_errors.clear()

    # ---------- Username validation ----------
    if username.strip() == "":
        username_errors.append("empty")

    if len(username) < 8:
        username_errors.append("length")

    if not re.match(r'^[A-Za-z0-9]+$', username):
        username_errors.append("format")

    if re.search(r'[\u0600-\u06FF]', username):
        username_errors.append("arabic")

    if " " in username:
        username_errors.append("space")

    if re.search(r'[!@#$%^&*]', username):
        username_errors.append("symbols")

    # ---------- Password validation ----------
    if password.strip() == "":
        password_errors.append("empty")

    if len(password) < 8:
        password_errors.append("length")

    if not re.search(r'[A-Za-z]', password):
        password_errors.append("letters")

    if not re.search(r'[0-9]', password):
        password_errors.append("numbers")

    if re.search(r'[\u0600-\u06FF]', password):
        password_errors.append("arabic")

    if " " in password:
        password_errors.append("space")

    # ---------- FINAL VALIDATION ----------
    if not username_errors and not password_errors:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Login Successful")

# ================== AFTER LOGIN ==================
if st.session_state.logged_in:
    st.markdown(
        f"""
        <div style="text-align:center; margin-top:30px;">
            <h2>Welcome, {st.session_state.username}</h2>
            <p>Redirecting to Home page...</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(3)
    st.switch_page("pages/home.py")



      
        







      
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

     



  
