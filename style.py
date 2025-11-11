import streamlit as st

def load_style():
    st.markdown("""
        <style>

        /* الخلفية العامة */
        body {
            background-color: #f5f7fa;
            font-family: 'Segoe UI', sans-serif;
        }
/* ===== تعديل أحجام النصوص والتباعد ===== */

/* العنوان الرئيسي */
.main-title {
    font-size: 38px;         /* حجم كبير وواضح */
    font-weight: 900;        /* سمك الخط */
    text-align: center;
    color: #0E4D64;          /* أزرق رسمي */
    margin-top: 10px;
    margin-bottom: 5px;
}

/* العنوان الفرعي (العربي + الإنجليزي) */
.sub-title {
    font-size: 20px;
    text-align: center;
    color: #333333;
    font-weight: 500;
    margin-bottom: 30px;
    line-height: 1.6;
}

/* النصوص الداخلية */
.stTextInput label, .stNumberInput label {
    font-size: 18px;
    font-weight: 600;
    color: #0E4D64;
}

/* الأزرار */
div.stButton > button {
    font-size: 18px;
    font-weight: 600;
    background-color: #1B83C0;
    color: white;
    border-radius: 8px;
    padding: 10px 30px;
}

/* نتائج التنبؤ */
.stSuccess, .stInfo, .stWarning {
    font-size: 17px;
    font-weight: 500;
}

        
           
