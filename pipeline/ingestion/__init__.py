# ingestion/__init__.py
print("Initializing the ingestion package")

from .ingest_data import fetch_statcast_data,save_to_csv  # Exposing DataIngestor for easier access
