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


# ========= Why This System Matters =========
st.markdown("## Why This System Matters 💡")

with st.container():
    st.markdown(
        """
- Helps citizens detect hidden leaks early  
- Supports national sustainability goals  
- Reduces wasted water and monthly bills  
- Enhances awareness about individual water usage  
- Strengthens Ministry decision-making  
"""
    )

st.write("")  # مسافة بين البوكسين


# ========= Behind the Model =========
st.markdown("## Behind the Model ⚙️")

with st.container():
    st.markdown(
        """
We tested multiple machine-learning models to find the most stable and reliable one:

- **Decision Tree**  
- **Random Forest**  
- **XGBoost (final model — 91% accuracy)**  

### Why XGBoost?
- Handles fluctuating data well  
- Low overfitting  
- Works efficiently with real-world patterns  
- Produces highly reliable predictions  
"""
    )

st.markdown("###  Key Benefits")

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

st.markdown("### 📌 Project Timeline")

st.write("""
- **Week 1-2:** Data cleaning & preprocessing  
- **Week 3-4:** Model training & evaluation  
- **Week 5-6:** Building the interactive Streamlit app  
- **Week 7-8:** Email alert integration & UI polishing  
""")


st.markdown("<h3 class='prediction-title'>Ready to explore the model predictions?</h3>", unsafe_allow_html=True)

if st.button("🔵 Go to Prediction Page"):
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

