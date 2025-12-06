import streamlit as st
import pandas as pd
from database import get_all_records

# ============================
# Load Custom CSS from /pages/
# ============================
with open("pages/style_database.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ============================
# Page Title
# ============================
st.markdown("<h1 class='db-title'>📂 Prediction Logs</h1>", unsafe_allow_html=True)
st.markdown("<p class='db-subtitle'>All prediction records stored in the system</p>", unsafe_allow_html=True)


# ============================
# Custom HTML Status Coloring
# ============================
def color_status(val):
    if val == "Normal":
        return '<span class="status-normal">Normal</span>'
    elif val == "Warning":
        return '<span class="status-warning">Warning</span>'
    elif val == "Leak":
        return '<span class="status-leak">Leak</span>'
    return val


# ============================
# Load records from database
# ============================
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

# Apply colored status column
df["Status"] = df["Status"].apply(color_status)


# ============================
# Show Table
# ============================
st.subheader("📊 Latest Prediction Records")
st.markdown(df.to_html(escape=False), unsafe_allow_html=True)


# ============================
# Quick Statistics
# ============================
st.subheader("📈 Quick Statistics")

total = len(df)
stable_count = (df["Status"].str.contains("Normal")).sum()
leak_count = (df["Status"].str.contains("Leak")).sum()
warning_count = (df["Status"].str.contains("Warning")).sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"<div class='stats-box'><div class='stats-number'>{total}</div><div class='stats-label'>Total Records</div></div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='stats-box'><div class='stats-number'>{stable_count}</div><div class='stats-label'>Stable Cases</div></div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<div class='stats-box'><div class='stats-number'>{leak_count}</div><div class='stats-label'>Leak Cases</div></div>", unsafe_allow_html=True)

with col4:
    st.markdown(f"<div class='stats-box'><div class='stats-number'>{warning_count}</div><div class='stats-label'>Warnings</div></div>", unsafe_allow_html=True)


# ============================
# Download Records
# ============================
st.subheader("📥 Download Records")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download CSV",
    data=csv,
    file_name="prediction_logs.csv",
    mime="text/csv",
    use_container_width=True
)
