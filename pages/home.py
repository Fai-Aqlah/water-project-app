import streamlit as st

# تحميل التنسيق
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()

st.markdown("""
<div class="hero-card">

    <h1 class="home-title">Smart Water System 💧🌿</h1>

    <p class="home-description">
        Smart Water System is an AI-powered platform designed to analyze water consumption 
        and detect potential leakages.
        <br><br>
        By comparing previous and current usage, the model identifies abnormal increases 
        that may indicate hidden water loss.
        <br><br>
        The project supports the Ministry of Environment, Water & Agriculture in improving 
        sustainability, reducing waste, and enhancing decision-making with accurate data.
    </p>

</div>

<div class="benefits-section">
    <h2 class="benefits-title">⭐ Key Benefits</h2>

    <div class="benefits-container">

        <div class="benefit-card blue-border">
            <h3 class="benefit-title">🚰 Early Leakage Detection</h3>
            <p>Detects abnormal water usage instantly, allowing early intervention before loss occurs.</p>
        </div>

        <div class="benefit-card green-border">
            <h3 class="benefit-title">📊 Smarter Consumption Management</h3>
            <p>Provides accurate monthly consumption analysis and improves awareness.</p>
        </div>

        <div class="benefit-card aqua-border">
            <h3 class="benefit-title">🌿 Environmental Sustainability</h3>
            <p>Supports national sustainability goals by reducing waste and enhancing planning.</p>
        </div>

    </div>
</div>
""", unsafe_allow_html=True)
