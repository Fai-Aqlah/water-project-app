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

# ===============================
# Session state defaults
# ===============================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "show_requirements" not in st.session_state:
    st.session_state.show_requirements = False


# ===============================
# IF USER IS LOGGED IN → STOP PAGE
# ===============================
if st.session_state.logged_in:

    st.markdown(
        f"""
        <div style="text-align:center; margin-top:40px;">
            <h2>Welcome, {st.session_state.username} 👋💧</h2>
            <p>Great! Let's take you to your Home page 🌿</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(2)
    st.switch_page("pages/home.py")

    st.stop()   # ⛔️ مهم جداً: يوقف تنفيذ الصفحة هنا


# ===============================
# LOGIN FORM (ONLY IF NOT LOGGED IN)
# ===============================
username = st.text_input("Username (English only)")
password = st.text_input("Password", type="password")

username_errors = []
password_errors = []


# ===============================
# Login Button
# ===============================
if st.button("Login", type="secondary"):

    username_errors.clear()
    password_errors.clear()
    st.session_state.show_requirements = False

    # ---------- Username validation ----------
    if username.strip() == "":
        username_errors.append("Cannot be empty")

    if len(username) < 8:
        username_errors.append("At least 8 characters")

    if not re.match(r'^[A-Za-z0-9]+$', username):
        username_errors.append("English letters and numbers only")

    if re.search(r'[\u0600-\u06FF]', username):
        username_errors.append("No Arabic characters")

    if " " in username:
        username_errors.append("No spaces")

    if re.search(r'[!@#$%^&*]', username):
        username_errors.append("No symbols")


    # ---------- Password validation ----------
    if password.strip() == "":
        password_errors.append("Cannot be empty")

    if len(password) < 8:
        password_errors.append("At least 8 characters")

    if not re.search(r'[A-Za-z]', password):
        password_errors.append("Must include letters")

    if not re.search(r'[0-9]', password):
        password_errors.append("Must include numbers")

    if re.search(r'[\u0600-\u06FF]', password):
        password_errors.append("No Arabic characters")

    if " " in password:
        password_errors.append("No spaces")


    # ---------- Show requirements if errors ----------
    if username_errors or password_errors:
        st.session_state.show_requirements = True


    # ---------- Success ----------
    if not username_errors and not password_errors:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.show_requirements = False
        st.success("Login Successful!")


# ===============================
# REQUIREMENTS (ONLY IF ERROR)
# ===============================
if st.session_state.show_requirements:

    st.markdown("### Username Requirements")
    st.write("- At least 8 characters")
    st.write("- English letters and numbers only")
    st.write("- No Arabic characters")
    st.write("- No spaces")
    st.write("- No symbols")

    st.markdown("### Password Requirements")
    st.write("- At least 8 characters")
    st.write("- Must include letters")
    st.write("- Must include numbers")
    st.write("- No Arabic characters")
    st.write("- No spaces")






      
        







      



  
