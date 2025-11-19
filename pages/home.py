import streamlit as st

# استدعاء ملف التنسيق الخاص بالهوم
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()

# ================== الصفحة الرئيسية ==================

# العنوان الرئيسي (بيكون لونه أزرق من ملف CSS)
st.markdown("# Smart Water System 💧🌿")

# وصف مختصر تحت العنوان (سطر ثانٍ)
st.markdown("### AI-Driven Water Consumption Analysis & Early Leakage Detection")

# الوصف العام (تعريف المشروع – بنلوّنه أخضر من الـ CSS)
st.markdown(
    """
Smart Water System is an AI-powered platform developed to analyze water consumption  
and detect potential leakages early. By comparing previous and current usage,  
the system identifies unusual patterns that may indicate hidden water loss,  
helping both citizens and the Ministry improve water efficiency  
and make smarter, data-driven decisions.
"""
)

st.divider()

# ================== الفوائد الرئيسية ==================

st.markdown("##  Key Benefits")

benefits = {
    "Early Leakage Detection 💧":
        "Detects abnormal water usage instantly and prevents hidden leaks before major damage occurs.",
    "Smarter Consumption Insights 📊":
        "Provides clear monthly insights that help citizens understand and optimize their water usage.",
    "Supports the Ministry & Citizens ⭐":
        "Helps the Ministry improve planning and sustainability efforts while guiding citizens to use water more responsibly.",
    "Automatic Email Alerts 📧":
        "Sends automatic email notifications when the model predicts extreme over-use that may indicate leakage."
}

# كل فائدة تظهر في بلوك مستقل تحت بعض
for title, text in benefits.items():
    st.markdown(f"### {title}")
    st.write(text)

st.divider()

# ================== زر الانتقال لصفحة التنبؤ ==================

st.markdown("####  Ready to explore the model predictions?")

# نخلي الزر في المنتصف باستخدام الأعمدة
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Go to Prediction Page"):
        # الانتقال لصفحة التنبؤ (app.py)
        st.switch_page("app.py")
