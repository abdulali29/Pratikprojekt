from database.connection import get_connection
from database.schema import create_table

def insert_azure_data(data):
    create_table()  # Ensure table exists

    conn = get_connection()
    cursor = conn.cursor()

    for item in data:
        cost = item.get("pretaxCost", 0)
        service = item.get("instanceName", "Unknown")

        cursor.execute("""
        INSERT INTO cloud_costs (service, cost)
        VALUES (?, ?)
        """, (service, float(cost)))

    conn.commit()
    conn.close()

    print("Azure data inserted into database.")