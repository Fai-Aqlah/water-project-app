import sqlite3
from datetime import datetime

# اسم ملف قاعدة البيانات
DB_NAME = "predictions.db"

def get_connection():
    """إنشاء اتصال بقاعدة البيانات"""
    return sqlite3.connect(DB_NAME)

def create_table():
    """إنشاء جدول لتخزين سجلات التنبؤ إذا ما كان موجود"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            previous REAL,
            current REAL,
            diff REAL,
            predicted_leak INTEGER,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_prediction(previous, current, diff, predicted_leak):
    """حفظ سجل جديد للتنبؤ داخل الجدول"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO prediction_logs (previous, current, diff, predicted_leak, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        previous,
        current,
        diff,
        predicted_leak,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()
