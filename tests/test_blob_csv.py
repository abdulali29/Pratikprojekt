from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

# Azure connection string
connection_string = "DIN_CONNECTION_STRING"
container_name = "cost-exports"

# connect
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service_client.get_container_client(container_name)

print("Searching for CSV files...")

for blob in container_client.list_blobs():

    if blob.name.endswith(".csv"):

        print("Found CSV:", blob.name)

        blob_client = container_client.get_blob_client(blob)

        data = blob_client.download_blob().readall()

        df = pd.read_csv(io.BytesIO(data))

        print("CSV loaded successfully")
        print(df.head())

        break