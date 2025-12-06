import streamlit as st
import pandas as pd
import plotly.express as px
from database import load_predictions_df

# =======================
# Load CSS styling
# =======================
with open("pages/style_analytics.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =======================
# Login check (نفس كودك القديم)
# =======================
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("🚨 You must log in first from the login page.")
    st.stop()

# =======================
# Load Database Data
# =======================
df = load_predictions_df()   # ← مهم

st.title("📊 Water Analytics Dashboard 💧")

# =======================
# METRICS SECTION
# =======================
col1, col2, col3, col4 = st.columns(4)

avg_prev = df["previous"].mean()
avg_curr = df["current"].mean()
avg_change = df["change_rate"].mean()
leaks = df[df["status"] == "Leak"].shape[0]

col1.metric("Avg Previous", f"{avg_prev:.2f}")
col2.metric("Avg Current", f"{avg_curr:.2f}")
col3.metric("Avg Change Rate", f"{avg_change:.2f}")
col4.metric("Leak Count 🚨", leaks)

st.divider()

# =======================
# TABS
# =======================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Distributions", 
    "🚨 Leakage Analysis", 
    "📘 Comparison", 
    "📈 Trends"
])

# ============================================================
# TAB 1: DISTRIBUTIONS
# ============================================================
with tab1:

    st.subheader("📦 Previous Consumption Distribution")
    fig1 = px.histogram(
        df,
        x="previous",
        nbins=20,
        color_discrete_sequence=["#4177b4"]
    )
    fig1.update_layout(xaxis_title="Previous Consumption", yaxis_title="Count")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📦 Current Consumption Distribution")
    fig2 = px.histogram(
        df,
        x="current",
        nbins=20,
        color_discrete_sequence=["#26a02c"]
    )
    fig2.update_layout(xaxis_title="Current Consumption", yaxis_title="Count")
    st.plotly_chart(fig2, use_container_width=True)

# ============================================================
# TAB 2: LEAKAGE ANALYSIS
# ============================================================
with tab2:

    st.subheader("🚨 Leakage Detection (Yes / No)")
    fig3 = px.histogram(
        df,
        x="status",
        color="status",
        color_discrete_sequence=["#4177b4", "#dd2728"]
    )
    fig3.update_layout(xaxis_title="Leak Status", yaxis_title="Count")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("📦 Change Rate Distribution")
    fig4 = px.box(
        df,
        y="change_rate",
        color_discrete_sequence=["#4177b4"]
    )
    st.plotly_chart(fig4, use_container_width=True)

# ============================================================
# TAB 3: COMPARISON
# ============================================================
with tab3:

    st.subheader("📘 Previous vs Current Consumption Comparison")

    fig5 = px.scatter(
        df,
        x="previous",
        y="current",
        color="status",
        color_discrete_sequence=["#4177b4", "#dd2728"]
    )
    fig5.update_layout(
        xaxis_title="Previous Consumption",
        yaxis_title="Current Consumption",
        legend_title="Leak Detected?"
    )
    st.plotly_chart(fig5, use_container_width=True)

# ============================================================
# TAB 4: TRENDS
# ============================================================
with tab4:

    st.subheader("📈 Consumption Trends Over Time")

    fig6 = px.line(
        df,
        y=["previous", "current"],
        color_discrete_sequence=["#4177b4", "#26a02c"]
    )
    fig6.update_layout(
        xaxis_title="Index",
        yaxis_title="Consumption",
        legend_title="Type"
    )
    st.plotly_chart(fig6, use_container_width=True)

    st.subheader("📈 Change Rate Trend")

    fig7 = px.line(
        df,
        y="change_rate",
        color_discrete_sequence=["#dd2728"]
    )
    fig7.update_layout(
        xaxis_title="Index",
        yaxis_title="Change Rate (%)"
    )
    st.plotly_chart(fig7, use_container_width=True)

df = load_predictions_df()

if df.empty:
    st.warning("No records found in the database.")
else:
    st.dataframe(df)



# زر الانتقال إلى صفحة عرض البيانات (Database Logs)
if st.button("📄 Go To Database Records", type="primary"):
    st.switch_page("pages/5_DatabaseView.py")


