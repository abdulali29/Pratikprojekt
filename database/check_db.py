from analytics import load_data, daily_change, detect_cost_spike

def main():

    df = load_data()

    print("All data:")
    print(df)

    print("\nDaily Percentage Change:")
    pct = daily_change(df).round(2)
    print(pct)

    print("\nCost Spike Detection (>20% change):")

    pos_spikes, neg_spikes = detect_cost_spike(df, threshold=20)

    if pos_spikes.empty and neg_spikes.empty:
        print("No abnormal cost changes detected.")
    else:
        if not pos_spikes.empty:
            print("\n⚠ Positive Spike Detected:")
            print(pos_spikes)

        if not neg_spikes.empty:
            print("\n⚠ Negative Spike Detected:")
            print(neg_spikes)

    print("\nContains NaN values:", pct.isna().any())


if __name__ == "__main__":
    main()
