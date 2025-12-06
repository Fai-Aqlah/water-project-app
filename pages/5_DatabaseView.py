import streamlit as st
import pandas as pd
from database import load_predictions_df

st.set_page_config(page_title="Database Records", layout="wide")

st.title("📄 Prediction Records (Database Logs)")
st.markdown("هذه الصفحة تعرض السجلّات الفعلية المحفوظة داخل قاعدة البيانات بعد كل عملية تنبؤ 💧")

# ======================
# Load database data
# ======================
df = load_predictions_df()

if df.empty:
    st.warning("⚠️ لا توجد أي سجلات بعد. قومي بعمل تنبؤ واحد على الأقل.")
    st.stop()

# ======================
# Search & Filter Section
# ======================
st.subheader("🔎 البحث والفلترة")

col1, col2, col3 = st.columns(3)

# Filter by status
status_filter = col1.selectbox(
    "فلترة حسب حالة التنبؤ",
    options=["الكل", "Stable", "Warning", "Leak", "Normal", "Decrease", "Zero-Prev"],
    index=0
)

# Search by number
search_value = col2.text_input("ابحث بالقيمة (Previous / Current / Change Rate)")


# Apply filters
filtered_df = df.copy()

if status_filter != "الكل":
    filtered_df = filtered_df[filtered_df["status"] == status_filter]

if search_value:
    try:
        search_value_num = float(search_value)
        filtered_df = filtered_df[
            (filtered_df["previous"] == search_value_num) |
            (filtered_df["current"] == search_value_num) |
            (filtered_df["change_rate"] == search_value_num)
        ]
    except:
        st.info("اكتبي رقم صحيح للبحث.")

st.markdown("### 📋 السجلّات بعد الفلترة")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")

# ======================
# Download Section
# ======================
st.subheader("⬇️ تحميل السجلّات")

download_df = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=download_df,
    file_name="database_records.csv",
    mime="text/csv",
    use_container_width=True
)

st.markdown("---")

# ======================
# Summary Cards
# ======================
st.subheader("📦 إحصائيات سريعة")

colA, colB, colC, colD = st.columns(4)

colA.metric("Total Records", df.shape[0])
colB.metric("Leak Cases", df[df["status"] == "Leak"].shape[0])
colC.metric("Stable Cases", df[df["status"] == "Stable"].shape[0])
colD.metric("Warnings", df[df["status"] == "Warning"].shape[0])

st.success("✨ تم عرض بيانات الداتا بيز بنجاح!")
