import requests
from datetime import datetime, timedelta
import os

def download_covid_data():
    start_date = datetime.strptime("01-01-2021", "%m-%d-%Y")

    end_date = datetime.strptime("11-13-2023", "%m-%d-%Y")

    current_date = start_date

    os.makedirs("source", exist_ok=True)

    while current_date <= end_date:
        date_to_try = current_date.strftime('%m-%d-%Y')
        print(date_to_try)
        url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date_to_try}.csv"
        print(f"Trying to download data from: {url}")

        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"source/covid_data_{date_to_try}.csv", "wb") as file:
                    file.write(response.content)
                print(f"Data downloaded successfully for {date_to_try}.")
            else:
                print(f"No data available for {date_to_try}.")
                break  
        except Exception as e:
            print(f"Failed to download data for {date_to_try}: {e}")
            break  

        current_date += timedelta(days=1)
    

if __name__ == "__main__":
    download_covid_data()
    