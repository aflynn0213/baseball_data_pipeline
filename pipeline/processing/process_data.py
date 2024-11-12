import pandas as pd
from pybaseball import statcast
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from datetime import date

def fetch_statcast_data(start_date, end_date):
    """Fetch Statcast data from pybaseball between two dates."""
    try:
        df = statcast(start_dt=start_date, end_dt=end_date)
        return df
    except Exception as e:
        print(f"An error occurred while fetching Statcast data: {e}")
        return pd.DataFrame()

def process_statcast_data(df):
    """Clean and process Statcast data."""
    # Any additional processing steps can be added here if needed
    return df

def get_latest_date(engine):
    """Get the latest game_date in the database to avoid duplicate data."""
    query = "SELECT MAX(game_date) FROM processed_statcast"
    with engine.connect() as conn:
        result = conn.execute(query)
        latest_date = result.scalar()
    return latest_date

def save_to_db(df, engine):
    """Save processed data to PostgreSQL without duplicating data."""
    if df.empty:
        print("No new data to save to the database.")
        return
    
    try:
        df.to_sql('processed_statcast', engine, if_exists='append', index=False)
        print("New data saved to database successfully.")
    except SQLAlchemyError as e:
        print(f"Error saving data to database: {e}")

if __name__ == "__main__":
    #DB connection
    db_connection_str = "postgresql://username:password@localhost:5432/baseball"
    engine = create_engine(db_connection_str)

    # Grab most recent date of uploaded data
    latest_date = get_latest_date(engine)
    if latest_date is None:
        # First time initialization of data or in case of corruption
        start_date = "2015-03-01"
    else:
        # Make start date one day after last date of upload
        start_date = (latest_date + pd.Timedelta(days=1)).strftime('%Y-%m-%d')
    
    # Define the end date as today
    end_date = date.today()

    # Fetch, process, and save new data
    raw_data = fetch_statcast_data(start_date, end_date)
    processed_data = process_statcast_data(raw_data)
    save_to_db(processed_data, engine)
