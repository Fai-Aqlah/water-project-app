import sqlite3
from datetime import datetime

DB_NAME = "predictions.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def reset_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS prediction_logs")
    conn.commit()
    conn.close()


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


def load_predictions_df():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prediction_logs ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    import pandas as pd
    df = pd.DataFrame(rows, columns=[
        "id", "previous", "current", "diff", "change_rate", "status", "created_at"
    ])
    return df

  
