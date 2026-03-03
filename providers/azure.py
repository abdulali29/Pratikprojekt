import subprocess
import json

def fetch():
    subscription_id = "df7bb429-79b5-41c2-828f-29b375942db5"

    command = [
        "az", "consumption", "usage", "list",
        "--subscription", subscription_id,
        "--output", "json"
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("Azure CLI error:")
        print(result.stderr)
        return None

    data = json.loads(result.stdout)

    print("Azure data fetched successfully.")
    return data