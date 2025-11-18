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

# ===================== IMPACT SECTION =====================

st.markdown(
    """
    <h2 style='text-align:center; color:#1b4d3e; font-size:38px; font-weight:900; margin-top:25px;'>
        How This System Helps the Ministry & Citizens 🌍💧
    </h2>
    """,
    unsafe_allow_html=True
)

impact_card = """
<div style="
    background:#f7fcff;
    width:92%;
    margin:25px auto;
    padding:30px;
    border-radius:18px;
    box-shadow:0 4px 15px rgba(0,0,0,0.1);
    border-left:12px solid #1b4d3e;
">

    <p style="font-size:18px; color:#333; line-height:1.9; text-align:justify;">
        The Smart Water System delivers real-world impact by enhancing the Ministry of Environment,
        Water & Agriculture’s ability to monitor water consumption with accuracy, detect hidden
        leakages early, and support national sustainability programs.  
        <br><br>
        For citizens, the system enables better understanding of consumption behavior, sends instant
        alerts when suspicious usage is detected, and helps reduce waste by providing AI-driven insights.
        This creates a smarter, more responsible, and highly efficient water management ecosystem for all.
    </p>

</div>
"""

st.markdown(impact_card, unsafe_allow_html=True)



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

