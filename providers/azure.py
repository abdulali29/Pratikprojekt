# ==========================================
# IMPORT LIBRARIES
# ==========================================

from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
from providers.base_provider import BaseProvider


# ==========================================
# AZURE PROVIDER CLASS
# Henter og parser Azure cost data
# ==========================================

class AzureProvider(BaseProvider):

    def __init__(self):

        # Azure Blob Storage connection
        self.connection_string = "DIN_CONNECTION_STRING"
        self.container_name = "cost-exports"

        self.blob_service = BlobServiceClient.from_connection_string(
            self.connection_string
        )

    # ==========================================
    # FETCH CSV FROM AZURE BLOB STORAGE
    # ==========================================
    def fetch_csv(self):

        container_client = self.blob_service.get_container_client(
            self.container_name
        )

        for blob in container_client.list_blobs():

            if blob.name.endswith(".csv"):

                print("Found CSV:", blob.name)

                blob_client = container_client.get_blob_client(blob)

                data = blob_client.download_blob().readall()

                df = pd.read_csv(io.BytesIO(data))

                print("CSV loaded successfully")

                return df

    # ==========================================
    # PARSE DATA
    # Konverterer CSV til systemets format
    # ==========================================
    def parse(self, df):

        data = []

        for _, row in df.iterrows():

            data.append({
                "date": row.get("usageStart"),
                "service": row.get("meterCategory"),
                "category": row.get("meterSubCategory"),
                "cost": row.get("pretaxCost", 0)
            })

        return data