import streamlit as st

def load_style():
    st.markdown("""
        <style>
            body {
                background-color: #f8fafc;
            }
            .main-title {
                text-align: center;
                font-size: 2.2em;
                font-weight: bold;
                color: #1E88E5;
                margin-bottom: 0.2em;
            }
            .sub-title {
                text-align: center;
                font-size: 1.1em;
                color: #5f6368;
                margin-bottom: 1.5em;
            }
            .stNumberInput label {
                font-weight: 600;
                color: #37474F;
            }
            .result-box {
                text-align: center;
                padding: 20px;
                border-radius: 10px;
                margin-top: 20px;
                font-size: 1.1em;
            }
            .normal {
                background-color: #e8f5e9;
                color: #2e7d32;
                border: 1px solid #81c784;
            }
            .leak {
                background-color: #ffebee;
                color: #c62828;
                border: 1px solid #ef9a9a;
            }
            footer {
                text-align: center;
                font-size: 0.9em;
                color: #777;
                margin-top: 3em;
            }
        </style>
    """, unsafe_allow_html=True)

                
