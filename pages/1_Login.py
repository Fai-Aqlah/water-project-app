import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 Login Page")

username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")

if st.button("Login"):
    if username == "Fai" and password == "192837":
        st.success("Logged in successfully 🎉")
        st.session_state.logged_in = True
        st.switch_page("app.py")
    else:
        st.error("Wrong username or password")
