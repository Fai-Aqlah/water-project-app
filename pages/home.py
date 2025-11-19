import streamlit as st

# استدعاء تنسيق صفحة الهوم
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()

# عنوان رئيسي
st.markdown("<h1 class='main-title'>Smart Water System 💧🌿</h1>", unsafe_allow_html=True)

# عنوان فرعي
st.markdown("<h3 class='subtitle'>AI-Powered Leakage Detection & Consumption Analysis</h3>", unsafe_allow_html=True)

# الوصف
st.markdown(
    """
    <p class='project-description'>
    Smart Water System is an AI-powered platform developed to analyze water consumption, detect potential leakages early,  
    and support sustainability efforts.<br>
    By comparing previous and current usage, the system identifies unusual patterns that may indicate hidden water loss — helping both citizens and the Ministry improve efficiency and make smarter decisions.
    </p>
    """,
    unsafe_allow_html=True
)

# عنوان الفوائد
st.markdown("<h2 class='benefits-title'>⭐ Key Benefits</h2>", unsafe_allow_html=True)

# الفائدة 1
st.markdown("""
<div class='benefit-card green-card'>
    <h3>💧 Early Leakage Detection</h3>
    <p>Detects abnormal usage instantly and prevents hidden leaks before major damage occurs.</p>
</div>
""", unsafe_allow_html=True)

# الفائدة 2
st.markdown("""
<div class='benefit-card blue-card'>
    <h3>📊 Smarter Consumption Insights</h3>
    <p>Provides monthly analytics that help citizens understand their water usage better.</p>
</div>
""", unsafe_allow_html=True)

# الفائدة 3
st.markdown("""
<div class='benefit-card yellow-card'>
    <h3>🤝 Supports the Ministry & Citizens</h3>
    <p>Improves national sustainability efforts and guides better resource planning.</p>
</div>
""", unsafe_allow_html=True)

# الفائدة 4 — الإيميل
st.markdown("""
<div class='benefit-card orange-card'>
    <h3>📬 Automatic Email Alerts</h3>
    <p>Sends instant email notifications when the model detects abnormal usage or potential leakage.</p>
</div>
""", unsafe_allow_html=True)

