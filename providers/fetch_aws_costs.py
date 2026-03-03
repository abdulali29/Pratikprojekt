import boto3  # AWS SDK for Python


# ---------------------------------------------------
# Function: fetch_data
# Purpose: Download AWS cost CSV file from S3
# ---------------------------------------------------
def fetch_data():

    # Create S3 client using configured IAM credentials
    s3 = boto3.client("s3")

    # S3 bucket name
    bucket_name = "cloud-cost-report-2026"

    # Path to CSV file inside the bucket
    object_key = "reports/cloud_costs.csv"

    # Local filename to save the downloaded CSV
    local_file = "cloud_costs.csv"

    # Download CSV file from S3
    s3.download_file(bucket_name, object_key, local_file)

    print("AWS cost CSV downloaded automatically.")

    # Return the local filename so pipeline can use it
    return local_file
