import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align:center; color:#1b4d3e; font-weight:900;'>
        Smart Water System 💧🌿
    </h1>
    <h3 style='text-align:center; color:#4a4a4a; margin-top:-10px;'>
        AI-Powered Leakage Detection & Consumption Analysis
    </h3>
    """,
    unsafe_allow_html=True
)

st.write("")  
st.write("")

# --------------- INTRO CARD ---------------
with st.container():
    st.markdown(
        """
        <div style="background:#f0f8ff; padding:25px; border-radius:15px; box-shadow:0px 4px 12px rgba(0,0,0,0.08);">
            <p style="font-size:18px; color:#333; text-align:center; line-height:1.7;">
                Smart Water System is an AI-powered platform developed to analyze water consumption,<br>
                detect potential leakages early, and support sustainability efforts.<br>
                By comparing previous and current usage, the system identifies unusual patterns<br>
                that may indicate hidden water loss.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")

# ------------- BENEFITS SECTION -------------
st.markdown(
    "<h2 style='text-align:center; color:#1b4d3e;'>⭐ Key Benefits</h2>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown(
        """
        <div style="background:white; padding:20px; border-radius:15px; 
        border-left:6px solid #4cb5ff; box-shadow:0 4px 12px rgba(0,0,0,0.08); text-align:center;">
            <h3 style="color:#1b4d3e;">💦 Early Leakage Detection</h3>
            <p style="color:#444; font-size:16px;">Detects abnormal usage instantly to prevent costly water loss.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="background:white; padding:20px; border-radius:15px; 
        border-left:6px solid #34c759; box-shadow:0 4px 12px rgba(0,0,0,0.08); text-align:center;">
            <h3 style="color:#1b4d3e;">📊 Smarter Consumption</h3>
            <p style="color:#444; font-size:16px;">Provides accurate monthly analysis for better awareness.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div style="background:white; padding:20px; border-radius:15px; 
        border-left:6px solid #00c2a8; box-shadow:0 4px 12px rgba(0,0,0,0.08); text-align:center;">
            <h3 style="color:#1b4d3e;">🌿 Sustainability</h3>
            <p style="color:#444; font-size:16px;">Supports efficient usage & national conservation goals.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")

# ------------------- BUTTON -------------------
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='text-align:center; color:#1b4d3e;'>Ready to explore the prediction model? 🚀</h3>",
    unsafe_allow_html=True
)

center = st.columns(3)[1]  # زر بالوسط

with center:
    go = st.button("Go to Prediction Page 👉", use_container_width=True)

if go:
    st.switch_page("app.py")

