import streamlit as st
import pandas as pd
from database import load_predictions

st.title("📊 Stored Predictions History")
st.write("Below is the full history of all water consumption predictions stored in the system.")
# LOAD PAGE-SPECIFIC CSS
try:
    with open("pages/style_database.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    st.warning("⚠️ style_database.css not found.")

# LOAD DATA
data = load_predictions()

if not data:
    st.info("ℹ️ No prediction records found yet.")
else:
    df = pd.DataFrame(data, columns=[
        "ID",
        "Previous Use (L)",
        "Current Use (L)",
        "Difference (L)",
        "Change Rate (%)",
        "Result",
        "Timestamp"
    ])

    # Round numeric columns
    df["Previous Use (L)"] = df["Previous Use (L)"].astype(float).round(2)
    df["Current Use (L)"] = df["Current Use (L)"].astype(float).round(2)
    df["Difference (L)"] = df["Difference (L)"].astype(float).round(2)
    df["Change Rate (%)"] = df["Change Rate (%)"].astype(float).round(2)

    # Display table
    st.dataframe(df, use_container_width=True)

    # Count
    st.success(f"✔ Total Records: {len(df)}")

    # Download CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="water_predictions_history.csv",
        mime="text/csv"
    )

