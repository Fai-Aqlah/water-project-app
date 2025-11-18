import streamlit as st

# --- LOAD CSS ---
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()
st.markdown("""
<div class="main-card">
    <h1 class="home-title">Smart Water System 💧🌿</h1>
    <p class="home-description">
        AI-powered water consumption analysis & leakage detection.
    </p>
</div>
""", unsafe_allow_html=True)




