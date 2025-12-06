import streamlit as st
import pandas as pd
from database import get_all_records
with open("pages/style_database.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("📄 Prediction Records (Database Logs)")
st.markdown("💧 This page displays all prediction logs stored in the system.")

# -------------------------------
# 1) Load records from database
# -------------------------------
records = get_all_records()

if not records or len(records) == 0:
    st.warning("⚠️ No records found. Please perform at least one prediction.")
    st.stop()

# Convert to DataFrame
df = pd.DataFrame(records, columns=[
    "ID",
    "Previous",
    "Current",
    "Difference",
    "Change Rate",
    "Status",
    "Created At"
])

# --------------------------------
# 2) Show the full table
# --------------------------------
st.subheader("📌 Latest Prediction Records")
st.dataframe(df, use_container_width=True)

# --------------------------------
# 3) Quick Statistics
# --------------------------------
st.subheader("📊 Quick Statistics")

total = len(df)
stable_count = (df["Status"] == "Stable").sum()
leak_count = (df["Status"] == "Leak").sum()
warning_count = (df["Status"] == "Warning").sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", total)
col2.metric("Stable Cases", stable_count)
col3.metric("Leak Cases", leak_count)
col4.metric("Warnings", warning_count)

# --------------------------------
# 4) Download CSV
# --------------------------------
st.subheader("⬇️ Download Records")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="prediction_logs.csv",
    mime="text/csv"
)


