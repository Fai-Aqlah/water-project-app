import streamlit as st
import re
import time

# --------------------- STYLE ---------------------
st.markdown("""
<style>

.error-box {
    background: #ffdddd;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
    border-left: 6px solid #b00000;
}

.error-title {
    color: #b00000;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 8px;
}

.error-list li {
    color: #600000;
    font-size: 15px;
    margin-left: 20px;
}

.warning-box {
    background: #fff4cc;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
    border-left: 6px solid #b88600;
}

.warning-title {
    color: #b88600;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 8px;
}

.warning-list li {
    color: #7a5a00;
    font-size: 15px;
    margin-left: 20px;
}

/* ====== شكل مربعات الإدخال Username / Password ====== */
div[data-testid="stTextInput"] input {
    font-size: 30px !important;        /* حجم الخط داخل المربع */
    padding: 14px 18px !important;     /* مساحة داخلية */
    height: 52px !important;           /* ارتفاع المربع */
    border-radius: 12px !important;    /* تدوير الحواف */
    border: 2px solid #1b4d3e !important;  /* لون الحدود */
    background-color: #f8fff8 !important;  /* خلفية خفيفة */
    width: 100% !important;            /* يخليه عريض على قد العمود */
    box-shadow: 0 2px 6px rgba(0,0,0,0.08) !important;
}

/* ====== تكبير خط الليبل فوق المربع ====== */
div[data-testid="stTextInput"] label {
    font-size: 30px !important;
    font-weight: 800 !important;
    color: #1b4d3e !important;
    font-family: Arial, sans-serif !important;
}




</style>
""", unsafe_allow_html=True)
# -------------------------------------------------

    




st.set_page_config(page_title="Login", layout="centered")

# ---------------- HEADER ----------------
header_html = """
<div style="width:75%; margin:auto; padding:25px; border-radius:20px; background:#ffffff; box-shadow:0px 6px 18px rgba(0,0,0,0.15); text-align:center;">
    <h1 style="font-size:48px; font-weight:900; color:#1b4d3e; margin:0;">
        Smart Water System — Login Portal 🔐💧
    </h1>
    <p style="font-size:18px; font-weight:600; margin-top:12px; color:#87CEFA;">
        Please log in to continue
    </p>
</div>
"""


st.markdown(header_html, unsafe_allow_html=True)

# ---------------- INPUTS ----------------
username = st.text_input("Username (English only)", "")
password = st.text_input("Password", type="password")

# ---------------- BUTTON ----------------
if st.button("Login"):

    username_errors = []
    password_errors = []

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
        re.search(r'[\u0600-\u06FF]', password) or
        re.search(r'[!@#$%^&*]', password)
    ):
        password_errors.append("Minimum 8 characters")
        password_errors.append("Must contain letters and numbers")
        password_errors.append("No spaces")
        password_errors.append("No Arabic characters")
        password_errors.append("No symbols allowed (!@#$%^&*)")
        password_errors.append("Cannot be empty")

    # ---------------- SHOW ERRORS (لا تلمسينها) ----------------
    if username_errors:
        st.markdown(
            f"""
            <div class="error-box">
                <div class="error-title">❌ Invalid Username</div>
                <ul class="error-list">
                    {''.join(f"<li>{e}</li>" for e in username_errors)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    if password_errors:
        st.markdown(
            f"""
            <div class="warning-box">
                <div class="warning-title">⚠️ Invalid Password</div>
                <ul class="warning-list">
                    {''.join(f"<li>{e}</li>" for e in password_errors)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------------- SUCCESS: username & password valid ----------------
    if not username_errors and not password_errors:
        st.success("Login successful! Redirecting...")
        st.session_state.logged_in = True
        st.session_state.username = username
        time.sleep(4)
        st.switch_page("app.py")

   
       
