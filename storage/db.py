import sqlite3

DB_NAME = "cloud_costs.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS costs (
        provider TEXT,
        service TEXT,
        resource TEXT,
        date TEXT,
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
        INSERT INTO costs (provider, service, resource, date, cost)
        VALUES (?, ?, ?, ?, ?)
        """, (
            item["provider"],
            item["service"],
            item["resource"],
            item["date"],
            item["cost"]
        ))

    conn.commit()
    conn.close()