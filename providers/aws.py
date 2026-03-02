import boto3

def fetch():

    s3 = boto3.client("s3")

    bucket_name = "cloud-cost-report-2026"
    object_key = "reports/cloud_costs.csv"
    local_file = "cloud_costs.csv"

    s3.download_file(bucket_name, object_key, local_file)

    print("AWS cost CSV downloaded automatically.")

    return local_file
