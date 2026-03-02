# Importerer AWS' officielle Python-SDK (bruges til at kalde AWS API'er)
import boto3

# Importerer csv-modulet til læsning af CSV-filer
import csv

# Importerer sqlite3 til at arbejde med SQLite-databasen
import sqlite3


# -------------------- AWS S3: HENT CSV --------------------

# Opretter forbindelse til AWS S3 via API
s3 = boto3.client("s3")

# Navn på S3-bucket hvor AWS Cost & Usage Report ligger
bucket_name = "my-cost-report-bucket"

# Sti til CSV-filen i S3-bucketten
object_key = "reports/cloud_costs.csv"

# Lokalt filnavn hvor CSV-filen gemmes efter download
local_file = "cloud_costs.csv"

# Downloader CSV-filen automatisk fra AWS S3 til lokal mappe
s3.download_file(bucket_name, object_key, local_file)

# Bekræfter at CSV-filen er hentet korrekt
print("CSV downloaded automatically from AWS S3.")


# -------------------- DATABASE: INDSÆT DATA --------------------

# Opretter forbindelse til SQLite-databasen
conn = sqlite3.connect("cloud_costs.db")

# Opretter en cursor til at udføre SQL-kommandoer
cursor = conn.cursor()

# Åbner den hentede CSV-fil
with open(local_file, newline="", encoding="utf-8") as csvfile:
    
    # Læser CSV-filen som dictionaries baseret på kolonnenavne
    reader = csv.DictReader(csvfile)

    # Gennemløber hver række i CSV-filen
    for row in reader:

        # Indsætter data struktureret i cloud_costs-tabellen
        cursor.execute(
            """
            INSERT INTO cloud_costs (date, service, category, cost)
            VALUES (?, ?, ?, ?)
            """,
            (
                row["date"],               # Dato for omkostningen
                row["service"],            # Cloud-service
                row["category"],           # Type af omkostning
                float(row["cost"])         # Omkostning konverteret til tal
            )
        )

# Gemmer ændringer i databasen
conn.commit()

# Lukker forbindelsen til databasen
conn.close()

# Bekræfter at data er valideret og indsat korrekt
print("CSV data validated and inserted into SQLite database.")
