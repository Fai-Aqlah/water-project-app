import re
import streamlit as st

def validate_username(username):
    pattern = r'^[A-Za-z][A-Za-z0-9]{4,14}$'
    return re.match(pattern, username) is not None


def login_page():

    # صندوق في المنتصف
    st.markdown("""
    <style>
        body {
            background-color: #f2f4f7;
        }

        .login-box {
            background: white;
            padding: 35px;
            width: 420px;
            margin: auto;
            margin-top: 100px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }

        .login-title {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #1d3557;
        }

        .login-input {
            font-size: 18px;
            margin-bottom: 10px;
        }

        .login-btn button {
            width: 100%;
            background: #1d3557;
            color: white !important;
            padding: 10px;
            border-radius: 8px;
            font-size: 18px;
        }

        .login-btn button:hover {
            background: #457b9d;
        }
    </style>
    """, unsafe_allow_html=True)

    # هيكل الصندوق
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.markdown("<div class='login-title'>🔐 Login</div>", unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", placeholder="Enter your password", type="password")

    login_button = st.button("Login")

    if login_button:
        if username.strip() == "" or password.strip() == "":
            st.error("❌ Username and password cannot be empty.")

        elif not validate_username(username):
            st.error("""
                ❌ Invalid username.
                It must:
                - Start with a letter
                - Contain only English letters & numbers
                - Be 5–15 characters long
                - No spaces or symbols
            """)

        elif password != "192837":  # كلمة سر بسيطة فقط للمشروع — نقدر نغيّرها
            st.error("❌ Incorrect password.")

        else:
            st.success(f"Welcome {username} 👋")
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

