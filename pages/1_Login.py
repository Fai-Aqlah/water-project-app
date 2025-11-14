import streamlit as st
import time

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# ===================== CUSTOM CSS =====================
st.markdown("""
<style>

body {
    font-family: 'Poppins', sans-serif !important;
}

/* Login title */
.main-title {
    font-size: 45px;
    font-weight: 700;
    color: #0277bd;
    text-align: center;
    margin-bottom: 5px;
}

/* Small subtitle */
.sub-text {
    text-align: center;
    color: #1b8a5a;
    font-size: 20px;
    margin-bottom: 20px;
}

/* Input fields */
input {
    font-size: 22px !important;
    padding: 12px !important;
    border-radius: 12px !important;
    border: 2px solid #0277bd !important;
    text-align: left !important;
}

/* Login button */
.stButton>button {
    background: linear-gradient(90deg, #1b8a5a, #0277bd);
    color: white !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    padding: 10px 40px !important;
    border-radius: 12px !important;
    border: none;
    transition: 0.2s;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* Eye inside password field */
.password-container {
    position: relative;
}

.password-container input {
    padding-right: 40px !important;
}

.eye-button {
    position: absolute;
    right: 10px;
    top: 30%;
    transform: translateY(-30%);
    font-size: 20px;
    cursor: pointer;
    color: #0277bd;
}

</style>
""", unsafe_allow_html=True)


# ============ PASSWORD TOGGLE LOGIC ============
if "show_pass" not in st.session_state:
    st.session_state.show_pass = False


# ============ PAGE CONTENT ============
st.markdown('<div class="main-title">🔐 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)

st.write("")

# Username
username = st.text_input("Enter username")

# Password with eye icon
st.markdown('<div class="password-container">', unsafe_allow_html=True)

password = st.text_input(
    "Enter password",
    type="default" if st.session_state.show_pass else "password",
)

eye_col = st.columns([0.8, 0.2])[1]

with eye_col:
    if st.button("👁️", key="eye_btn"):
        st.session_state.show_pass = not st.session_state.show_pass

st.markdown('</div>', unsafe_allow_html=True)


# ============ VALIDATION ============
def show_rules():
    st.error("""
**Username Requirements:**
• Must NOT contain Arabic letters  
• Must NOT contain spaces  
• Must be at least 3 characters  
• Must contain only letters or numbers  
""")


if st.button("Login"):

    # RULES
    if username.strip() == "":
        st.error("❌ Username cannot be empty.")
        show_rules()

    elif " " in username:
        st.error("❌ Username cannot contain spaces.")
        show_rules()

    elif len(username) < 3:
        st.error("❌ Username must be at least 3 characters.")
        show_rules()

    elif any('\u0600' <= c <= '\u06FF' for c in username):
        st.error("❌ Arabic letters are NOT allowed.")
        show_rules()

    else:
        # SUCCESS
        st.success(f"Welcome, {username}! 👋")
        time.sleep(1)

        st.switch_page("app.py")




