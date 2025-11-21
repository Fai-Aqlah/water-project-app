import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# إعداد الصفحة
st.set_page_config(page_title="Analytics Dashboard", layout="wide")

# تحميل ملف CSS
def load_analytics_style():
    with open("style_analytics.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_analytics_style()

# تحميل البيانات
df = pd.read_csv("water_data_clean.csv")

st.title("📊 Water Consumption Analytics Dashboard")

# ------------------------------------------------
# 1. Summary Statistics
# ------------------------------------------------
st.subheader("📌 Summary Statistics")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Previous", round(df["previous_consumption"].mean(), 2))
col2.metric("Avg Current", round(df["current_consumption"].mean(), 2))
col3.metric("Avg Difference", round(df["consumption_diff"].mean(), 2))
col4.metric("Leak Count", int(df["leak_detected"].sum()))

# ------------------------------------------------
# 2. Histogram – Previous Consumption
# ------------------------------------------------
st.subheader("📈 Distribution of Previous Consumption")
fig1, ax1 = plt.subplots()
sns.histplot(df["previous_consumption"], kde=True, ax=ax1)
st.pyplot(fig1)

# ------------------------------------------------
# 3. Histogram – Current Consumption
# ------------------------------------------------
st.subheader("📈 Distribution of Current Consumption")
fig2, ax2 = plt.subplots()
sns.histplot(df["current_consumption"], kde=True, ax=ax2)
st.pyplot(fig2)

# ------------------------------------------------
# 4. Leakage Rate
# ------------------------------------------------
st.subheader("🚨 Leakage Detection Rate")

leak_counts = df["leak_detected"].value_counts()
fig3, ax3 = plt.subplots()
plt.pie(leak_counts, labels=["No Leak", "Leak"], autopct="%1.1f%%", colors=["#5EC9E8", "#FF7070"])
plt.title("Leak Percentage")
st.pyplot(fig3)

# ------------------------------------------------
# 5. Correlation Heatmap
# ------------------------------------------------
st.subheader("🔍 Feature Correlation Heatmap")

fig4, ax4 = plt.subplots()
sns.heatmap(df.corr(), annot=True, cmap="Blues", linewidths=0.5, ax=ax4)
st.pyplot(fig4)

