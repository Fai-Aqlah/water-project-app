import streamlit as st

def load_analytics_style():
    st.markdown(
    """
    <style>

    /* Main title */
    .css-10trblm {
        color: #0E96A8 !important;
        font-size: 42px !important;
        font-weight: 900 !important;
        text-align: center !important;
    }

    /* Section subtitles */
    h3 {
        color: #127C99 !important;
        margin-top: 30px;
        font-weight: 700 !important;
    }

    /* Metrics boxes */
    [data-testid="stMetricValue"] {
        color: #006D77 !important;
        font-weight: 800 !important;
        font-size: 26px !important;
    }

    [data-testid="stMetricLabel"] {
        color: #40E0D0 !important;
        font-size: 14px !important;
    }

    /* Body text */
    .css-1q8dd3e {
        color: #06474F !important;
        font-size: 18px;
    }

    </style>
    """,
    unsafe_allow_html=True
    )
