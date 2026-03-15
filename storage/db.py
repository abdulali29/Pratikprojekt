import sqlite3

DB_NAME = "cloud_costs.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cloud_costs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        service TEXT,
        category TEXT,
        cost REAL
    )
    """)

    conn.commit()
    conn.close()


def save_costs(data):
    conn = get_connection()
    cursor = conn.cursor()

    for item in data:
        cursor.execute("""
        INSERT INTO cloud_costs (date, service, category, cost)
        VALUES (?, ?, ?, ?)
        """, (
            item.get("date"),
            item.get("service"),
            item.get("category"),
            item.get("cost")
        ))

    conn.commit()
    conn.close()

    print("Data inserted into database")