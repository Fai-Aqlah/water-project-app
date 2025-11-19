import streamlit as st

# استدعاء ملف التنسيق
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()


# ===========================
#    الصفحة الرئيسية
# ===========================

# العنوان الرئيسي
st.markdown(
    "## Smart Water System: AI-Driven Consumption Analysis & Early Leakage Detection
💧🌿", unsafe_allow_html=False)

# الوصف العام
st.markdown("""
### AI-Powered Leakage Detection & Consumption Analysis

Smart Water System is an AI-powered platform developed to analyze water consumption, 
detect potential leakages early, and support sustainability efforts.  
By comparing previous and current usage, the system identifies unusual patterns 
that may indicate hidden water loss — helping both citizens and the Ministry 
improve water efficiency and make smarter decisions.
""")

st.divider()


# ===========================
#   الفوائد (بدون HTML)
# ===========================

st.markdown("## ⭐ Key Benefits")

st.success("### 💧 Early Leakage Detection\nDetects abnormal usage instantly and prevents hidden leaks before major damage occurs.")

st.info("### 📊 Smarter Consumption Insights\nProvides clear monthly analysis to help citizens understand their water usage better.")

st.warning("### 🌱 Supports Sustainability\nHelps reduce waste and supports national environmental goals.")

st.error("### 📩 Smart Email Alerts\nSends automatic email notifications when abnormal consumption or leakage is detected.")

st.divider()


# زر الانتقال لصفحة التنبؤ
st.markdown("### 🌟 Ready to explore the prediction model?")

if st.button("Go to Prediction Page "):
    st.switch_page("app.py")


