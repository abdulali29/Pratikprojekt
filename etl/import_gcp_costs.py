import pandas as pd
import sqlite3

# path to CSV
csv_path = "data/cloud_costs.csv"

# path to database
db_path = "database/cloud_costs.db"

# load CSV
df = pd.read_csv(csv_path)

print("Data loaded:")
print(df)

# connect database
conn = sqlite3.connect(db_path)

# save data
df.to_sql("cloud_costs", conn, if_exists="replace", index=False)

print("Data imported to database")