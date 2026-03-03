from providers.azure import fetch
from database.db import insert_azure_data

def run_pipeline():
    print("Starting Azure pipeline...")

    data = fetch()

    if not data:
        print("No data fetched. Pipeline stopped.")
        return

    insert_azure_data(data)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()