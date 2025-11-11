
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

# Prediction button
if st.button("🔍 Predict"):
        data = np.array([[prev_use, curr_use]])
        prediction = model.predict(data)

        # 🔹 حساب نسبة التغير
        change_rate = ((curr_use - prev_use) / prev_use) * 100

        # 🔹 منطق العتبة Threshold
        if abs(change_rate) <= 10:
            st.success(f"✅ No Leak Detected. Change rate is only {change_rate:.1f}%. Water usage is normal.")
        else:
            if prediction[0] == 1:
                st.error(f"🚨 Leak Detected! Water usage changed by {change_rate:.1f}%. Please check the system immediately.")
            else:
                st.success(f"✅ No Leak Detected. Change rate: {change_rate:.1f}%.")

    # Footer
    st.markdown("---")
    st.caption("Developed by Fai Alshamary | Powered by XGBoost & Streamlit ✨")
