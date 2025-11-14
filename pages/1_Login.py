import streamlit as st
import re

st.set_page_config(page_title="Login", layout="centered")

# ----------------------------------------------------
#            FUNCTIONS
# ----------------------------------------------------
def is_valid_username(username):
    """اسم المستخدم: إنجليزي فقط + بدون رموز"""
    return re.match(r'^[A-Za-z0-9_]+$', username)


# ----------------------------------------------------
#            LOGIN UI
# ----------------------------------------------------

st.markdown("<h2 style='text-align:center;'>🔐 Login Page</h2>", unsafe_allow_html=True)

# Username
username = st.text_input(
    "Username (English only)",
    placeholder="Enter username..."
)

# Password + Eye Icon
password_container = st.empty()

if "show_password" not in st.session_state:
    st.session_state.show_password = False

with password_container:
    password = st.text_input(
        "Password",
        type="text" if st.session_state.show_password else "password",
        placeholder="Enter password...",
        help="Click the eye to show/hide the password"
    )

# Eye button inside the same row
eye_col1, eye_col2 = st.columns([0.9, 0.1])
with eye_col2:
    if st.button("👁️"):
        st.session_state.show_password = not st.session_state.show_password
        st.experimental_rerun()

# ----------------------------------------------------
#            LOGIN BUTTON
# ----------------------------------------------------
if st.button("Login"):
    if username.strip() == "":
        st.error("❌ Please enter a username.")
    elif not is_valid_username(username):
        st.error("❌ Username must be English letters or numbers only.")
    elif password.strip() == "":
        st.error("❌ Please enter a password.")
    else:
        st.success("✅ Login successful!")

   






   



