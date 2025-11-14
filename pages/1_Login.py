import streamlit as st
import re


# ---------------------------------------------------
#                PAGE SETTINGS
# ---------------------------------------------------
st.set_page_config(page_title="Login", layout="centered")


# ---------------------------------------------------
#                SESSION STATE
# ---------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.switch_page("app.py")


# ---------------------------------------------------
#                       CSS
# ---------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #f5f7fb;
}

/* عنوان الصفحة */
.login-title {
    text-align:center;
    font-size: 30px;
    font-weight: bold;
    color: #2b4c7e;
    margin-bottom: 25px;
}

/* مربعات الإدخال */
.stTextInput > div > div > input {
    border: 1.6px solid #c9d6e8 !important;
    border-radius: 10px !important;
    padding: 12px !important;
    font-size: 16px !important;
}

/* زر الدخول */
.stButton > button {
    width: 100%;
    background-color: #2b4c7e !important;
    color: white !important;
    padding: 10px;
    border-radius: 10px;
    font-size: 17px;
    border: none !important;
}

/* صناديق الأخطاء */
.error-box, .warning-box {
    width: 100%;
    display: block;
    padding: 18px;
    margin-top: 14px;
    border-radius: 8px;
    line-height: 1.7;
}

/* Error = أحمر */
.error-box {
    background-color: #ffe5e5;
    border-left: 6px solid #d9534f;
}

/* Warning = أصفر */
.warning-box {
    background-color: #fff4e5;
    border-left: 6px solid #f0ad4e;
}

/* العناوين */
.error-title, .warning-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 8px;
}

.error-title { color: #b52b27; }
.warning-title { color: #d48806; }

/* القائمة */
.error-list, .warning-list {
    font-size: 16px;
    padding-left: 10px;
}

.error-list li, .warning-list li {
    margin-bottom: 4px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
#        USERNAME VALIDATION FUNCTION
# ---------------------------------------------------
def is_valid_username(u):
    return re.match(r'^[A-Za-z0-9_]+$', u)


# ---------------------------------------------------
#                    UI TITLE
# ---------------------------------------------------
st.markdown("<div class='login-title'>🔐 Login Page</div>", unsafe_allow_html=True)


# ---------------------------------------------------
#                    INPUT FIELDS
# ---------------------------------------------------
username = st.text_input("Username (English only)", placeholder="Enter username...")
password = st.text_input("Password", type="password", placeholder="Enter password...")


# ---------------------------------------------------
#                LOGIN BUTTON ACTION
# ---------------------------------------------------
if st.button("Login"):

    username_errors = []
    password_errors = []


    # ---------------- USERNAME RULES ----------------
    if username.strip() == "":
        username_errors.append("The username cannot be empty")
    if not is_valid_username(username):
        username_errors.append("English letters only")
        username_errors.append("Numbers allowed")
        username_errors.append("No Arabic characters")
        username_errors.append("No spaces")
        username_errors.append("No symbols (!@#$%^&*)")


    # ---------------- PASSWORD RULES ----------------
    if password.strip() == "":
        password_errors.append("The password cannot be empty")
    if len(password) < 8:
        password_errors.append("Minimum 8 characters")
    if not re.search(r'[A-Za-z]', password):
        password_errors.append("Must contain at least one letter")
    if not re.search(r'[0-9]', password):
        password_errors.append("Must contain at least one number")
    if " " in password:
        password_errors.append("No spaces allowed")
    if re.search(r'[\u0600-\u06FF]', password):
        password_errors.append("No Arabic characters allowed")


    # ---------------- SHOW USERNAME ERRORS ----------------
    if username_errors:
        st.markdown(
            f"""
            <div class="error-box">
                <div class="error-title">❌ Invalid Username</div>
                <ul class="error-list">
                    {''.join([f"<li>{e}</li>" for e in username_errors])}
                </ul>
            </div>
            """, unsafe_allow_html=True
        )


    # ---------------- SHOW PASSWORD ERRORS ----------------
    if password_errors:
        st.markdown(
            f"""
            <div class="warning-box">
                <div class="warning-title">⚠️ Invalid Password</div>
                <ul class="warning-list">
                    {''.join([f"<li>{e}</li>" for e in password_errors])}
                </ul>
            </div>
            """, unsafe_allow_html=True
        )


    # ---------------- SUCCESS ----------------
    if not username_errors and not password_errors:
        st.success(f"🎉 Welcome, {username}!")
        st.session_state.logged_in = True
        st.switch_page("app.py")




    


    
          
