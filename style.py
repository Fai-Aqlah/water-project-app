
import streamlit as st

def load_style():
    st.markdown("""
    <style>

    /* ===== الأساسيات ===== */
    body {
        background: linear-gradient(to bottom, #f8fafc, #eaf6ff);
        font-family: 'Arial', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
    }

    /* ===== العنوان الرئيسي ===== */
    .main-title {
        font-size: 42px;
        font-weight: 900;
        text-align: center;
        color: #0E4D64;
        margin-top: 20px;
        margin-bottom: 10px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.2); /* ✨ ظل أنيق تحت العنوان */
    }

    /* ===== العنوان الفرعي ===== */
    .sub-title {
        font-size: 16px;
        font-weight: 500;
        text-align: center;
        color: #333333;
        margin-bottom: 25px;
        line-height: 1.5;
    }

    /* ===== الشعار ===== */
    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 5px;
        margin-bottom: 15px;
        width: 90px;
        border-radius: 8px;
        box-shadow: 0px 1px 5px rgba(0,0,0,0.15);
    }

    /* ===== مربعات الإدخال ===== */
    .stNumberInput label {
        font-size: 18px;
        font-weight: 600;
        color: #0E4D64;
    }

    .stNumberInput input {
        border: 1px solid #d1e7dd;
        border-radius: 8px;
        background-color: #f8fffa;
        box-shadow: 0px 1px 4px rgba(0,0,0,0.08);
    }

    /* ===== الزر ===== */
    div.stButton > button {
        font-size: 18px;
        font-weight: 600;
        color: white;
        background-color: #1B83C0;
        border-radius: 10px;
        padding: 10px 30px;
        transition: 0.3s ease-in-out;
        border: none;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
    }

    div.stButton > button:hover {
        background-color: #156EA3;
        transform: scale(1.05);
    }

    /* ===== رسائل النتيجة ===== */
    .stSuccess, .stInfo, .stWarning, .stError {
        font-size: 17px;
        font-weight: 500;
        text-align: center;
        line-height: 1.6;
    }

    /* ===== خط فاصل قبل الفوتر ===== */
    hr {
        border: 1px solid #B6E2D3;
        width: 80%;
        margin: 40px auto 20px auto;
    }

    /* ===== الفوتر ===== */
    footer {
    text-align: center;
    color: #2e8b57; /* 💚 أخضر فاتح جميل */
    font-size: 17px;
    font-weight: 600;
    margin-top: 30px;
    padding-bottom: 10px;
    line-height: 1.6;
    position: relative;
    bottom: 40px;
    opacity: 0.95;
}


    </style>
    """, unsafe_allow_html=True)
