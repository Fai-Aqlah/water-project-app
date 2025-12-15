import sqlite3
from datetime import datetime
import pytz

DB_NAME = "predictions.db"

# ============================================================
#  CREATE TABLE
# ============================================================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prev_use REAL,
            curr_use REAL,
            diff REAL,
            change_rate REAL,
            result TEXT,
            timestamp TEXT
        )
    """)
    
    conn.commit()
    conn.close()


#  SAVE PREDICTION
def save_prediction(prev_use, curr_use, diff, change_rate, result):

    # Reject zero or negative values (not allowed in your model logic)
    if prev_use <= 0 or curr_use <= 0:
        print("❌ Invalid values: zero or negative inputs are not allowed.")
        return

    # Saudi time
    sa_tz = pytz.timezone("Asia/Riyadh")
    timestamp = datetime.now(sa_tz).strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions (prev_use, curr_use, diff, change_rate, result, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (prev_use, curr_use, diff, change_rate, result, timestamp))

    conn.commit()
    conn.close()


# ============================================================
#  LOAD ALL RECORDS
# ============================================================
def load_predictions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, prev_use, curr_use, diff, change_rate, result, timestamp
        FROM predictions
        ORDER BY id DESC
    """)

    data = cursor.fetchall()
    conn.close()
    return data


# Initialize DB on import
init_db()

       
  







    
    
