import streamlit as st
import time

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# ======================================================
#                LOGIN PAGE UI (HTML)
# ======================================================

st.markdown("""
<div class="login-wrapper">
    <div class="login-box">
        <div class="login-title">🔐 Login</div>
        <div class="login-subtext">Welcome to Smart Water Consumption System</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================================================
#                INPUT FIELDS
# ======================================================

st.markdown("<div class='login-input'>", unsafe_allow_html=True)
username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")
st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
#                VALIDATION
# ======================================================

if st.button("Login"):

    # شرط 1 — فارغ
    if username.strip() == "":
        st.error("❌ Username cannot be empty.")

    # شرط 2 — يحتوي مسافات
    elif " " in username:
        st.error("❌ Username cannot contain spaces.")

    # شرط 3 — أقل من 3 حروف
    elif len(username) < 3:
        st.error("❌ Username must be at least 3 characters.")

    # شرط 4 — منع العربية
    elif any('\u0600' <= c <= '\u06FF' for c in username):
        st.error("❌ Arabic is not allowed in the username.")

    # التحقق النهائي
    else:
        if username == "Fai" and password == "1929837":
            st.session_state.logged_in = True
            st.session_state.username = username

            st.success(f"Welcome, {username}! 🎉")
            time.sleep(1)
            st.switch_page("app.py")
        else:
            st.error("❌ Wrong username or password")


            
