import sqlite3


def insert_costs(data):

    conn = sqlite3.connect("database/cloud_costs.db")
    cursor = conn.cursor()

    for row in data:
        cursor.execute(
            """
            INSERT INTO cloud_costs (date, service, category, cost)
            VALUES (?, ?, ?, ?)
            """,
            (row["date"], row["service"], row["category"], row["cost"])
        )

    conn.commit()
    conn.close()