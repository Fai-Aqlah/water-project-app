import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Home", layout="centered")

# ----------------------- HEADER -----------------------
header_html = """
<div style="
    text-align:center;
    padding:20px;
    margin-top:20px;
">
    <h1 style="
        font-size:50px;
        font-weight:900;
        color:#1b4d3e;
    ">
        Smart Water System 💧
    </h1>

    <p style="
        font-size:20px;
        margin-top:10px;
        color:#4a4a4a;
        font-weight:600;
    ">
        AI-powered water consumption prediction and leakage detection
    </p>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)


# ----------------------- WELCOME MESSAGE -----------------------
if "username" in st.session_state:
    st.markdown(
        f"<h2 style='text-align:center; color:#1b4d3e;'>Welcome, {st.session_state.username}! 👋💧</h2>",
        unsafe_allow_html=True
    )


# ----------------------- ABOUT THE PROJECT -----------------------
st.markdown("""
<div style="
    background:#f1f7f2;
    padding:25px;
    border-radius:15px;
    margin-top:25px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    text-align:center;
">
    <h3 style="color:#1b4d3e; font-weight:800;">About the Project</h3>
    <p style="font-size:17px; color:#4a4a4a; margin-top:10px;">
        This system uses Machine Learning to analyze water consumption patterns and detect potential leakage early.<br><br>
        By comparing previous and current usage, the model identifies abnormal increases that may indicate hidden water loss.<br><br>
        The goal is to support the Ministry of Environment, Water & Agriculture in improving water efficiency, reducing waste,
        and enabling smarter decision-making based on data rather than manual estimation.
    </p>
</div>
""", unsafe_allow_html=True)


# ----------------------- MAIN BUTTON -----------------------
st.write("")
st.write("")

if st.button(" Go to Prediction Page", use_container_width=True):
    st.switch_page("app.py")


# ----------------------- FOOTER -----------------------
st.markdown("""
<div style="text-align:center; margin-top:40px; color:#777;">
    <hr>
    <p>Developed by Fai Aqlah | Ministry of Environment, Water & Agriculture – Hail Branch 🌿💧</p>
</div>
""", unsafe_allow_html=True)
