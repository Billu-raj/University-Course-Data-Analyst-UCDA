# data_manager/loader.py
import pandas as pd
import os

class DataLoader:
    """Handles the loading of raw data from a CSV file."""

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """
        Loads data from the specified CSV file.
        Raises FileNotFoundError if file is missing.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Input file not found at: {self.file_path}")
        
        print(f"Loading data from {self.file_path}...")
        try:
            # Using low_memory=False to better handle mixed types during initial load
            df = pd.read_csv(self.file_path, low_memory=False)
            return df
        except pd.errors.ParserError as e:
            raise ValueError(f"Error parsing CSV file: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred during loading: {e}")
