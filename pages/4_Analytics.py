import streamlit as st
import pandas as pd
import plotly.express as px

with open("pages/style_analytics.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📊 Water Analytics Dashboard")
st.write("Deep insights into water consumption & leakage behavior.")

df = pd.read_csv("water_data_clean.csv")

col1, col2, col3 = st.columns(3)
col1.metric("Avg Previous", round(df["previous_consumption"].mean(), 2))
col2.metric("Avg Current", round(df["current_consumption"].mean(), 2))
col3.metric("Leakage Count", int(df["leak_detected"].sum()))

st.divider()

tab1, tab2, tab3 = st.tabs(["📦 Distributions", "💧 Leakage Impact", "📈 Trends"])

with tab1:
    st.subheader("Distribution of Water Consumption")

    c1, c2 = st.columns(2)

    with c1:
        fig_prev = px.histogram(
            df,
            x="previous_consumption",
            nbins=30,
            title="Previous Consumption Distribution",
            color_discrete_sequence=["#4F8BD4"]
        )
        st.plotly_chart(fig_prev, use_container_width=True)

    with c2:
        fig_curr = px.histogram(
            df,
            x="current_consumption",
            nbins=30,
            title="Current Consumption Distribution",
            color_discrete_sequence=["#1D976C"]
        )
        st.plotly_chart(fig_curr, use_container_width=True)

with tab2:
    st.subheader("Leakage Effect on Consumption")

    fig_box = px.box(
        df,
        x="leak_detected",
        y="current_consumption",
        color="leak_detected",
        title="Consumption Levels: Leak vs No Leak",
        color_discrete_sequence=["#4F8BD4", "#D9534F"],
    )
    fig_box.update_layout(xaxis_title="Leak Detected (0 = No, 1 = Yes)")
    st.plotly_chart(fig_box, use_container_width=True)

    leak_rate = df["leak_detected"].mean() * 100
    st.metric("Leakage Percentage", f"{leak_rate:.2f}%")

with tab3:
    st.subheader("Consumption Trend Over Records")

    fig_line = px.line(
        df,
        y=["previous_consumption", "current_consumption"],
        title="Previous vs Current Consumption Trend",
        labels={"index": "Record Index"},
        color_discrete_sequence=["#4F8BD4", "#1D976C"]
    )
    st.plotly_chart(fig_line, use_container_width=True)

   
