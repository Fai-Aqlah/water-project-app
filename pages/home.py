import streamlit as st

# --- LOAD CSS ---
def load_home_css():
    with open("pages/style_home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_home_css()


# تنسيق خاص بصفحة الهوم (CSS داخلي)
st.markdown(
    """
    <style>
        .main {
            background-color: #f5fafc;
        }

        .hero-card {
            max-width: 900px;
            margin: 40px auto 10px auto;
            padding: 30px 40px;
            border-radius: 24px;
            background: #ffffff;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
            text-align: center;
        }

        .hero-title {
            font-size: 42px;
            font-weight: 900;
            color: #1b4d3e;
            margin-bottom: 8px;
        }

        .hero-subtitle {
            font-size: 18px;
            font-weight: 600;
            color: #2f7c9c;
            margin-bottom: 18px;
        }

        .hero-text {
            font-size: 16px;
            line-height: 1.7;
            color: #333333;
        }

        .section-title {
            text-align: center;
            margin-top: 40px;
            margin-bottom: 20px;
            font-size: 28px;
            font-weight: 800;
            color: #1b4d3e;
        }

        .benefits-container {
            max-width: 950px;
            margin: 0 auto 40px auto;
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
        }

        .benefit-card {
            background: #ffffff;
            border-radius: 20px;
            padding: 18px 20px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.06);
        }

        .benefit-card h3 {
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 8px;
        }

        .benefit-card p {
            font-size: 14px;
            line-height: 1.6;
            color: #444444;
            margin: 0;
        }

        .blue-border {
            border-left: 5px solid #3ba4e6;
        }

        .green-border {
            border-left: 5px solid #3cb371;
        }

        .aqua-border {
            border-left: 5px solid #00c2ba;
        }

        .center-button {
            text-align: center;
            margin: 20px 0 10px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# اسم المستخدم لو كان مسجل دخول
username = st.session_state.get("username", "User")

# بطاقة التعريف بالمشروع
st.markdown(
    f"""
    <div class="hero-card">
        <h1 class="hero-title">Smart Water System 💧🌿</h1>
        <p class="hero-subtitle">
            AI-Powered Leakage Detection & Consumption Analysis
        </p>
        <p class="hero-text">
            Smart Water System is an AI-powered platform designed to analyze water consumption
            and detect potential leakage early. By comparing previous and current usage,
            the model identifies abnormal increases that may indicate hidden water loss.
            This helps the Ministry of Environment, Water & Agriculture make smarter,
            data-driven decisions, enhancing monitoring accuracy and reducing water waste.
            <br><br>
            Welcome, <b>{username}</b> — this Home page gives you a quick overview before
            you move to the prediction page.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# قسم الفوائد
st.markdown(
    """
    <h2 class="section-title">⭐ Key Benefits</h2>

    <div class="benefits-container">

        <div class="benefit-card blue-border">
            <h3>💧 Early Leakage Detection</h3>
            <p>
                Detects abnormal water usage instantly, allowing early intervention
                before significant water loss occurs.
            </p>
        </div>

        <div class="benefit-card green-border">
            <h3>📊 Smarter Consumption Management</h3>
            <p>
                Provides accurate monthly consumption analysis, improving awareness
                and reducing unnecessary usage.
            </p>
        </div>

        <div class="benefit-card aqua-border">
            <h3>🌿 Environmental Sustainability</h3>
            <p>
                Supports sustainability goals by minimizing waste and enabling
                better planning of water resources.
            </p>
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# زر الذهاب لصفحة التنبؤ (app)
with st.container():
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    go = st.button("Go to Prediction Page 🚰")
    st.markdown("</div>", unsafe_allow_html=True)

if go:
    st.switch_page("app")




