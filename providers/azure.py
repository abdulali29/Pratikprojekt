import subprocess
import json
import logging
from providers.base_provider import BaseProvider


class AzureProvider(BaseProvider):

    def __init__(self):
        self.subscription_id = "df7bb429-79b5-41c2-828f-29b375942db5"

    def fetch_raw(self):
        """
        1️⃣ Fetch raw JSON from Azure CLI
        """
        command = [
            "az", "consumption", "usage", "list",
            "--subscription", self.subscription_id,
            "--output", "json"
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            logging.error("Azure CLI error:")
            logging.error(result.stderr)
            return []

        return json.loads(result.stdout)

    def map_columns(self, raw_data):
        """
        2️⃣ Map Azure fields to standardized format
        """
        standardized_data = []

        for item in raw_data:
            try:
                standardized_data.append({
                    "date": (item.get("usageStart") or "")[:10],
                    "service": item.get("meterCategory", "Unknown"),
                    "category": item.get("meterSubCategory", "General"),
                    "cost": float(item.get("pretaxCost", 0))
                })
            except Exception:
                continue

        return standardized_data

    def fetch(self):
        """
        3️⃣ Full Azure pipeline:
            - Fetch raw data
            - Map columns
            - Return standardized format
        """
        raw_data = self.fetch_raw()
        return self.map_columns(raw_data)