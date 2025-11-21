import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# تحميل CSS
with open("pages/style_analytics.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# عنوان
st.title("📊 Water Analytics Dashboard")
st.markdown("### Insights into water consumption & leakage patterns")

# تحميل البيانات
df = pd.read_csv("water_data_clean.csv")

# --- الصناديق ---
col1, col2, col3 = st.columns(3)

col1.metric("Avg Previous", round(df["previous_consumption"].mean(), 2))
col2.metric("Avg Current", round(df["current_consumption"].mean(), 2))
col3.metric("Leakage Count", int(df["leak_detected"].sum()))

st.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs(["Distributions", "Leakage Analysis", "Trend"])

# ========== TAB 1 ==========
with tab1:
    st.subheader("Distribution of Consumption")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("**Previous Consumption**")
        fig1, ax1 = plt.subplots()
        sns.histplot(df["previous_consumption"], kde=True, ax=ax1)
        st.pyplot(fig1)

    with c2:
        st.markdown("**Current Consumption**")
        fig2, ax2 = plt.subplots()
        sns.histplot(df["current_consumption"], kde=True, ax=ax2)
        st.pyplot(fig2)

# ========== TAB 2 ==========
with tab2:
    st.subheader("Leakage vs Consumption")

    fig3, ax3 = plt.subplots()
    sns.boxplot(x=df["leak_detected"], y=df["current_consumption"], ax=ax3)
    ax3.set_xlabel("Leak Detected (0=No, 1=Yes)")
    ax3.set_ylabel("Current Consumption")
    st.pyplot(fig3)

    leak_rate = df["leak_detected"].mean() * 100
    st.metric("Leakage Percentage", f"{leak_rate:.2f}%")

# ========== TAB 3 ==========
with tab3:
    st.subheader("Consumption Trend by Index")

    fig4, ax4 = plt.subplots()
    ax4.plot(df.index, df["previous_consumption"], label="Previous")
    ax4.plot(df.index, df["current_consumption"], label="Current")
    ax4.set_xlabel("Data Index")
    ax4.set_ylabel("Consumption")
    ax4.legend()
    st.pyplot(fig4)



    
    

    
