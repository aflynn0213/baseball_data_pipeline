import requests
import pandas as pd

# Endpoint for Statcast Data (replace with actual endpoint)
STATCAST_API_URL = "https://somebaseballdataapi.com/statcast"

def fetch_statcast_data(start_date, end_date):
    """Fetch Statcast data between given dates."""
    params = {
        "start_date": start_date,
        "end_date": end_date
    }
    try:
        response = requests.get(STATCAST_API_URL, params=params)
        response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None  # Return None if there's an error

def save_to_csv(data, filename):
    """Save fetched data to a CSV file."""
    if data:  # Check if data is not None
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

if __name__ == "__main__":
    # Fetch last week's data
    start_date = "2024-10-01"
    end_date = "2024-10-08"
    
    data = fetch_statcast_data(start_date, end_date)
    save_to_csv(data, "statcast_data.csv")
