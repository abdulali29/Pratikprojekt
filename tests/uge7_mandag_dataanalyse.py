# uge7_cloud_cost_analysis.py
# Purpose: Perform full analysis of cloud_costs database

import sqlite3


def analyze_cloud_costs():
    # Connect to SQLite database
    conn = sqlite3.connect("cloud_costs.db")
    cursor = conn.cursor()

    print("===== CLOUD COST ANALYSIS =====\n")

    # 1️⃣ Total cost overall
    cursor.execute("SELECT SUM(cost) FROM cloud_costs;")
    total_cost = cursor.fetchone()[0]
    print(f"Total overall cloud cost: {total_cost}\n")

    # 2️⃣ Total cost per service
    print("Total cost per service:")
    cursor.execute("""
        SELECT service, SUM(cost)
        FROM cloud_costs
        GROUP BY service
        ORDER BY SUM(cost) DESC;
    """)

    services = cursor.fetchall()

    for service, cost in services:
        print(f" - {service}: {cost}")

    print()

    # 3️⃣ Total cost per month
    print("Total cost per month:")
    cursor.execute("""
        SELECT 
            strftime('%Y-%m', date) AS month,
            SUM(cost)
        FROM cloud_costs
        GROUP BY month
        ORDER BY month;
    """)

    months = cursor.fetchall()

    for month, cost in months:
        print(f" - {month}: {cost}")

    print()

    # 4️⃣ Find most expensive service
    most_expensive = services[0][0]
    print(f"Most expensive service: {most_expensive}\n")

    # 5️⃣ Average cost value
    cursor.execute("SELECT AVG(cost) FROM cloud_costs;")
    avg_cost = cursor.fetchone()[0]
    print(f"Average individual cost entry: {round(avg_cost, 2)}")

    conn.close()


if __name__ == "__main__":
    analyze_cloud_costs()
