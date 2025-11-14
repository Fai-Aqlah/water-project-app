import streamlit as st
import time

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# ===================== CUSTOM CSS =====================
st.markdown("""
<style>

body {
    font-family: 'Poppins', sans-serif !important;
}

/* Main title (Login) */
.login-title {
    font-size: 42px;
    font-weight: 700;
    color: #0277bd;  /* Blue */
    text-align: center;
    margin-bottom: 10px;
}

/* Welcome message */
.welcome-text {
    font-size: 26px;
    font-weight: 600;
    color: #1b8a5a;  /* Green */
    text-align: center;
    margin-top: 15px;
}

/* Input fields */
input {
    font-size: 20px !important;
    padding: 12px !important;
    border-radius: 10px !important;
    border: 2px solid #0277bd !important;
    text-align: left !important;
}

/* Login button */
.stButton>button {
    background: linear-gradient(90deg, #1b8a5a, #0277bd);
    color: white !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    padding: 12px 40px !important;
    border-radius: 10px !important;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 10px rgba(0,0,0,0.15);
}

/* Eye toggle fix */
.password-toggle {
    font-size: 18px;
    cursor: pointer;
}

</style>
""", unsafe_allow_html=True)

# ===================== PAGE UI =====================

st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown("### Welcome to Smart Water Consumption System")

st.write("")  # space

# Password visibility toggle
if "show_password" not in st.session_state:
    st.session_state.show_password = False

col1, col2 = st.columns([10,1])

username = st.text_input("Enter username", key="username_input")

# Password + Eye Button
with col1:
    password = st.text_input("Enter password", type="password" if not st.session_state.show_password else "default",
                             key="password_input")

with col2:
    toggle_btn = st.button("👁️", key="toggle_password")
    if toggle_btn:
        st.session_state.show_password = not st.session_state.show_password

# ===================== VALIDATION =====================
def show_all_username_rules():
    st.error("""
**Username Requirements:**
- Must NOT contain Arabic letters  
- Must NOT contain spaces  
- Must be at least 3 characters  
- Must contain only letters or numbers  
""")

if st.button("Login"):
    
    # RULE 1 — Empty
    if username.strip() == "":
        st.error("❌ Username cannot be empty.")
        show_all_username_rules()

    # RULE 2 — Contains Arabic
    elif any('\u0600' <= c <= '\u06FF' for c in username):
        st.error("❌ Arabic letters are NOT allowed in the username.")
        show_all_username_rules()

    # RULE 3 — Space inside username
    elif " " in username:
        st.error("❌ Username cannot contain spaces.")
        show_all_username_rules()
    
    # RULE 4 — Too short
    elif len(username) < 3:
        st.error("❌ Username must be at least 3 characters long.")
        show_all_username_rules()

    else:
        # ACCEPT ANY username + ANY password
        st.success(f"Welcome, **{username}** 👋")
        st.markdown(f'<div class="welcome-text">Welcome, {username}! 👋</div>', unsafe_allow_html=True)
        time.sleep(1)
        st.switch_page("app.py")


