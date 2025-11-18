import streamlit as st

# --- LOAD CSS ---
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()

# --- HTML CONTENT ---
html_code = """
<div class="home-container">

    <div class="intro-card">
        <h1 class="home-title">Smart Water System 💧🌿</h1>
        <p class="home-description">
            Smart Water System is an AI-powered platform designed to analyze water consumption
            and detect potential leakages. By comparing previous and current usage,
            the model identifies abnormal spikes that may indicate hidden water loss.
            The system supports the Ministry of Environment, Water & Agriculture 
            in improving sustainability, reducing waste, and enabling smarter decision-making 
            with accurate monitoring.
        </p>
    </div>

    <h2 class="benefits-title">⭐ Key Benefits</h2>

    <div class="benefits-container">

        <div class="benefit-card blue-border">
            <h3 class="benefit-title">🔍 Early Leakage Detection</h3>
            <p>Detects abnormal water usage instantly, allowing early intervention before significant water loss occurs.</p>
        </div>

        <div class="benefit-card green-border">
            <h3 class="benefit-title">📊 Smarter Consumption Management</h3>
            <p>Provides accurate monthly consumption analysis and improves awareness on efficient usage.</p>
        </div>

        <div class="benefit-card aqua-border">
            <h3 class="benefit-title">🌱 Environmental Sustainability</h3>
            <p>Supports national sustainability goals by minimizing waste and enhancing resource planning.</p>
        </div>

    </div>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
