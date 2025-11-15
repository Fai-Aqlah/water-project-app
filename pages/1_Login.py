import streamlit as st
import re

# ---------------------------------------------------
#                PAGE SETTINGS
# ---------------------------------------------------
st.set_page_config(page_title="Login", layout="centered")

# ---------------------------------------------------
#                CSS
# ---------------------------------------------------
st.markdown("""
<style>

body { background-color: #f5f7fb; }

.login-title {
    text-align:center;
    font-size: 30px;
    font-weight: bold;
    color: #2b4c7e;
    margin-bottom: 25px;
}

/* input boxes */
.stTextInput > div > div > input {
    border: 1.6px solid #c9d6e8 !important;
    border-radius: 10px !important;
    padding: 12px !important;
    font-size: 16px !important;
}

/* Login button */
.stButton > button {
    width: 100%;
    background-color: #2b4c7e !important;
    color: white !important;
    padding: 10px;
    border-radius: 10px;
    font-size: 17px;
    border: none !important;
}

/* Error & Warning boxes */
.error-box, .warning-box {
    width: 95% !important;
    display: block;
    padding: 18px;
    margin-top: 18px;
    margin-left: auto;
    margin-right: auto;
    border-radius: 8px;
    line-height: 1.7;
    white-space: normal !important;
    word-break: keep-all !important;
    overflow-wrap: normal !important;
}

.error-box {
    background-color: #ffe5e5;
    border-left: 6px solid #d9534f;
}

.warning-box {
    background-color: #fff4e5;
    border-left: 6px solid #f0ad4e;
}

.error-title, .warning-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 8px;
}

.error-title { color: #b52b27; }
.warning-title { color: #d48806; }

.error-list li, .warning-list li {
    font-size: 16px;
    margin-bottom: 4px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
#                SESSION STATE
# ---------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Already logged in → go to app
if st.session_state.logged_in:
    st.switch_page("app.py")


# ---------------------------------------------------
#                PAGE TITLE
# ---------------------------------------------------
st.markdown("<div class='login-title'>🔐 Login Page</div>", unsafe_allow_html=True)


# ---------------------------------------------------
#                INPUT FIELDS
# ---------------------------------------------------
username = st.text_input("Username (English only)", placeholder="Enter username...")
password = st.text_input("Password", type="password", placeholder="Enter password...")


# ---------------------------------------------------
#        LOGIN BUTTON ACTION
# ---------------------------------------------------
if st.button("Login"):

    username_errors = []
    password_errors = []

    # ---------------- USERNAME RULES ----------------
    if (
        username.strip() == "" or
        not re.match(r'^[A-Za-z0-9]+$', username)
    ):
        username_errors.append("• English letters and numbers only")
        username_errors.append("• No Arabic characters")
        username_errors.append("• No spaces")
        username_errors.append("• No symbols (!@#$%^&*)")
        username_errors.append("• Cannot be empty")


    # ---------------- PASSWORD RULES ----------------
    if (
        password.strip() == "" or
        len(password) < 8 or
        not re.search(r'[A-Za-z]', password) or
        not re.search(r'[0-9]', password) or
        " " in password or
        re.search(r'[\u0600-\u06FF]', password)
    ):
        password_errors.append("• Minimum 8 characters")
        password_errors.append("• Must contain letters and numbers")
        password_errors.append("• No spaces")
        password_errors.append("• No Arabic characters")

    # ---------------- SHOW ERRORS (لا تلمسينها) ----------------
    if username_errors:
        st.markdown(
            f"""
            <div class="error-box">
                <div class="error-title">❌ Invalid Username</div>
                <ul class="error-list">
                    {''.join([f"<li>{e}</li>" for e in username_errors])}
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
                    {''.join([f"<li>{e}</li>" for e in password_errors])}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    if not username_errors and not password_errors:
        st.success(f"Welcome {username}!")
        st.session_state.logged_in = True
        st.switch_page("app.py")
