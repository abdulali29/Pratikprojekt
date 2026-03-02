import sqlite3
import pandas as pd

# ---------------------------------------------------
# Function: load_data
# Purpose: Load cloud cost data from SQLite database
# ---------------------------------------------------
def load_data():
    # Connect to SQLite database
    conn = sqlite3.connect("cloud_costs.db")

    # Read entire cloud_costs table into a Pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM cloud_costs", conn)

    # Close database connection
    conn.close()

    # Return dataframe for further analysis
    return df


# ---------------------------------------------------
# Function: total_cost
# Purpose: Calculate total cloud spending
# ---------------------------------------------------
def total_cost(df):
    # Sum all cost values in the dataframe
    return df["cost"].sum()


# ---------------------------------------------------
# Function: cost_per_service
# Purpose: Aggregate cost grouped by cloud service
# ---------------------------------------------------
def cost_per_service(df):
    # Group by service and calculate total cost per service
    # Sort descending to identify most expensive service
    return df.groupby("service")["cost"].sum().sort_values(ascending=False)


# ---------------------------------------------------
# Function: cost_per_category
# Purpose: Aggregate cost grouped by category
# ---------------------------------------------------
def cost_per_category(df):
    # Group by category (Compute, Storage, etc.)
    return df.groupby("category")["cost"].sum().sort_values(ascending=False)


# ---------------------------------------------------
# Function: daily_change
# Purpose: Calculate percentage change day-to-day
# ---------------------------------------------------
# ---------------------------------------------------
# Function: daily_change
# Purpose: Calculate percentage change in daily cloud cost
# ---------------------------------------------------
def daily_change(df):

    # Convert date column from string to datetime format
    df["date"] = pd.to_datetime(df["date"])

    # Group by date and calculate total cost per day
    daily = df.groupby("date")["cost"].sum().sort_index()

    # Calculate percentage change between consecutive days
    # fillna(0) replaces NaN for the first day (no previous value to compare)
    daily_pct_change = daily.pct_change().fillna(0) * 100

    return daily_pct_change

# ---------------------------------------------------
# Function: detect_cost_spike
# Purpose: Identify abnormal increases or decreases
# ---------------------------------------------------
def detect_cost_spike(df, threshold=20):

    # Calculate daily percentage change
    daily_pct = daily_change(df).round(2)

    # Detect positive spikes (large increase)
    positive_spikes = daily_pct[daily_pct > threshold]

    # Detect negative spikes (large decrease)
    negative_spikes = daily_pct[daily_pct < -threshold]

    return positive_spikes, negative_spikes
