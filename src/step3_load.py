import sqlite3
import pandas as pd

def load_to_database(df, db_path='data/loader.db', table_name='holidays'):
    """Load a DataFrame into a SQLite database table."""
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Loaded {len(df)} rows into '{table_name}' table in {db_path}")

# Quick test when running this file directly
if __name__ == "__main__":
    from step1_extract import extract_holiday_data
    from step2_transform import transform_holiday_data
    
    raw_df = extract_holiday_data()
    cleaned_df = transform_holiday_data(raw_df)
    load_to_database(cleaned_df)