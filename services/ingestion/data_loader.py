import sqlite3
import pandas as pd
from config import DATABASE_PATH


def load_cloud_costs():

    conn = sqlite3.connect(DATABASE_PATH)

    query = """
    SELECT
        date,
        service,
        category,
        cost
    FROM cloud_costs
    """

    df = pd.read_sql(query, conn)

    df["date"] = pd.to_datetime(df["date"])

    conn.close()

    return df