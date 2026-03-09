from providers.azure import AzureProvider

provider = AzureProvider()
data = provider.fetch()

print("Azure records fetched:", len(data))
print("Sample record:", data[:1])