# data_manager/validator.py
import pandas as pd
from config import REQUIRED_COLUMNS, COLUMN_DTYPES

class DataValidator:
    """Performs validation checks on the loaded DataFrame."""
    
    def __init__(self, df):
        self.df = df
        self.errors = []

    def validate_columns(self):
        """Checks if all required columns are present."""
        missing_cols = [col for col in REQUIRED_COLUMNS if col not in self.df.columns]
        if missing_cols:
            self.errors.append(f"Missing required columns: {', '.join(missing_cols)}")
        return not missing_cols

    def validate_dtypes(self):
        """Checks if key columns match the expected data types."""
        type_errors = []
        for col, expected_dtype in COLUMN_DTYPES.items():
            if col in self.df.columns:
                try:
                    # Attempt to cast the column to the expected type
                    self.df[col] = self.df[col].astype(expected_dtype)
                except ValueError:
                    # Append error if casting fails (e.g., text in a numeric column)
                    type_errors.append(f"Column '{col}' failed to cast to {expected_dtype}. Contains invalid values.")
        
        if type_errors:
            self.errors.extend(type_errors)
        return not type_errors

    def clean_data(self):
        """
        Performs data cleaning steps: handling missing values.
        For simplicity, we'll fill numeric NaNs with the column mean.
        """
        df_cleaned = self.df.copy()
        for col, dtype in COLUMN_DTYPES.items():
            if dtype in ['float64', 'int64'] and col in df_cleaned.columns:
                mean_val = df_cleaned[col].mean()
                # Fills NaN values in numeric columns with the column mean
                df_cleaned[col].fillna(mean_val, inplace=True)
                print(f"Info: Filled missing values in '{col}' with mean ({mean_val:.2f}).")
        return df_cleaned

    def is_valid(self):
        """Runs all validation checks."""
        self.validate_columns()
        self.validate_dtypes()
        return not self.errors

    def get_errors(self):
        return self.errors
