import streamlit as st

# ============================
#   HOME PAGE (NO HTML)
# ============================

st.title("💧 Smart Water System")
st.subheader("AI-Powered Leakage Detection & Consumption Analysis")

st.info("""
Smart Water System is an AI-powered platform developed to analyze water consumption,
detect potential leakages early, and support sustainability efforts.
By comparing previous and current usage, the system identifies unusual patterns
that may indicate hidden water loss.
""")

st.markdown("---")

st.header("⭐ Key Benefits")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💧 Early Leakage Detection")
    st.write("Detects abnormal usage instantly to prevent water loss.")

with col2:
    st.subheader("📊 Smarter Consumption")
    st.write("Provides accurate monthly consumption analytics.")

with col3:
    st.subheader("🌱 Sustainability")
    st.write("Supports national goals by reducing waste and improving efficiency.")

st.markdown("---")

st.success("🚀 Ready to explore? Go to the prediction page from the sidebar!")

            
