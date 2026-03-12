from database.connection import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cloud_costs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service TEXT,
        cost REAL
    )
    """)

    conn.commit()
    conn.close()