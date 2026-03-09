from providers.aws import AWSProvider
from data.insert_data import insert_costs


def run_pipeline():
    print("Starting cloud cost pipeline...")

    # Fetch AWS data
    aws_provider = AWSProvider()
    aws_data = aws_provider.fetch()

    print(f"AWS records fetched: {len(aws_data)}")

    # Insert into database
    insert_costs(aws_data)

    print("Data successfully stored in database.")


if __name__ == "__main__":
    run_pipeline()