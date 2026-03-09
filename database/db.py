import sqlite3

def insert_azure_data(data):
    conn = sqlite3.connect("database/cloud_costs.db")
    cursor = conn.cursor()

    for record in data:
        cursor.execute("""
            INSERT INTO cloud_costs (date, service, category, cost)
            VALUES (?, ?, ?, ?)
        """, (
            record["date"],
            record["service"],
            record["category"],
            record["cost"]
        ))

    conn.commit()
    conn.close()