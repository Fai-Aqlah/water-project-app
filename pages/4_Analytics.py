import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load style
from style_analytics import load_analytics_style
load_analytics_style()

st.title("📊 Water Analytics Dashboard")
st.markdown("### Deep Insights into Water Consumption & Leakage Patterns 💧")

# Load data
df = pd.read_csv("water_data_clean.csv")

# --- SUMMARY BOXES ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Average Previous", round(df["previous_consumption"].mean(), 2))
col2.metric("Average Current", round(df["current_consumption"].mean(), 2))
col3.metric("Average Diff", round(df["consumption_diff"].mean(), 2))
col4.metric("Leakage Count", df["leak_detected"].sum())

st.markdown("---")

# HISTOGRAM 1
st.subheader("Distribution of Previous Consumption")
fig1, ax1 = plt.subplots()
sns.histplot(df["previous_consumption"], kde=True, ax=ax1)
st.pyplot(fig1)

# HISTOGRAM 2
st.subheader("Distribution of Current Consumption")
fig2, ax2 = plt.subplots()
sns.histplot(df["current_consumption"], kde=True, ax=ax2)
st.pyplot(fig2)

st.markdown("---")

# BOX PLOT
st.subheader("Consumption Difference - Box Plot")
fig3, ax3 = plt.subplots()
sns.boxplot(x=df["consumption_diff"], ax=ax3)
st.pyplot(fig3)

# PIE CHART
st.subheader("Leakage Ratio")
labels = ["No Leak", "Leak Detected"]
sizes = [
    len(df[df["leak_detected"] == 0]),
    len(df[df["leak_detected"] == 1])
]
fig4, ax4 = plt.subplots()
ax4.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
st.pyplot(fig4)

st.markdown("---")

# CORRELATION HEATMAP
st.subheader("Correlation Heatmap")
fig5, ax5 = plt.subplots()
sns.heatmap(df.corr(), annot=True, cmap="Blues", ax=ax5)
st.pyplot(fig5)
