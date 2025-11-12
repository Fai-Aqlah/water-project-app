import re
import streamlit as st

def validate_username(username):
    # Regex rules
    pattern = r'^[A-Za-z][A-Za-z0-9]{4,14}$'
    return re.match(pattern, username) is not None


def login_page():
    st.title("🔐 Login Page")

    username = st.text_input("Username", placeholder="Enter your username")

    if st.button("Login"):
        if username.strip() == "":
            st.error("❌ Username cannot be empty.")
        elif not validate_username(username):
            st.error(
                "❌ Invalid username.\n\n"
                "It must:\n"
                "- Start with a letter\n"
                "- Contain only English letters and numbers\n"
                "- Be 5 to 15 characters long\n"
                "- No spaces or symbols"
            )
        else:
            st.success(f"Welcome, {username} 👋")
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
