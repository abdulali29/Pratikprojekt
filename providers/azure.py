# ==========================================
# IMPORT LIBRARIES
# ==========================================

import subprocess
import json
import logging
from providers.base_provider import BaseProvider


# ==========================================
# AZURE PROVIDER CLASS
# Denne klasse håndterer hentning af
# cloud-omkostningsdata fra Azure
# ==========================================

class AzureProvider(BaseProvider):


    # ==========================================
    # INITIALIZE AZURE PROVIDER
    # Gemmer subscription ID
    # ==========================================
    def __init__(self):

        self.subscription_id = "df7bb429-79b5-41c2-828f-29b375942db5"


    # ==========================================
    # FETCH RAW DATA FROM AZURE
    # Bruger Azure CLI til at hente usage data
    # ==========================================
    def fetch_raw(self):

        command = [
            "az", "consumption", "usage", "list",
            "--subscription", self.subscription_id,
            "--output", "json"
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            raise Exception("Azure CLI error")

        return json.loads(result.stdout)


  # ==========================================
# PARSE AZURE DATA
# Konverterer Azure JSON data til et
# standard format for systemet
# ==========================================

def parse(self, data):

    parsed = []

    for item in data:

        parsed.append({
            "provider": "azure",
            "service": item.get("meterCategory", "unknown"),
            "resource": item.get("instanceName", "unknown"),
            "date": item.get("usageStart"),
            "cost": item.get("pretaxCost", 0)
        })

    return parsed

