import unittest
import pandas as pd
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ingestion.ingest_data import fetch_statcast_data  # Replace 'your_function' with the actual function you want to import
from processing.process_data import process_statcast_data  # Replace 'your_function' with the actual function you want to import

class TestDataPipeline(unittest.TestCase):
    
    def test_fetch_statcast_data(self):
        data = fetch_statcast_data("2024-10-01", "2024-10-08")
        self.assertTrue(len(data) > 0, "No data fetched from API")

    def test_process_data(self):
        # Assume we have a sample CSV for testing
        df = process_statcast_data("test_statcast_data.csv")
        self.assertTrue(not df.empty, "Processed data is empty")
        self.assertTrue('launch_speed' in df.columns, "launch_speed column missing")

if __name__ == '__main__':
    unittest.main()
