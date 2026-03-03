import csv


# ---------------------------------------------------
# Function: validate_data
# Purpose: Validate CSV structure and data
# ---------------------------------------------------
def validate_data(csv_file):

    valid_rows = []
    invalid_rows = 0

    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                # Validate required fields
                if not row["date"] or not row["service"] or not row["category"] or not row["cost"]:
                    raise ValueError("Missing required field")

                # Validate cost is numeric
                float(row["cost"])

                valid_rows.append(row)

            except Exception:
                invalid_rows += 1

    print(f"Valid rows: {len(valid_rows)}")
    print(f"Invalid rows: {invalid_rows}")

    # Return original file (since it's already valid in this case)
    return csv_file
