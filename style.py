import streamlit as st

def load_custom_style():
    st.markdown("""
        <style>
            /*  Main App Background */
            .stApp {
                background-color: #F4F9FF;
                color: #000000;
            }

            /*  Main Title */
            h1 {
                color: #004E8F;
                text-align: center;
                font-size: 36px !important;
                font-weight: bold;
            }

            /*  Subheading */
            h3 {
                text-align: center;
                color: #0077B6;
                font-style: italic;
            }

            /*  Button Styling */
            div.stButton > button:first-child {
                background-color: #0077B6;
                color: white;
                border-radius: 10px;
                height: 3em;
                width: 100%;
                font-size: 18px;
                font-weight: bold;
                border: none;
                transition: 0.3s;
            }
            div.stButton > button:hover {
                background-color: #0096C7;
                color: #ffffff;
                transform: scale(1.02);
            }

            /*  Input Boxes */
            input {
                border: 2px solid #0096C7 !important;
                border-radius: 8px !important;
                background-color: #E9F5FF !important;
                padding: 6px !important;
                font-size: 16px !important;
            }

            /*  Alert Boxes */
            .stAlert {
                font-size: 18px !important;
                padding: 15px;
                border-radius: 10px;
            }

            /*  Sidebar Design */
            [data-testid="stSidebar"] {
                background-color: #E3F2FD;
                color: #003366;
            }
            [data-testid="stSidebar"] h2 {
                color: #004E8F;
                text-align: center;
                font-weight: bold;
            }
            [data-testid="stSidebar"] p {
                font-size: 15px;
                text-align: center;
            }

            /*  Divider Line */
            hr {
                border: 1px solid #0077B6;
                border-radius: 5px;
            }

            /*  Footer */
            footer {
                visibility: hidden;
            }
        </style>
    """, unsafe_allow_html=True)
