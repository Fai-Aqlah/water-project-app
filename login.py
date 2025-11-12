import re
import streamlit as st


def validate_username(username):
    pattern = r'^[A-Za-z][A-Za-z0-9]{4,14}$'
    return re.match(pattern, username) is not None


def login_page():
    # CSS style for the login page
    st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom right, #eef2f3, #d9e2ec);
    }

    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .login-box {
        background: #ffffff;
        padding: 35px;
        width: 380px;
        border-radius: 18px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        text-align: center;
    }

    .login-title {
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #1a2e4f;
    }

    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }

    .stButton button {
        background-color: #1a73e8;
        color: white !important;
        width: 100%;
        padding: 10px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: 600;
        border: none;
    }

    .stButton button:hover {
        background-color: #1558b0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Login box layout
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.markdown("<div class='login-title'>🔐 Login</div>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color:#4a4a4a; font-size:16px; margin-bottom:20px;'>"
        "Welcome to the Smart Water Management System<br>"
        "Please login to continue."
        "</p>",
        unsafe_allow_html=True
    )

    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", placeholder="Enter your password", type="password")

    if st.button("Login"):
        if username.strip() == "" or password.strip() == "":
            st.error("❌ Username and password cannot be empty.")
        elif not validate_username(username):
            st.error(
                "❌ Invalid username.\n\n"
                "It must:\n"
                "- Start with a letter\n"
                "- Contain only English letters & numbers\n"
                "- Be 5–15 characters long\n"
                "- Have no spaces or symbols"
            )
        elif password != "192837":  # غيّريها إذا حبيتي
            st.error("❌ Incorrect password.")
        else:
            st.success(f"Welcome {username} 👋")
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()

    st.markdown("</div></div>", unsafe_allow_html=True)

    
