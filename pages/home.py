import streamlit as st

# استدعاء تنسيق صفحة الهوم
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("🚫 You must log in first from the Login page.")
    st.stop()

# العنوان الرئيسي
st.markdown(
    "<h1 class='main-title'>Smart Water System 💧🌿</h1>",
    unsafe_allow_html=True
)

# العنوان الفرعي
st.markdown(
    "<h2 class='subtitle'>AI-Powered Leakage Detection & Consumption Analysis</h2>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class='project-description'>
    Smart Water System is an AI-powered platform designed to analyze water consumption, 
    detect potential leakages early, and support sustainability goals.  
    By comparing previous and current usage, the system identifies 
    unusual patterns that may indicate hidden water loss — helping 
    citizens reduce waste and enabling the Ministry to make smarter 
    national water decisions.
    </p>
    """,
    unsafe_allow_html=True
)


# ===== Why This System Matters =====
st.markdown(
    """
    <div class='why-box'>
        <h3>Why This System Matters 💡</h3>
        <ul>
            <li>Helps citizens detect hidden leaks early</li>
            <li>Supports national sustainability goals</li>
            <li>Reduces wasted water and monthly bills</li>
            <li>Enhances awareness about individual water usage</li>
            <li>Strengthens Ministry decision-making</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
<div class="model-box">
<h3>Behind the Model 🔍</h3>
<p>We tested multiple machine-learning models to find the most stable and reliable option:</p>

<ul>
<li>Decision Tree</li>
<li>Random Forest</li>
<li><b>XGBoost</b> (final model — <b>91% accuracy</b>)</li>
</ul>

<h4>Why XGBoost?</h4>
<ul>
<li>Handles fluctuating data well</li>
<li>Low overfitting</li>
<li>Works efficiently with real-world patterns</li>
<li>Produces highly reliable predictions</li>
</ul>
</div>
    """,
    unsafe_allow_html=True
)







st.markdown(
    """
<div style="text-align: center; margin-top: 40px; margin-bottom: 20px;">
    <h2 style="font-weight: 800;">Key Benefits</h2>
</div>
""",
    unsafe_allow_html=True
)

st.markdown("""
<div class='benefit-card green-card'>
    <h3 class='benefit-title'>💧 Early Leakage Detection</h3>
    <p>Detects abnormal usage instantly and prevents hidden leaks before major damage occurs.</p>
</div>

<div class='benefit-card blue-card'>
    <h3 class='benefit-title'>📊 Smarter Consumption Insights</h3>
    <p>Provides clear monthly analytics to help citizens understand and improve their water usage.</p>
</div>

<div class='benefit-card yellow-card'>
    <h3 class='benefit-title'>⭐ Supports the Ministry & Citizens</h3>
    <p>Improves planning efforts and guides better resource distribution across regions.</p>
</div>

<div class='benefit-card orange-card'>
    <h3 class='benefit-title'>📩 Automatic Email Alerts</h3>
    <p>Sends instant notifications when the system detects abnormal usage or potential leakage.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### <span class='timeline-title'>📌 Project Timeline</span>", unsafe_allow_html=True)

st.markdown(
    """
<span class='timeline-content'>
Week 1–2: Data cleaning & preprocessing  
Week 3–4: Model training & evaluation  
Week 5–6: Building the interactive Streamlit app  
Week 7–8: Email alert integration & UI polishing  
Week 9–10: Final system refinement & testing  
</span>
""",
    unsafe_allow_html=True
)






# العبارة في الوسط
st.markdown(
    "<h3 style='text-align:center;'>Ready to explore the model predictions?</h3>",
    unsafe_allow_html=True
)

# الزر في الوسط
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("Go to Prediction Page"):
        st.switch_page("app.py")




# الفوتر
st.markdown("""
<hr style='margin-top:15px; margin-bottom:10px; border: 1px solid #4CAF50;'>

<div style='text-align:center; color:#156b3a; font-weight:bold; font-size:22px;'>
    Developed by <b style="color:#0277bd;">Fai Aqlah</b> | Ministry of Environment, Water & Agriculture 🌿💧 – Hail Branch
    <br>
    Powered by <b>XGBoost</b> & <b>Streamlit</b>
</div>
""", unsafe_allow_html=True)

