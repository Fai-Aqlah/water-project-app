
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('xgboost_model.pkl')

# App setup
st.set_page_config(page_title="💧 Water Consumption & Leak Detection System", layout="centered")
st.title("🚰 Smart Water Consumption Prediction & Leak Detection")
st.markdown("### Using **XGBoost** for intelligent water monitoring 💡")

# Input section
prev_use = st.number_input("Enter previous consumption:", min_value=0.0, step=0.1)
curr_use = st.number_input("Enter current consumption:", min_value=0.0, step=0.1)

if st.button("🔍 Predict"):
    # حساب نسبة التغير
    change_rate = ((curr_use - prev_use) / prev_use) * 100 if prev_use != 0 else 0

    # تحديد فئة الاستهلاك
    def consumption_level(value):
        if value < 500:
            return "Low"
        elif value < 1500:
            return "Medium"
        else:
            return "High"

    prev_level = consumption_level(prev_use)
    curr_level = consumption_level(curr_use)

    # منطق القرار
    if curr_use == prev_use:
        if curr_level == "High":
            st.warning(f"⚠️ High constant consumption detected ({curr_use} L). Try to reduce usage.")
        elif curr_level == "Medium":
            st.info(f"ℹ️ Stable average consumption ({curr_use} L). No leak detected.")
        else:
            st.success("✅ Stable and efficient water usage. Keep it up!")
    elif curr_use < prev_use:
        st.success(f"✅ Excellent! Water usage decreased by {abs(change_rate):.1f}%. Great efficiency!")
    elif change_rate > 10:
        st.error(f"🚨 Leak or Overuse Detected! Water usage increased by {change_rate:.1f}%. Please check the system.")
    else:
        st.warning(f"⚠️ Slight increase ({change_rate:.1f}%). Keep monitoring your consumption.")

    # عرض المستوى الحالي والسابق دائمًا تحت النتيجة
    st.info(f"Previous Level: {prev_level} | Current Level: {curr_level}")



# Footer
st.markdown("---")
st.caption("Developed by Fai Alshamary | Powered by XGBoost & Streamlit ✨")

