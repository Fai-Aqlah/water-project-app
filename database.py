import sqlite3
from datetime import datetime

# --------------------------
# 1) اتصال دائم بالقاعدة
# --------------------------
def get_connection():
    # يخزن قاعدة البيانات في ملف دائم database.db
    conn = sqlite3.connect("database.db", check_same_thread=False)
    return conn


# --------------------------
# 2) إنشاء الجدول (مرة وحدة فقط)
# --------------------------
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            previous REAL,
            current REAL,
            diff REAL,
            change_rate REAL,
            status TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


# --------------------------
# 3) حفظ التنبؤ داخل قاعدة البيانات
# --------------------------
def save_prediction(previous, current, diff, change_rate, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO prediction_logs (previous, current, diff, change_rate, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        previous,
        current,
        diff,
        change_rate,
        status,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


# --------------------------
# 4) جلب كل السجلات لصفحة DatabaseView
# --------------------------
def get_all_records():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM prediction_logs ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows


# --------------------------
# 5) حذف كل السجلات (إن احتجتي)
# --------------------------
def clear_records():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM prediction_logs")

    conn.commit()
    conn.close()

   

   
