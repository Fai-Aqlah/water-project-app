import streamlit as st
import time

st.set_page_config(page_title="Login", page_icon="🔑", layout="centered")

# =========================
# CSS DESIGN
# =========================
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #e9f7ef, #ffffff);
}

.login-box {
    background: #ffffff;
    padding: 40px;
    border-radius: 18px;
    width: 430px;
    margin: auto;
    box-shadow: 0px 4px 25px rgba(0,0,0,0.12);
    animation: glow 5s ease-in-out infinite alternate;
}

@keyframes glow {
    from { box-shadow: 0px 0px 8px rgba(27,138,90,0.3); }
    to   { box-shadow: 0px 0px 18px rgba(27,138,90,0.5); }
}

.login-title {
    text-align: center;
    font-size: 38px;
    color: #1b8a5a;
    font-weight: 700;
}

.subtitle {
    text-align: center;
    color: #333;
    font-size: 18px;
    margin-bottom: 25px;
}

.stTextInput > div > div > input {
    font-size: 18px;
    padding: 12px;
    border-radius: 10px;
    border: 1.5px solid #1b8a5a;
    text-align: center;
}

button[kind="primary"] {
    width: 100%;
    padding: 12px;
    font-size: 20px !important;
    background: linear-gradient(90deg, #1b8a5a, #0277bd);
    color: white !important;
    border-radius: 10px;
    font-weight: 600;
    border: none;
    transition: 0.3s ease;
}

button[kind="primary"]:hover {
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)


# =========================
# MAIN UI
# =========================
st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="login-title">🔑 Login</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Welcome to Smart Water Consumption System</div>', unsafe_allow_html=True)

username = st.text_input("Enter username", key="username_field")
password = st.text_input("Enter password", type="password", key="password_field")

login_btn = st.button("Login")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# VALIDATION
# =========================
if login_btn:
    if username.strip() == "" or password.strip() == "":
        st.error("❌ Please fill all fields")
    elif username == "Fai" and password == "192837":
        st.success(f"Welcome, {username} 🎉")
        st.session_state.logged_in = True
        st.session_state.username = username
        time.sleep(1)
        st.switch_page("app.py")
    else:
        st.error("❌ Wrong username or password")

        
           
