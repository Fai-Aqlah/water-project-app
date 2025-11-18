import streamlit as st

# --- LOAD CSS ---
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()



st.markdown("""
<div class="project-box">
    <h2 class="section-title">Smart Water System 💧🌿</h2>
    <p class="project-description">
        Smart Water System is an AI-powered platform designed to analyze water consumption and detect potential leakage early.
        The system compares previous and current usage to identify unusual spikes, enabling faster intervention and reducing unnecessary water waste.
        This project supports the Ministry of Environment, Water & Agriculture in improving sustainability,
        enhancing monitoring accuracy, and accelerating digital transformation.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown(
    """
    <h2 class="section-title">⭐ Key Benefits</h2>

    <div class="benefits-container">

        <div class="benefit-card blue-border">
            <h3 class="benefit-title">💧 Early Leakage Detection</h3>
            <p class="benefit-text">
                Detects abnormal water usage instantly, allowing early intervention before significant water loss occurs.
            </p>
        </div>

        <div class="benefit-card green-border">
            <h3 class="benefit-title">📊 Smarter Consumption Management</h3>
            <p class="benefit-text">
                Provides accurate monthly consumption analysis, improving awareness and reducing unnecessary usage.
            </p>
        </div>

        <div class="benefit-card aqua-border">
            <h3 class="benefit-title">🌿 Environmental Sustainability</h3>
            <p class="benefit-text">
                Supports national sustainability goals by minimizing waste and enhancing resource planning.
            </p>
        </div>

    </div>
    """,
    unsafe_allow_html=True
)
