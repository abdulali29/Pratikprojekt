import boto3
import csv
import logging


class AWSProvider:
    def __init__(self):
        self.bucket_name = "cloud-cost-report-2026"
        self.object_key = "reports/cloud_costs.csv"
        self.local_file = "aws_cloud_costs.csv"

    def fetch_file(self):
        """
        1️⃣ Download CSV from S3
        """
        s3 = boto3.client("s3")
        s3.download_file(self.bucket_name, self.object_key, self.local_file)
        logging.info("AWS cost CSV downloaded automatically.")
        return self.local_file

    def parse_csv(self, file_path):
        """
        2️⃣ Parse CSV
        """
        data = []
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data

    def map_columns(self, raw_data):
        """
        3️⃣ Map AWS-specific columns to standardized format
        """
        standardized_data = []

        for row in raw_data:
            standardized_data.append({
                "date": row.get("UsageDate"),
                "service": row.get("ServiceName"),
                "category": row.get("UsageType"),
                "cost": float(row.get("Cost", 0))
            })

        return standardized_data

    def fetch(self):
        """
        4️⃣ Full pipeline:
            - Download
            - Parse
            - Map
            - Return standardized format
        """
        file_path = self.fetch_file()
        raw_data = self.parse_csv(file_path)
        return self.map_columns(raw_data)