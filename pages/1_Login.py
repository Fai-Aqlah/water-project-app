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

username = st.text_input("Username (English only)", key="username_input")
password = st.text_input("Password", type="password", key="password_input")

if st.button("Login", type="secondary"):

    username_rules = [
        "Cannot be empty",
        "At least 8 characters",
        "English letters and numbers only",
        "No Arabic characters",
        "No spaces allowed",
        "No symbols (!@#$%^&*)",
    ]

    password_rules = [
        "Cannot be empty",
        "At least 8 characters",
        "Must include letters",
        "Must include numbers",
        "No Arabic characters",
        "No spaces allowed",
    ]

    # التحقق الفعلي (بدون عرض)
    username_valid = (
        username.strip() != "" and
        len(username) >= 8 and
        re.match(r'^[A-Za-z0-9]+$', username) and
        not re.search(r'[\u0600-\u06FF]', username) and
        " " not in username and
        not re.search(r'[!@#$%^&*]', username)
    )

    password_valid = (
        password.strip() != "" and
        len(password) >= 8 and
        re.search(r'[A-Za-z]', password) and
        re.search(r'[0-9]', password) and
        not re.search(r'[\u0600-\u06FF]', password) and
        " " not in password
    )

    if not username_valid:
        st.error("Username Requirements")
        for r in username_rules:
            st.write(f"- {r}")

    if not password_valid:
        st.warning("Password Requirements")
        for r in password_rules:
            st.write(f"- {r}")

    if username_valid and password_valid:
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

     



  
