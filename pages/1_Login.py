import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# عنوان
st.markdown("<h2 style='text-align:center;'>🔐 Login Page</h2>", unsafe_allow_html=True)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "Fai" and password == "1929837":
        st.session_state.logged_in = True
        st.success("Login successful! 🎉")
        st.experimental_rerun()
    else:
        st.error("Wrong username or password ❌")

