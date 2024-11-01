from pybaseball import steamer_batter_projection, steamer_pitcher_projection
from sqlalchemy import create_engine
import pandas as pd

def fetch_and_store_projections(year):
    # Fetch projections
    batter_projections = steamer_batter_projection(year)
    pitcher_projections = steamer_pitcher_projection(year)

    # Database connection
    engine = create_engine("postgresql://username:password@localhost:5432/baseball_data")

    # Store projections in the database
    batter_projections.to_sql('steamer_batter_projections', con=engine, if_exists='replace', index=False)
    pitcher_projections.to_sql('steamer_pitcher_projections', con=engine, if_exists='replace', index=False)

if __name__ == "__main__":
    fetch_and_store_projections(2023)  # Replace with the desired year
