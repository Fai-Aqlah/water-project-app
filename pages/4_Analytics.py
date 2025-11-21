import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- تحميل ملف CSS ----------------
with open("pages/style_analytics.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- عنوان الصفحة ----------------
st.title("📊 Water Analytics Dashboard")
st.markdown("### Deep insights into water consumption & leakage patterns 💧")

# ---------------- تحميل البيانات ----------------
df = pd.read_csv("water_data_clean.csv")

required_cols = [
    "previous_consumption",
    "current_consumption",
    "consumption_diff",
    "leak_detected",
    "district",
    "temperature",
    "humidity",
]

missing = [c for c in required_cols if c not in df.columns]
if missing:
    st.error(f"❌ Missing columns in dataset: {', '.join(missing)}")
    st.stop()

# ---------------- إحصائيات عامة ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Previous", round(df["previous_consumption"].mean(), 2))
col2.metric("Average Current", round(df["current_consumption"].mean(), 2))
col3.metric("Average Diff", round(df["consumption_diff"].mean(), 2))
col4.metric("Leakage Count", int(df["leak_detected"].sum()))

st.markdown("---")

# ---------------- Tabs ----------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["Consumption Distribution", "Leakage Analysis", "Trends", "Correlations"]
)

# ================= TAB 1 =================
with tab1:
    st.subheader("Water Consumption Distribution")

    left, right = st.columns(2)

    with left:
        st.markdown("**Previous Consumption**")
        fig1, ax1 = plt.subplots()
        sns.histplot(df["previous_consumption"], kde=True, ax=ax1)
        ax1.set_xlabel("Previous Consumption (m³)")
        st.pyplot(fig1)

    with right:
        st.markdown("**Current Consumption**")
        fig2, ax2 = plt.subplots()
        sns.histplot(df["current_consumption"], kde=True, ax=ax2)
        ax2.set_xlabel("Current Consumption (m³)")
        st.pyplot(fig2)

# ================= TAB 2 =================
with tab2:
    st.subheader("Leakage Analysis by District")

    leak_by_district = (
        df.groupby("district")["leak_detected"].sum().sort_values(ascending=False)
    )

    fig3, ax3 = plt.subplots()
    leak_by_district.plot(kind="bar", ax=ax3)
    ax3.set_xlabel("District")
    ax3.set_ylabel("Leakage Count")
    plt.xticks(rotation=45)
    st.pyplot(fig3)

    leakage_rate = df["leak_detected"].mean() * 100
    st.metric("Overall Leakage Rate", f"{leakage_rate:.2f}%")

# ================= TAB 3 =================
with tab3:
    st.subheader("Consumption Trends (Index-based)")

    fig4, ax4 = plt.subplots()
    ax4.plot(df.index, df["previous_consumption"], label="Previous")
    ax4.plot(df.index, df["current_consumption"], label="Current")
    ax4.set_xlabel("Record Index")
    ax4.set_ylabel("Consumption (m³)")
    ax4.legend()
    st.pyplot(fig4)

# ================= TAB 4 =================
with tab4:
    st.subheader("Correlation Heatmap")

    numeric_cols = [
        "previous_consumption",
        "current_consumption",
        "consumption_diff",
        "temperature",
        "humidity",
    ]

    if pd.api.types.is_numeric_dtype(df["leak_detected"]):
        numeric_cols.append("leak_detected")

    corr = df[numeric_cols].corr()

    fig5, ax5 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", square=True, ax=ax5)
    ax5.set_title("Correlation Matrix")
    st.pyplot(fig5)
