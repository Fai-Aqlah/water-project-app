import streamlit as st
import numpy as np
from style import load_style
import requests
import os
from database import save_prediction   # مهم

# ============================================================
#  EMAIL ALERT FUNCTION
# ============================================================
RESEND_API_KEY = os.environ.get("RESEND_API_KEY")

def send_email_alert(consumption_value, change_rate):
    url = "https://api.resend.com/emails"
    payload = {
        "from": "Smart Water System <alerts@resend.dev>",
        "to": ["faialahmary@gmail.com"],
        "subject": "🚨 Water Leakage Alert Detected!",
        "html": f"""
            <h2>🚨 Leakage / Extreme Overuse Detected</h2>
            <p><b>Current Consumption:</b> {consumption_value} L</p>
            <p><b>Change Rate:</b> +{change_rate:.1f}%</p>
            <p>Please check the system immediately.</p>
        """
    }
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code


# ============================================================
#  LOGIN CHECK
# ============================================================
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("🚫 You must log in first from the Login page.")
    st.stop()

st.markdown(f"""
    <h2 style="color:#1b4d3e; font-size:40px; margin-top:10px;">
        Welcome, {st.session_state.username}! 💧
    </h2>
""", unsafe_allow_html=True)

if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()


# ============================================================
#  STYLE
# ============================================================
load_style()
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<header>Ministry of Environment, Water & Agriculture 🌿</header>", unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])
with col2:
    st.image("Green.jpg", width=550, use_column_width=False)

st.markdown("<div class='main-title'>Smart Water Consumption Prediction & Leak Detection 💧</div>", unsafe_allow_html=True)
st.markdown("""
<div class='sub-title'>
نظام مدعوم بالذكاء الاصطناعي لإدارة المياه الذكية ومنع التسريبات 💧<br>
<small><i>AI-powered system for smart water management and leak prevention</i></small>
</div>
""", unsafe_allow_html=True)


# ============================================================
#  THRESHOLDS
# ============================================================
MEAN = 339.91
STD  = 142.69
LOW_MAX = MEAN - STD
MED_MAX = MEAN + STD

WARN_PCT = 113.0
LEAK_PCT = 190.0
PCT_TOL  = 5.0
ABS_TOL  = 10.0


# ============================================================
#  INPUTS
# ============================================================
prev_use = st.number_input("Enter previous consumption:", min_value=0.0, step=0.1)
curr_use = st.number_input("Enter current consumption:", min_value=0.0, step=0.1)

predict_btn = st.button("🔍 Predict")

# ============================================================
#  منع تكرار حفظ السجل (مهم جداً)
# ============================================================
if "saved_once" not in st.session_state:
    st.session_state.saved_once = False


# ============================================================
#  PREDICTION LOGIC
# ============================================================
if predict_btn:

    # إعادة التهيئة لكل عملية تنبؤ جديدة
    st.session_state.saved_once = False

    if prev_use <= 0:
        st.error("⚠️ Previous consumption must be greater than 0.")

    diff = curr_use - prev_use
    change_rate = (diff / prev_use) * 100

    def level(x):
        if x < LOW_MAX: return "Low"
        if x <= MED_MAX: return "Medium"
        return "High"

    prev_level = level(prev_use)
    curr_level = level(curr_use)

    # == Stable ==
    if abs(diff) < ABS_TOL or abs(change_rate) < PCT_TOL:
        st.success(f"✅ Stable usage (Δ={diff:.0f} L, {change_rate:.1f}%). No action needed.")
        if not st.session_state.saved_once:
            save_prediction(prev_use, curr_use, diff, change_rate, "Stable")
            st.session_state.saved_once = True

    else:
        # == Leak ==
        if change_rate >= LEAK_PCT:
            st.error(f"🚨 Leak/Extreme overuse detected! +{change_rate:.1f}%. Check the system immediately.")
            send_email_alert(curr_use, change_rate)
            st.info("📧 Alert email has been sent.")
            if not st.session_state.saved_once:
                save_prediction(prev_use, curr_use, diff, change_rate, "Leak")
                st.session_state.saved_once = True

        # == Warning ==
        elif change_rate >= WARN_PCT:
            st.warning(f"⚠️ High increase (+{change_rate:.1f}%). Please monitor usage.")
            if not st.session_state.saved_once:
                save_prediction(prev_use, curr_use, diff, change_rate, "Warning")
                st.session_state.saved_once = True

        # == Decrease ==
        elif change_rate <= -PCT_TOL:
            st.success(f"✅ Excellent! Usage decreased by {abs(change_rate):.1f}%.")
            if not st.session_state.saved_once:
                save_prediction(prev_use, curr_use, diff, change_rate, "Decrease")
                st.session_state.saved_once = True

        # == Normal ==
        else:
            st.success(f"✅ Normal change ({change_rate:.1f}%).")
            if not st.session_state.saved_once:
                save_prediction(prev_use, curr_use, diff, change_rate, "Normal")
                st.session_state.saved_once = True

    st.markdown(f"**Previous Level:** {prev_level} | **Current Level:** {curr_level}")

    colA, colB, colC = st.columns([1, 2, 1])
    with colB:
        if st.button("📊 Go To Analytics Page", use_container_width=True):
            st.switch_page("pages/4_Analytics.py")









