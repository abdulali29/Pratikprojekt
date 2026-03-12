import pandas as pd

aws = pd.read_csv("data/aws_cost_report.csv")
aws["provider"] = "AWS"

azure = pd.read_csv("data/azure_cost_report.csv")
azure["provider"] = "Azure"

df = pd.concat([aws, azure], ignore_index=True)

df.to_csv("data/cloud_costs.csv", index=False)

print("Unified cloud dataset created")