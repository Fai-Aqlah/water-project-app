import streamlit as st
import numpy as np
from style import load_style


# إعداد جلسة المستخدم
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ========== صفحة تسجيل الدخول ==========
def login_page():
    st.title("🔐 Login Page")

    username = st.text_input("Enter username")
    password = st.text_input("Enter password", type="password")

    if st.button("Login"):
        if username == "Fai" and password == "1929837":
            st.success("Login successful 🎉")
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Wrong username or password ❌")


# ========== الصفحة الرئيسية بعد تسجيل الدخول ==========
def main_page():
    load_style()  # تحميل التنسيق إذا عندك style.py

    st.markdown("<header>Ministry of Environment, Water & Agriculture 🌿</header>", unsafe_allow_html=True)

    st.title("Smart Water Consumption Prediction 💧")

    prev = st.number_input("Enter previous consumption:", min_value=0.0)
    curr = st.number_input("Enter current consumption:", min_value=0.0)

    if st.button("Predict"):
        if curr > prev * 1.3:
            st.error("Leak Detected! 🚨")
        else:
            st.success("No Leak Detected ✔")


# ========== بدء التطبيق ==========
if st.session_state.logged_in:
    main_page()
else:
    login_page()



load_style()

st.markdown("<header>Ministry of Environment, Water & Agriculture 🌿</header>", unsafe_allow_html=True)


# Apply CSS style
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])  

with col2:  
    st.image("Green.jpg", width=550, use_column_width=False)


load_style()
st.markdown("<header>Ministry of Environment, Water & Agriculture 🌿</header>", unsafe_allow_html=True)



st.markdown("<div class='main-title'>Smart Water Consumption Prediction & Leak Detection 💧</div>", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
نظام مدعوم بالذكاء الاصطناعي لإدارة المياه الذكية ومنع التسريبات 💧<br>
<small><i>AI-powered system for smart water management and leak prevention</i></small>
</div>
""", unsafe_allow_html=True)

# القيم الإحصائية من البيانات (من التحليل بالكولاب)
low_threshold = 197.22
high_threshold = 482.60

# إدخال القيم من المستخدم
prev_use = st.number_input("Enter previous consumption:", min_value=0.0, step=0.1)
curr_use = st.number_input("Enter current consumption:", min_value=0.0, step=0.1)

# عند الضغط على زر التنبؤ
if st.button("🔍 Predict"):
    if prev_use == 0:
        st.warning("⚠️ Please enter a valid previous consumption value.")
    else:
    #  حساب نسبة التغير
       change_rate = ((curr_use - prev_use) / prev_use) * 100 if prev_use != 0 else 0

# ==== configurable thresholds ====
MEAN = 339.91
STD  = 142.69

LOW_MAX    = MEAN - STD      # 197.22
MED_MAX    = MEAN + STD      # 482.60

WARN_PCT   = 113.0           # بداية التحذير
LEAK_PCT   = 190.0           # تسريب فعلي
PCT_TOL    = 5.0             # تجاهل تغيّر أقل من 5%
ABS_TOL    = 10.0            # أو أقل من 10 لتر

# ==== compute features ====
change_rate = ((curr_use - prev_use) / prev_use) * 100 if prev_use != 0 else 0.0
abs_delta   = abs(curr_use - prev_use)

def level(x):
    if x < LOW_MAX: return "Low"
    if x <= MED_MAX: return "Medium"
    return "High"

prev_level = level(prev_use)
curr_level = level(curr_use)

# ==== decision logic ====
if prev_use == 0:
    st.info("ℹ️ Previous consumption is 0, change rate set to 0%.")
elif abs_delta < ABS_TOL or abs(change_rate) < PCT_TOL:
    st.success(f"✅ Stable usage (Δ={abs_delta:.0f} L, {change_rate:.1f}%). No action needed.")
else:
    if change_rate >= LEAK_PCT:
        st.error(f"🚨 Leak/Extreme overuse detected! +{change_rate:.1f}%. Check the system immediately.")
    elif change_rate >= WARN_PCT:
        st.warning(f"⚠️ High increase (+{change_rate:.1f}%). Please monitor usage.")
    elif change_rate <= -PCT_TOL:
        st.success(f"✅ Excellent! Usage decreased by {abs(change_rate):.1f}%.")
    else:
        st.success(f"✅ Normal change ({change_rate:.1f}%).")

st.markdown(f"**Previous Level:** {prev_level}  |  **Current Level:** {curr_level}")

# الفوتر
st.markdown("""
<hr style='margin-top:15px; margin-bottom:10px; border: 1px solid #4CAF50;'>

<div style='text-align:center; color:#156b3a; font-weight:bold; font-size:22px;'>
    Developed by <b style="color:#0277bd;">Fai Aqlah</b> | Ministry of Environment, Water & Agriculture 🌿💧 – Hail Branch
    <br>
    Powered by <b>XGBoost</b> & <b>Streamlit</b>
</div>
""", unsafe_allow_html=True)


