from step1_extract import extract_holiday_data
from step2_transform import transform_holiday_data
from step3_load import load_to_database

def run_pipeline():
    """Run the full ETL pipeline: extract, transform, load."""
    print("Starting ETL pipeline...")
    
    raw_df = extract_holiday_data()
    print(f"Extracted {len(raw_df)} rows.")
    
    cleaned_df = transform_holiday_data(raw_df)
    print(f"Transformed data - {cleaned_df.shape[1]} columns remaining.")
    
    load_to_database(cleaned_df)
    print("Pipeline finished successfully.")

if __name__ == "__main__":
    run_pipeline()