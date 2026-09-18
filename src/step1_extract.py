import requests
import pandas as pd

def extract_holiday_data(country_code="US", year=2025):
    """Fetch public holiday data from the Nager.Date API and return it as a DataFrame."""

    url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    return df

# Quick test when running this file directly
if __name__ == "__main__":
    df = extract_holiday_data()
    print(df.head())
    print(df.shape)
    print(df.columns.tolist())  # To see all 9 column names.
    print(df.isnull().sum())