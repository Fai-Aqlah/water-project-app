import streamlit as st

def load_style():
    st.markdown("""
        <style>
        body {
            background: linear-gradient(to bottom right, #E3F2FD, #F1F8E9);
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 2.4em;
            font-weight: bold;
            color: #1565C0;
            margin-bottom: 0.3em;
        }
        .sub-title {
            text-align: center;
            font-size: 1.1em;
            color: #555;
            margin-bottom: 1.5em;
        }
        .stNumberInput label {
            font-weight: 600;
            color: #37474F;
        }
        .result-box {
            background: white;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            border-left: 6px solid #1E88E5;
            border-radius: 10px;
            padding: 20px;
            margin-top: 30px;
            font-weight: 600;
            text-align: center;
        }
        .stButton>button {
            background: linear-gradient(to right, #42A5F5, #1E88E5);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.1em;
            padding: 10px 30px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background: linear-gradient(to right, #1E88E5, #1565C0);
        }
        footer {
            text-align: center;
            font-size: 0.9em;
            color: #555;
            margin-top: 3em;
        }
        hr {
            border: none;
            border-top: 1px solid #ddd;
        }
        </style>
    """, unsafe_allow_html=True)
