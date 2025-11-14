import streamlit as st
import re


st.set_page_config(page_title="Login", page_icon="🔐")

# عنوان تسجيل الدخول
st.markdown("<h2 style='text-align:center;'>🔐 Login Page</h2>", unsafe_allow_html=True)

# مسافة
st.write("")

# صناديق الإدخال

username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")

def valid_username(name):
    pattern = r'^[A-Za-z][A-Za-z0-9]{3,11}$'
    return re.match(pattern, name)

if st.button("Login"):
    if not valid_username(username):
        st.error("""
        ❌ Invalid username!
        Username must:
        • Start with a letter  
        • Be 4–12 characters  
        • Contain only letters and numbers  
        • No spaces or symbols  
        """)
        
    elif username == "Fai" and password == "192837":
        st.session_state.logged_in = True
        st.success("Login successful 🎉")
        st.switch_page("app.py")
        
    else:
        st.error("❌ Wrong username or password")
