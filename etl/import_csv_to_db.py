import sqlite3
import csv


# ---------------------------------------------------
# Function: import_to_db
# Purpose: Load validated CSV data into SQLite database
# ---------------------------------------------------
def import_to_db(csv_file):

    # Connect to SQLite database
    conn = sqlite3.connect("cloud_costs.db")
    cursor = conn.cursor()

    inserted_rows = 0

    # Open CSV file
    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            # Extract required fields from CSV
            date = row["date"]
            service = row["service"]
            category = row["category"]
            cost = float(row["cost"])

            # Handle cloud_provider safely
            # If column does not exist, default to "AWS"
            cloud_provider = row.get("cloud_provider", "AWS")

            # Insert into database
            # INSERT OR IGNORE prevents duplicate entries
            cursor.execute("""
                INSERT OR IGNORE INTO cloud_costs
                (date, service, category, cost, cloud_provider)
                VALUES (?, ?, ?, ?, ?)
            """, (date, service, category, cost, cloud_provider))

            # Count only rows that were actually inserted
            if cursor.rowcount > 0:
                inserted_rows += 1

    # Commit changes
    conn.commit()

    # Close database connection
    conn.close()

    print(f"{inserted_rows} new rows inserted into database.")
