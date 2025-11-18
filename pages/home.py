import streamlit as st

# ---------- LOAD HOME CSS ----------
def load_home_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css("pages/style_home.css")

# ---------- PAGE CONTENT ----------
html_content = """
<div style='padding:30px;'>

    <div style='
        background:#ffffff;
        padding:30px;
        border-radius:20px;
        box-shadow:0 4px 15px rgba(0,0,0,0.1);
        margin-bottom:40px;
    '>
        <h1 style='color:#1b4d3e; text-align:center; font-size:42px;'>
            Smart Water System 💧🌿
        </h1>

        <p style='font-size:18px; color:#333; text-align:center; line-height:1.7;'>
            Smart Water System is an AI-powered platform designed to analyze water consumption 
            and detect potential leakages.<br><br>
            By comparing previous and current usage, the model identifies abnormal increases 
            that may indicate hidden water loss.<br><br>
            The system supports the Ministry of Environment, Water & Agriculture in improving 
            sustainability, reducing waste, and enabling smarter decision-making.
        </p>
    </div>

    <h2 style='color:#1b4d3e; font-size:32px; text-align:center; margin-bottom:20px;'>
        ⭐ Key Benefits
    </h2>

    <div style='display:flex; gap:20px; justify-content:center; flex-wrap:wrap;'>

        <div style='
            background:white;
            width:300px;
            padding:20px;
            border-radius:15px;
            border-left:6px solid #4da3ff;
            box-shadow:0px 3px 12px rgba(0,0,0,0.1);
        '>
            <h3 style='margin:0; color:#1b4d3e;'>🚰 Early Leakage Detection</h3>
            <p style='font-size:16px; color:#444;'>
                Detects abnormal usage instantly, allowing fast intervention.
            </p>
        </div>

        <div style='
            background:white;
            width:300px;
            padding:20px;
            border-radius:15px;
            border-left:6px solid #59c17a;
            box-shadow:0px 3px 12px rgba(0,0,0,0.1);
        '>
            <h3 style='margin:0; color:#1b4d3e;'>📊 Smart Consumption Management</h3>
            <p style='font-size:16px; color:#444;'>
                Provides accurate monthly consumption insights.
            </p>
        </div>

        <div style='
            background:white;
            width:300px;
            padding:20px;
            border-radius:15px;
            border-left:6px solid #00c7c7;
            box-shadow:0px 3px 12px rgba(0,0,0,0.1);
        '>
            <h3 style='margin:0; color:#1b4d3e;'>🌿 Environmental Sustainability</h3>
            <p style='font-size:16px; color:#444;'>
                Reduces water waste and supports national sustainability goals.
            </p>
        </div>

    </div>

</div>
"""

st.markdown(html_content, unsafe_allow_html=True)
