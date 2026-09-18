import pandas as pd

def transform_holiday_data(df):
    """Clean the raw holiday DataFrame: drop unusable columns, fill meaningful nulls."""
    
    # Drop launchYear column - 100% missing, provides no information
    df = df.drop(columns=['launchYear'])
    
    # Fill counties nulls - null means the holiday applies nationwide
    df['counties'] = df['counties'].fillna('Nationwide')

    # Convert any remaining lists in counties to plain text
    df['counties'] = df['counties'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

    # Convert types column from list to plain text - SQLite can't store lists
    df['types'] = df['types'].apply(lambda x: ', '.join(x))
    
    return df

# Quick test when running this file directly
if __name__ == "__main__":
    # Import extract function to get sample data to test on
    from step1_extract import extract_holiday_data
    
    raw_df = extract_holiday_data()
    cleaned_df = transform_holiday_data(raw_df)
    
    print(cleaned_df.isnull().sum())
    print(cleaned_df.shape)