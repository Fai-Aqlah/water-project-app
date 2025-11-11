import streamlit as st

def load_style():
    st.markdown("""
        <style>

        /* الخلفية العامة */
        body {
            background-color: #f5f7fa;
            font-family: 'Segoe UI', sans-serif;
        }

        /* العنوان الرئيسي */
        .main-title {
            text-align: center;
            font-size: 2.4em;
            font-weight: bold;
            color: #0D47A1;
            margin-bottom: 0.2em;
        }

        /* العنوان الفرعي */
        .sub-title {
            text-align: center;
            font-size: 1.05em;
            color: #5f6368;
            margin-bottom: 1.8em;
        }

        /* مربعات الإدخال */
        .stNumberInput label {
            font-weight: 600;
            color: #37474F;
        }

        /* زر التنبؤ */
        .stButton>button {
            background-color: #1565C0;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: 600;
            padding: 10px 30px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0D47A1;
            transform: scale(1.05);
        }

        /* نتيجة التنبؤ */
        .result-box {
            background: #ffffff;
            border-left: 6px solid #1565C0;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
            border-radius: 10px;
            padding: 20px;
            margin-top: 30px;
            text-align: center;
            font-size: 1.1em;
            font-weight: 500;
            color: #2e7d32;
        }
        .leak {
            border-left: 6px solid #C62828;
            color: #C62828;
        }

        /* الفوتر */
        footer {
            text-align: center;
            font-size: 0.9em;
            color: #555;
            margin-top: 3em;
        }

        /* خط فاصل */
        hr {
            border: none;
            border-top: 1px solid #ddd;
            margin-top: 2em;
        }

        /* الشعار */
        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 90px;
            margin-bottom: 20px;
            opacity: 0.95;
        }

        </style>
    """, unsafe_allow_html=True)
