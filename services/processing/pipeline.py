class Pipeline:

    def __init__(self, provider, db):
        self.provider = provider
        self.db = db

    def validate(self, data):
        valid_data = []

        for item in data:
            # Check required fields
            if item["date"] and item["cost"] is not None:
                valid_data.append(item)

        return valid_data

    def run(self, df):
        # 1. Transform data
        data = self.provider.transform(df)

        # 2. Validate & clean data
        data = self.validate(data)

        # 3. Save to database
        self.db.insert_data(data)

        print(f"Pipeline completed: {len(data)} rows inserted")