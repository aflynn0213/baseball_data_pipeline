import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def process_statcast_data(csv_file):
    """Load, clean, and process Statcast data."""
    try:
        # Load the data from CSV
        df = pd.read_csv(csv_file)

        # Clean and process data (remove missing values and filter)
        df.dropna(inplace=True)  # Remove rows with missing values
        df = df[df['launch_speed'] > 80]  # Filter for hard-hit balls

        # Additional processing can be done here
        # e.g., df['some_column'] = df['some_column'].apply(some_function)

        return df
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
        return pd.DataFrame()  # Return an empty DataFrame
    except Exception as e:
        print(f"An error occurred while processing the data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame

def save_to_db(df, db_connection_str):
    """Save processed data to PostgreSQL."""
    if df.empty:
        print("No data to save to the database.")
        return
    
    try:
        engine = create_engine(db_connection_str)
        df.to_sql('processed_statcast', engine, if_exists='replace', index=False)
        print("Data saved to database successfully.")
    except SQLAlchemyError as e:
        print(f"Error saving data to database: {e}")

if __name__ == "__main__":
    csv_file = "statcast_data.csv"
    db_connection_str = "postgresql://username:password@localhost:5432/baseball"
    
    processed_data = process_statcast_data(csv_file)
    save_to_db(processed_data, db_connection_str)
