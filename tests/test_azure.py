from providers.azure import fetch

def test_fetch():
    filename = fetch()
    print(f"Report created: {filename}")

if __name__ == "__main__":
    test_fetch()