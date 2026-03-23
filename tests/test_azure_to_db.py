import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from providers.azure import AzureProvider
from storage.db import init_db, save_costs

print("Starting Azure → DB test...")

# start provider
azure = AzureProvider()

# hent CSV fra Azure Blob
df = azure.fetch_csv()

# parse data
data = azure.parse(df)

# opret database
init_db()

# gem data i database
save_costs(data)

print("Pipeline finished successfully")