
import streamlit as st

def load_style():
    st.markdown("""
    <style>
    /*  الشريط العلوي  */
header {
    background-color: #2e8b57; /* الأخضر  */
    color: white;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    padding: 10px;
    border-radius: 0 0 10px 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

    /*  الأساسيات  */
    body {
        background: linear-gradient(to bottom, #f8fafc, #eaf6ff);
        font-family: 'Arial', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
       


    }

    /* العنوان الرئيسي */
.main-title {
    font-size: 42px;
    font-weight: 900;
    text-align: center;
    color: #0E4D64;
    margin-top: 20px;
    margin-bottom: 10px;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.2);
    animation: fadeInDown 1s ease-in-out, glowEffect 3s infinite ease-in-out;
}

/* 🌿 تأثير التوهّج الأخضر الناعم */
@keyframes glowEffect {
    0% { text-shadow: 1px 1px 4px rgba(0,0,0,0.2), 0 0 10px #81c784, 0 0 20px #a5d6a7; }
    50% { text-shadow: 1px 1px 4px rgba(0,0,0,0.2), 0 0 15px #a5d6a7, 0 0 30px #c8e6c9; }
    100% { text-shadow: 1px 1px 4px rgba(0,0,0,0.2), 0 0 10px #81c784, 0 0 20px #a5d6a7; }
}

/* الحركة الانسيابية للعنوان */
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}



    /*  العنوان الفرعي  */
    .sub-title {
        font-size: 16px;
        font-weight: 500;
        text-align: center;
        color: #333333;
        margin-bottom: 25px;
        line-height: 1.5;
    }

    /*  الشعار  */
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

    /*  مربعات الإدخال  */
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

    /*  الزر  */
    div.stButton > button {
    font-size: 19px;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #1B83C0, #20a4f3);
    border-radius: 10px;
    padding: 10px 35px;
    transition: 0.3s ease-in-out;
    border: none;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.2);
}
div.stButton > button:hover {
    background: linear-gradient(90deg, #156EA3, #1B83C0);
    transform: scale(1.06);
}


    /*  رسائل النتيجة  */
    .stSuccess, .stInfo, .stWarning, .stError {
        font-size: 17px;
        font-weight: 500;
        text-align: center;
        line-height: 1.6;
        .stSuccess { 
    background-color: #d4edda; 
    color: #155724; 
    border-radius: 8px; 
    padding: 10px; 
} 

.stWarning { 
    background-color: #fff3cd; 
    color: #856404; 
    border-radius: 8px; 
    padding: 10px; 
} 

.stError { 
    background-color: #f8d7da; 
    color: #721c24; 
    border-radius: 8px; 
    padding: 10px; 
}

    }

    /*  خط فاصل قبل الفوتر  */
    hr {
        border: 1px solid #B6E2D3;
        width: 80%;
        margin: 40px auto 20px auto;
    }

    /*  الفوتر  */
    footer {
    text-align: center;
    color: #2e8b57;
    font-size: 16px;
    font-weight: 600;
    margin-top: 40px;
    padding-top: 10px;
    border-top: 2px solid #b7dfc5;
    line-height: 1.8;
}


  section.main > div {
    padding-top: 10px;
}

    </style>
    """, unsafe_allow_html=True)
