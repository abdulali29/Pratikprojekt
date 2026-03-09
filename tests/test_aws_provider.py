from providers.aws import AWSProvider
from data.insert_data import insert_costs

provider = AWSProvider()

data = provider.fetch()

insert_costs(data)

print("Records inserted:", len(data))