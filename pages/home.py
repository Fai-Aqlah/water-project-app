import streamlit as st

# استدعاء ملف التنسيق
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()

# ==========================
#        الصفحة الرئيسية
# ==========================

# ---- العنوان الرئيسي ----
st.markdown(
    """
    <div class="intro-card">
        <h1 class="home-title">Smart Water System 💧🌿</h1>
        <p class="home-description">
            Smart Water System is an AI-powered platform developed to analyze water consumption,
            detect potential leakages early, and support sustainability efforts. By comparing previous
            and current usage, the system identifies unusual patterns that may indicate hidden water loss.
            This system assists both citizens and the Ministry in improving water efficiency and informed
            decision-making.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- العنوان الفرعي للفوائد ----
st.markdown(
    """
    <h2 class="section-title">🌟 Key Benefits</h2>
    """,
    unsafe_allow_html=True
)

# ---- كروت الفوائد ----
st.markdown(
    """
    <div class="benefit-card">
        <h3 class="benefit-title">💧 Early Leakage Detection</h3>
        <p>Detects abnormal water usage instantly and prevents hidden leaks before major damage occurs.</p>
    </div>

    <div class="benefit-card">
        <h3 class="benefit-title">📊 Smarter Consumption Insights</h3>
        <p>Provides accurate month-to-month usage analysis to help citizens understand and optimize their consumption.</p>
    </div>

    <div class="benefit-card">
        <h3 class="benefit-title">📩 Automatic Email Alerts</h3>
        <p>Sends instant AI-powered email notifications when sudden spikes in consumption indicate a possible leakage.</p>
    </div>

    <div class="benefit-card">
        <h3 class="benefit-title">🌱 Supports Sustainability</h3>
        <p>Helps reduce water waste and supports the Ministry’s long-term environmental and sustainability goals.</p>
    </div>

    <div class="benefit-card">
        <h3 class="benefit-title">🏛️ Ministry Decision Support</h3>
        <p>Improves monitoring accuracy and supports data-driven planning for better national water management.</p>
    </div>
    """,
    unsafe_allow_html=True
)


# ------------------- BUTTON -------------------
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='text-align:center; color:#1b4d3e;'>Ready to explore the prediction model? 🚀</h3>",
    unsafe_allow_html=True
)

center = st.columns(3)[1]  # زر بالوسط

with center:
    go = st.button("Go to Prediction Page 👉", use_container_width=True)

if go:
    st.switch_page("app.py")

