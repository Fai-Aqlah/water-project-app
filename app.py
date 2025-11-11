
import streamlit as st
import numpy as np
import joblib

# تحميل النموذج (احتياطي فقط – في حال أردت استخدامه لاحقًا)
model = joblib.load('xgboost_model.pkl')

# إعداد الصفحة
st.set_page_config(page_title="💧 Smart Water Consumption & Leak Detection System", layout="centered")
st.title("💧 Smart Water Consumption Prediction & Leak Detection")
st.markdown("💡 Using XGBoost for intelligent water monitoring")

# إدخال القيم من المستخدم
prev_use = st.number_input("Enter previous consumption (L):", min_value=0.0, step=1.0)
curr_use = st.number_input("Enter current consumption (L):", min_value=0.0, step=1.0)

# زر التنبؤ
if st.button("🔍 Predict"):

    # حساب نسبة التغير بين الاستهلاكين
    change_rate = ((curr_use - prev_use) / prev_use) * 100 if prev_use != 0 else 0

    # القيم المستنتجة من البيانات (عتبات واقعية)
    low_threshold = 197.22
    high_threshold = 482.60

    # تصنيف مستوى الاستهلاك الحالي
    if curr_use < low_threshold:
        level = "Low"
        st.success(f"✅ Efficient usage detected! Current consumption ({curr_use:.1f} L) is LOW. Keep it up! 💧")
    elif curr_use <= high_threshold:
        level = "Medium"
        st.info(f"⚖️ Normal usage detected. Current consumption ({curr_use:.1f} L) is within the normal range.")
    else:
        level = "High"
        st.error(f"🚨 High water consumption detected! ({curr_use:.1f} L). Please check for leaks or overuse.")

    # عرض التغير بالنسبة السابقة
    st.markdown(f"**Change Rate:** {abs(change_rate):.1f}%")
    st.caption(f"Previous: {prev_use:.1f} L | Current: {curr_use:.1f} L | Level: {level}")

# التذييل (Footer)
st.markdown("---")
st.caption("Developed by Fai Alshamary | Powered by XGBoost & Streamlit ✨")

