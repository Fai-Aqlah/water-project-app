
import streamlit as st
import numpy as np

# إعداد الصفحة
st.set_page_config(page_title="💧 Smart Water Consumption & Leak Detection System", layout="centered")

st.title("💧 Smart Water Consumption Prediction & Leak Detection")
st.markdown("Using XGBoost for intelligent water monitoring 💡")

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
        # حساب نسبة التغير
        change_rate = ((curr_use - prev_use) / prev_use) * 100

        # تحديد مستويات الاستهلاك السابقة والحالية
        if prev_use <= low_threshold:
            prev_level = "Low"
        elif prev_use <= high_threshold:
            prev_level = "Medium"
        else:
            prev_level = "High"

        if curr_use <= low_threshold:
            curr_level = "Low"
        elif curr_use <= high_threshold:
            curr_level = "Medium"
        else:
            curr_level = "High"

        # منطق الكشف والتحليل
        if curr_use < prev_use:
            st.success(f"✅ Excellent! Water usage decreased by {abs(change_rate):.1f}%. Great efficiency!")
        elif curr_use > prev_use:
            if change_rate > 10:
                st.error(f"❌ Leak or Overuse Detected! Water usage increased by {change_rate:.1f}%. Please check the system.")
            else:
                st.warning(f"⚠️ Slight increase ({change_rate:.1f}%). Keep monitoring your consumption.")
        else:
            # حالة التساوي تمامًا
            if curr_use <= low_threshold:
                st.info(f"ℹ️ Constant low usage detected ({curr_use:.1f} L). Stable and efficient.")
            elif curr_use <= high_threshold:
                st.info(f"ℹ️ Constant medium usage detected ({curr_use:.1f} L). Normal operation.")
            else:
                st.warning(f"⚠️ High constant consumption detected ({curr_use:.1f} L). Try to reduce usage.")

        # عرض مستوى الاستهلاك الحالي والسابق
        st.markdown(f"**Previous Level:** {prev_level} | **Current Level:** {curr_level}")

# الفوتر
st.markdown("---")
st.caption("Developed by Fai Alshamary | Powered by XGBoost & Streamlit ✨")


