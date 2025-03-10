import pandas as pd
import os

def check_raw_data():
    # تاريخ معين علشان نتأكد
    date_to_check = "01-01-2021"
    file_path = f"source/covid_data_{date_to_check}.csv"
    
    if os.path.exists(file_path):
        print(f"File found: {file_path}")
        try:
            df = pd.read_csv(file_path)
            print(df.head())  # نطبع أول 5 صفوف من البيانات
        except Exception as e:
            print(f"Failed to read file: {e}")
    else:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    check_raw_data()