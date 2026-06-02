import sqlite3

conn = sqlite3.connect("credit_risk.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age REAL,
    debt_ratio REAL,
    monthly_income REAL,
    dependents REAL,
    risk_score REAL,
    risk_level TEXT,
    decision TEXT
)
""")

conn.commit()