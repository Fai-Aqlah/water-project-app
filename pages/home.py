import streamlit as st
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("❌ You must log in first from the Login page.")
    st.stop()


st.set_page_config(page_title="Home", layout="centered")

# ====== MAIN CONTAINER ======
st.markdown("""
<style>
.center-box {
    max-width: 800px;
    margin: auto;
    background: #ffffff;
    padding: 35px;
    border-radius: 18px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.12);
}
.title {
    font-size: 42px;
    font-weight: 900;
    color: #1b4d3e;
    text-align: center;
}
.subtitle {
    font-size: 19px;
    text-align: center;
    margin-top: -10px;
    color: #5f5f5f;
}
.box {
    background: #f3f7f4;
    padding: 25px;
    border-radius: 15px;
    margin-top: 25px;
}
.section-title {
    font-size: 22px;
    font-weight: 800;
    color: #1b4d3e;
    text-align: center;
}
.text {
    font-size: 17px;
    text-align: center;
    color: #4a4a4a;
    line-height: 1.6;
}
.button-style {
    font-size: 18px !important;
    padding: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ====== PAGE CONTENT ======
with st.container():
    st.markdown("<div class='center-box'>", unsafe_allow_html=True)

    st.markdown("<div class='title'>Smart Water System 💧</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>AI-powered prediction & leakage detection</div>", unsafe_allow_html=True)
    
    # Welcome message
    if "username" in st.session_state:
        st.markdown(
            f"<h3 style='text-align:center; color:#1b4d3e; margin-top:20px;'>Welcome, {st.session_state.username}! 👋💧</h3>",
            unsafe_allow_html=True
        )

    # About Box
    st.markdown("""
    <div class="box">
        <div class="section-title">About the Project</div>
        <p class="text">
            This system uses Machine Learning to analyze water consumption patterns and detect potential leakage early.<br><br>
            By comparing previous and current usage, the model identifies abnormal increases 
            that may indicate hidden water loss.<br><br>
            The goal is to support the Ministry of Environment, Water & Agriculture in improving 
            water efficiency, reducing waste, and enabling smarter decision-making based on data.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # Main Button
    if st.button("🔮 Go to Prediction Page", use_container_width=True):
        st.switch_page("app.py")

    # Footer
    st.markdown("""
    <p style="text-align:center; margin-top:35px; color:#777;">
    Developed by Fai Aqlah | Ministry of Environment, Water & Agriculture – Hail Branch 🌿💧
    </p>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

