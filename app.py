
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
if st.button("🔎 Predict"):
    data = np.array([[prev_use, curr_use]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("🚨 Leak Detected! Please check the system immediately.")
    else:
        st.success("✅ No leak detected. Water usage is normal.")

# Footer
st.markdown("---")
st.caption("Developed by Fai Alshamary | Powered by XGBoost & Streamlit 🌟")
