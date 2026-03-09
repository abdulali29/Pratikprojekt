from datetime import datetime

def validate_records(data):
    validated = []

    for item in data:
        try:
            date = item.get("date")
            service = item.get("service")
            category = item.get("category")
            cost = float(item.get("cost", 0))

            if not date or not service:
                continue

            if cost < 0:
                continue

            # Azure gives ISO date like 2026-03-01T00:00:00Z
            clean_date = date[:10]
            datetime.strptime(clean_date, "%Y-%m-%d")

            validated.append({
                "date": clean_date,
                "service": service,
                "category": category,
                "cost": cost
            })

        except Exception:
            continue

    print(f"Validation complete: {len(validated)} valid records")
    return validated