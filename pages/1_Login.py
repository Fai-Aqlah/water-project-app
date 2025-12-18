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
        ("Cannot be empty", username.strip() != ""),
        ("At least 8 characters", len(username) >= 8),
        ("English letters and numbers only", bool(re.match(r'^[A-Za-z0-9]+$', username))),
        ("No Arabic characters", not re.search(r'[\u0600-\u06FF]', username)),
        ("No spaces allowed", " " not in username),
        ("No symbols (!@#$%^&*)", not re.search(r'[!@#$%^&*]', username)),
    ]

    password_rules = [
        ("Cannot be empty", password.strip() != ""),
        ("At least 8 characters", len(password) >= 8),
        ("Must include letters", bool(re.search(r'[A-Za-z]', password))),
        ("Must include numbers", bool(re.search(r'[0-9]', password))),
        ("No Arabic characters", not re.search(r'[\u0600-\u06FF]', password)),
        ("No spaces allowed", " " not in password),
    ]

    username_valid = all(rule[1] for rule in username_rules)
    password_valid = all(rule[1] for rule in password_rules)

    if not username_valid:
        st.error("❌ Username Rules")
        for rule, passed in username_rules:
            st.write(f"{'✅' if passed else '❌'} {rule}")

    if not password_valid:
        st.warning("⚠️ Password Rules")
        for rule, passed in password_rules:
            st.write(f"{'✅' if passed else '❌'} {rule}")

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

     



  
