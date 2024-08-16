import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for historical stock data in CSV format
url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=0&period2=9999999999&interval=1d&events=history"

# Headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to download CSV data
def download_csv(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        return response.content
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

# Download the CSV data
csv_data = download_csv(url)

if csv_data:
    # Save the CSV data to a file
    with open("yahoo_finance_stock_data.csv", "wb") as file:
        file.write(csv_data)
    print("Data saved to 'yahoo_finance_stock_data.csv'")
else:
    print("Failed to retrieve the data.")
