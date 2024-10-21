import pandas as pd
from pybaseball import statcast
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from datetime import date

def fetch_statcast_data(start_date, end_date):
    """Fetch Statcast data from pybaseball between two dates."""
    try:
        # Fetch data using pybaseball
        df = statcast(start_dt=start_date, end_dt=end_date)
        return df
    except Exception as e:
        print(f"An error occurred while fetching Statcast data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame

def process_statcast_data(df):
    """Clean and process Statcast data."""
    try:
        # Clean and process data (remove missing values and filter)
        df.dropna(inplace=True)  # Remove rows with missing values
        df = df[df['launch_speed'] > 80]  # Filter for hard-hit balls

        # Additional processing can be done here
        # e.g., df['some_column'] = df['some_column'].apply(some_function)

        return df
    except Exception as e:
        print(f"An error occurred while processing the data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame

def save_to_db(df, db_connection_str):
    """Save processed data to PostgreSQL."""
    if df.empty:
        print("No data to save to the database.")
        return
    
    try:
        # Create a database connection
        engine = create_engine(db_connection_str)
        
        # Save the dataframe to a new SQL table
        df.to_sql('processed_statcast', engine, if_exists='replace', index=False)
        print("Data saved to database successfully.")
    except SQLAlchemyError as e:
        print(f"Error saving data to database: {e}")

if __name__ == "__main__":
    # Dynamically calculate the season start and end dates
    current_year = date.today().year
    start_date = f"{current_year}-03-28"  # Estimated start date for MLB season
    end_date = f"{current_year}-10-01"    # Estimated end date for regular season

    # Define your database connection string (adjust with your credentials)
    db_connection_str = "postgresql://username:password@localhost:5432/baseball"
    
    # Fetch data from pybaseball for the full season
    raw_data = fetch_statcast_data(start_date, end_date)
    
    # Process the raw data
    processed_data = process_statcast_data(raw_data)
    
    # Save the processed data to the database
    save_to_db(processed_data, db_connection_str)
