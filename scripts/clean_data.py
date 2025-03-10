from datetime import datetime, timedelta
import os
import pandas as pd

def clean_covid_data():
    start_data = datetime.strptime("01-01-2021", "%m-%d-%Y")

    end_data = datetime.strptime("11-13-2023", "%m-%d-%Y")

    os.makedirs("cleaned", exist_ok=True)

    current_date = start_data
    while current_date <= end_data:
        date_to_clean = current_date.strftime('%m-%d-%Y')

        try:
            df = pd.read_csv(f"source/covid_data_{date_to_clean}.csv")


            df.columns = df.columns.str.lower().str.replace("/", "_").str.replace(" ", "_")

            if 'last_update' in df.columns:
                df['last_update'] = pd.to_datetime(df['last_update']).dt.strftime("%Y-%m-%d")

            df.fillna(0, inplace=True)
            df[['confirmed', 'deaths', 'recovered']] = df[['confirmed', 'deaths', 'recovered']].apply(lambda x: x.clip(lower=0))

            df.to_csv(f"source/cleaned/cleaned_covid_data_{date_to_clean}.csv", index=False)
            print(f"Data cleaned and saved for {date_to_clean}.")

        except FileNotFoundError:
            print(f"No raw data found for {date_to_clean}.")
        except Exception as e:
            print(f"Failed to clean data for {date_to_clean}: {e}")
        
        current_date += timedelta(days=1)


if __name__ == '__main__':
    clean_covid_data()