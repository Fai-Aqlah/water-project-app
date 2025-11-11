
import streamlit as st

def load_style():
    st.markdown("""
    <style>

    /* ===== الخلفية العامة ===== */
    body {
        background: linear-gradient(to bottom, #ffffff, #f6fbff);
        font-family: 'Arial', sans-serif;
    }

    /* ===== العنوان الرئيسي ===== */
    .main-title {
        font-size: 40px;
        font-weight: 900;
        text-align: center;
        color: #0E4D64;
        margin-top: 5px;
        margin-bottom: 10px;
    }

    /* ===== العنوان الفرعي ===== */
    .sub-title {
        font-size: 21px;
        text-align: center;
        color: #333333;
        font-weight: 500;
        margin-bottom: 35px;
        line-height: 1.8;
    }

    /* ===== تحسين ترتيب الشعار والعنوان ===== */
    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    /* ===== الحقول ===== */
    .stNumberInput label {
        font-size: 18px;
        font-weight: 600;
        color: #0E4D64;
    }

    /* ===== الأزرار ===== */
    div.stButton > button {
        font-size: 18px;
        font-weight: 600;
        background-color: #1B83C0;
        color: white;
        border-radius: 8px;
        padding: 10px 28px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #145a86;
        transform: scale(1.05);
    }

    /* ===== النصوص الناتجة ===== */
    .stSuccess, .stInfo, .stWarning, .stError {
        font-size: 17px;
        font-weight: 500;
        line-height: 1.6;
    }

    /* ===== الفوتر ===== */
    footer {
    text-align: center;
    color: #0E4D64;
    font-size: 18px;
    font-weight: 600;
    margin-top: 80px;       /* رفع المسافة عن الأسفل */
    padding-bottom: 30px;   /* زيادة التباعد عن نهاية الصفحة */
    line-height: 1.6;       /* تباعد بسيط بين السطرين */
}

    }

    hr {
        border: 1px solid #ccc;
        margin-top: 50px;
        margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True)
