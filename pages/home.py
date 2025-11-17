import streamlit as st

# --- LOAD CSS ---
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()

# ---- PROTECT PAGE ----
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("❌ You must log in first from the Login page.")
    st.stop()

# ---- HOME CONTENT ----
st.markdown("<h1 class='home-title'>Smart Water System 💧</h1>", unsafe_allow_html=True)
st.markdown("<p class='home-subtitle'>AI-Based Leakage Detection & Consumption Analysis</p>", unsafe_allow_html=True)

st.markdown("<div class='home-box'>", unsafe_allow_html=True)

st.markdown("<div class='home-card'>💧 This system monitors water consumption using AI to detect leakage early.</div>", unsafe_allow_html=True)
st.markdown("<div class='home-card'>📊 It compares current and previous usage to identify unusual spikes.</div>", unsafe_allow_html=True)
st.markdown("<div class='home-card'>🌿 Helps reduce water waste and supports better resource management.</div>", unsafe_allow_html=True)

st.markdown("<div class='predict-btn'>", unsafe_allow_html=True)
if st.button("Go to Prediction Page ➡️"):
    st.switch_page("app.py")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown(
    """
    <p style='text-align:center; font-size:13px; color:#6c757d; margin-top:40px;'>
        Empowering Water Efficiency with AI 💧
    </p>
    """,
    unsafe_allow_html=True
)
