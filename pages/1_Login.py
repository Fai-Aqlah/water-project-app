import streamlit as st
import re

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

def validate_username(username):
    pattern = r'^[A-Za-z][A-Za-z0-9]{4,14}$'
    return re.match(pattern, username) is not None

st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #e8f0fe, #d2e3fc);
    font-family: 'Arial';
}

.login-box {
    background: white;
    padding: 40px;
    width: 420px;
    margin: auto;
    margin-top: 80px;
    border-radius: 18px;
    box-shadow: 0px 10px 35px rgba(0, 0, 0, 0.15);
    animation: slideDown 0.7s ease;
}

.login-title {
    text-align: center;
    font-size: 26px;
    font-weight: 700;
    color: #1a73e8;
    margin-bottom: 15px;
}

.icon {
    text-align: center;
    font-size: 45px;
    margin-bottom: 10px;
}

.stButton > button {
    width: 100%;
    background-color: #1a73e8 !important;
    color: white !important;
    border-radius: 10px !important;
    height: 45px;
    font-size: 17px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #155fc1 !important;
    transition: 0.2s;
}

@keyframes slideDown {
    from {opacity: 0; transform: translateY(-25px);}
    to   {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)


st.markdown("<div class='login-box'>", unsafe_allow_html=True)

st.markdown("<div class='icon'>🔐</div>", unsafe_allow_html=True)
st.markdown("<div class='login-title'>Welcome Back</div>", unsafe_allow_html=True)

st.write("Please login to continue 👇")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username.strip() == "" or password.strip() == "":
        st.error("❌ Username and password are required.")

    elif not validate_username(username):
        st.error("""
❌ Invalid username.
It must:
- Start with a letter  
- Include only English letters & numbers  
- Be 5–15 characters  
""")

    elif password != "192837":
        st.error("❌ Incorrect password.")

    else:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success(f"Welcome {username} 🎉")
        st.switch_page("app.py")

st.markdown("</div>", unsafe_allow_html=True)
