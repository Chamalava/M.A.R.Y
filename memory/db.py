import sqlite3
import time
from config.config import DB_PATH, MEMORY_LIMIT

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT,
            ts REAL
        )
    """)
    conn.commit()
    conn.close()

def save_memory(role, content):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO memory (role, content, ts) VALUES (?, ?, ?)",
        (role, content, time.time())
    )
    conn.commit()
    conn.close()

def load_memory(limit=MEMORY_LIMIT):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT role, content FROM memory ORDER BY id DESC LIMIT ?", (limit,)
    )
    rows = c.fetchall()
    conn.close()
    return rows[::-1]
