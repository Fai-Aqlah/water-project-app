import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSS
with open("pages/style_analytics.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.title("📊 Water Analytics Dashboard")

# Load Data
df = pd.read_csv("water_data_clean.csv")

# ========== METRICS ==========
col1, col2, col3, col4 = st.columns(4)

avg_prev = df["previous_consumption"].mean()
avg_curr = df["current_consumption"].mean()
leaks = df["leak_detected"].sum()
diff = avg_curr - avg_prev

col1.metric("Avg Previous", f"{avg_prev:.2f}")
col2.metric("Avg Current", f"{avg_curr:.2f}")
col3.metric("Leakage Count", str(leaks))
col4.metric("Difference", f"{diff:.2f}")

st.divider()

# ========== TABS ==========
tab1, tab2, tab3, tab4 = st.tabs(
    ["📦 Distributions", "💧 Leakage Analysis", "🟦 Comparison", "📈 Trends"]
)

# ========== TAB 1: DISTRIBUTIONS ==========
with tab1:
    c1, c2 = st.columns(2)

    with c1:
        fig1 = px.histogram(
            df,
            x="previous_consumption",
            nbins=40,
            color_discrete_sequence=["#1f77b4"]
        )
        fig1.update_layout(xaxis_title="Previous Consumption", yaxis_title="Count")
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        fig2 = px.histogram(
            df,
            x="current_consumption",
            nbins=40,
            color_discrete_sequence=["#2ca02c"]
        )
        fig2.update_layout(xaxis_title="Current Consumption", yaxis_title="Count")
        st.plotly_chart(fig2, use_container_width=True)

# ========== TAB 2: LEAKAGE ==========
with tab2:
    fig3 = px.box(
        df,
        x="leak_detected",
        y="current_consumption",
        color="leak_detected",
        color_discrete_sequence=["#1f77b4", "#d62728"]
    )
    fig3.update_layout(
        xaxis_title="Leak Detected (0 = No, 1 = Yes)",
        yaxis_title="Current Consumption"
    )
    st.plotly_chart(fig3, use_container_width=True)

# ========== TAB 3: COMPARISON ==========
with tab3:
    fig4 = px.scatter(
        df,
        x="previous_consumption",
        y="current_consumption",
        color="leak_detected",
        color_discrete_sequence=["#1f77b4", "#d62728"]
    )
    fig4.update_layout(
        xaxis_title="Previous Consumption",
        yaxis_title="Current Consumption",
        legend_title="Leak Detected"
    )
    st.plotly_chart(fig4, use_container_width=True)

# ========== TAB 4: TRENDS ==========
with tab4:
    fig5 = px.line(
        df,
        y=["previous_consumption", "current_consumption"],
        color_discrete_sequence=["#1f77b4", "#2ca02c"]
    )
    fig5.update_layout(
        xaxis_title="Index",
        yaxis_title="Consumption",
        legend_title="Type"
    )
    st.plotly_chart(fig5, use_container_width=True)
