import streamlit as st
import pandas as pd
import plotly.express as px
from database import load_predictions

# Load CSS styling
with open("pages/style_analytics.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# LOGIN CHECK
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("🚫 You must log in first from the Login page.")
    st.stop()

# PAGE TITLE
st.title("📊 Water Analytics Dashboard 💧")

# LOAD DATABASE DATA
data = load_predictions()

if not data:
    st.warning("⚠️ No data available for analytics.")
    st.stop()

# Convert to DataFrame
df = pd.DataFrame(data, columns=[
    "ID",
    "Previous",
    "Current",
    "Difference",
    "ChangeRate",
    "Result",
    "Timestamp"
])

# Clean numeric fields
df["Previous"] = df["Previous"].astype(float)
df["Current"] = df["Current"].astype(float)
df["Difference"] = df["Difference"].astype(float)
df["ChangeRate"] = df["ChangeRate"].astype(float)

# METRICS
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Avg Previous", f"{df['Previous'].mean():.2f}")

with col2:
    st.metric("Avg Current", f"{df['Current'].mean():.2f}")

with col3:
    st.metric("Avg Δ Change", f"{df['Difference'].mean():.2f}")

with col4:
    leaks = df[df["Result"] == "Leak"].shape[0]
    st.metric("Leak Count", leaks)

st.divider()

# TABS
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Distributions",
    "🚨 Leakage Analysis",
    "🔍 Comparison",
    "📈 Trends"
])

# TAB 1 — DISTRIBUTIONS
with tab1:
    st.subheader("📦 Previous Consumption Distribution")
    fig1 = px.histogram(df, x="Previous", nbins=20, color_discrete_sequence=["#4177b4"])
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📦 Current Consumption Distribution")
    fig2 = px.histogram(df, x="Current", nbins=20, color_discrete_sequence=["#28a02c"])
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📦 Change Rate Distribution")
    fig3 = px.histogram(df, x="ChangeRate", nbins=20, color_discrete_sequence=["#d02728"])
    st.plotly_chart(fig3, use_container_width=True)

# TAB 2 — LEAK ANALYSIS
with tab2:
    st.subheader("🚨 Leakage Detection (Yes / No)")
    fig4 = px.histogram(df, x="Result", color="Result",
                        color_discrete_sequence=["#4177b4", "#d02728", "#28a02c"])
    st.plotly_chart(fig4, use_container_width=True)

# TAB 3 — COMPARISON
with tab3:
    st.subheader("🔍 Previous vs Current Consumption Comparison")
    fig5 = px.scatter(df, x="Previous", y="Current", color="Result",
                      color_discrete_sequence=["#4177b4", "#d02728", "#28a02c"])
    fig5.update_layout(xaxis_title="Previous Consumption", yaxis_title="Current Consumption")
    st.plotly_chart(fig5, use_container_width=True)

# TAB 4 — TRENDS
with tab4:
    st.subheader("📈 Consumption Trends Over Time")
    df_sorted = df.sort_values(by="Timestamp")

    fig6 = px.line(df_sorted, x="Timestamp", y="Current",
                   color_discrete_sequence=["#4177b4"])
    fig6.update_layout(xaxis_title="Time", yaxis_title="Current Consumption")
    st.plotly_chart(fig6, use_container_width=True)

    st.subheader("📈 Change Rate Trend")
    fig7 = px.line(df_sorted, x="Timestamp", y="ChangeRate",
                   color_discrete_sequence=["#d02728"])
    fig7.update_layout(xaxis_title="Time", yaxis_title="Change Rate (%)")
    st.plotly_chart(fig7, use_container_width=True)

# NAVIGATION BUTTON
st.divider()
if st.button("📁 Go to Database Records"):
    st.switch_page("pages/5_DatabaseView.py")


      
       
    



