import streamlit as st
import re
import time

st.set_page_config(page_title="Login", layout="centered")

st.markdown(
    """
    <div style="
        text-align:center;
        padding:25px;
        border-radius:20px;
        background: linear-gradient(180deg, #1b4d3e, #2a6f55);
        box-shadow: 0px 6px 18px rgba(0,0,0,0.25);
        margin-bottom:40px;
    ">
        <h1 style="
            font-size:48px;
            font-weight:900;
            color:white;
            margin:0;
        ">
            Smart Water System – Login Portal 💧🔐
        </h1>

        <h3 style="
            color:#87CEFA;
            font-weight:600;
            margin-top:12px;
        ">
            Please log in to continue
        </h3>
    </div>
    """,
    unsafe_allow_html=True
)


# Inputs
username = st.text_input("Username (English only)", "")
password = st.text_input("Password", type="password")

# Button
if st.button("Login"):
    
    username_errors = []
    password_errors = []

    # ---------------- USERNAME RULES ----------------
    if (
        username.strip() == "" or
        not re.match(r"^[A-Za-z0-9]+$", username)
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
        not re.search(r"[A-Za-z]", password) or
        not re.search(r"[0-9]", password) or
        " " in password or
        re.search(r"[\u0600-\u06FF]", password) or
        re.search(r"[!@#$%^&*]", password)
    ):
        password_errors.append("• Minimum 8 characters")
        password_errors.append("• Must contain letters AND numbers")
        password_errors.append("• No spaces allowed")
        password_errors.append("• No Arabic characters allowed")
        password_errors.append("• No symbols allowed (!@#$%^&*)")
        password_errors.append("• Cannot be empty")

    # ---------------- SHOW USERNAME ERRORS ----------------
    if username_errors:
        st.markdown(
            f"""
            <div class="error-box" style="background:#ffdddd;padding:15px;border-radius:10px;">
                <div class="error-title" style="color:#8b0000;font-size:20px;">
                    ❌ Invalid Username
                </div>
                <ul>
                    {''.join([f"<li>{e}</li>" for e in username_errors])}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ---------------- SHOW PASSWORD ERRORS ----------------
    if password_errors:
        st.markdown(
            f"""
            <div class="warning-box" style="background:#fff1cc;padding:15px;border-radius:10px;">
                <div class="warning-title" style="color:#b36b00;font-size:20px;">
                    ⚠️ Invalid Password
                </div>
                <ul>
                    {''.join([f"<li>{e}</li>" for e in password_errors])}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ---------------- SUCCESS ----------------
    if not username_errors and not password_errors:

        # ترحيب قبل الانتقال للصفحة
        st.markdown(
            f"""
            <h1 style="text-align:center; font-size:50px; font-weight:900; color:#1b4d3e; margin-top:100px;">
                Welcome, {username}! 💧👋
            </h1>

            <h3 style="text-align:center; color:#266f57; margin-top:10px;">
                Glad to have you here — let's start predicting your water consumption 🌿
            </h3>
            """,
            unsafe_allow_html=True,
        )

        # حفظ حالة تسجيل الدخول
        st.session_state.logged_in = True
        st.session_state.username = username

        # تأخير بسيط
        time.sleep(4)

        # الانتقال لصفحة التنبؤ
        st.switch_page("app.py")
