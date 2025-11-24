# main.py
import argparse
import logging
from data_manager.loader import DataLoader
from data_manager.validator import DataValidator
from analytics.reports import ReportGenerator
from visualization.plots import Plotter
from config import LOG_FILE

# Setup basic logging for error handling and system messages
logging.basicConfig(
    filename=LOG_FILE, 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_analysis(file_path):
    """
    Core function to orchestrate the data processing workflow (F-100, F-200, F-300).
    """
    print("\n--- Starting UCDA Analysis ---")
    try:
        # F-100: Data Loading
        loader = DataLoader(file_path)
        raw_df = loader.load_data()
        logging.info(f"Successfully loaded {len(raw_df)} records.")

        # F-100: Data Validation
        validator = DataValidator(raw_df)
        if not validator.is_valid():
            print("\n❌ DATA VALIDATION FAILED:")
            for error in validator.get_errors():
                print(f"  - {error}")
                logging.error(f"Validation Error: {error}")
            print("\nPlease fix the input file and try again.")
            return

        # F-100: Data Cleaning
        clean_df = validator.clean_data()
        logging.info("Data validated and cleaned successfully.")
        print("Data is valid and clean. Proceeding to analysis...")

        # F-200: Core Analysis & Reporting
        reporter = ReportGenerator(clean_df)
        reporter.generate_class_summary()
        reporter.generate_individual_reports()
        logging.info("Reports generated successfully.")

        # F-300: Visualization
        plotter = Plotter(clean_df)
        plotter.generate_grade_distribution()
        plotter.generate_course_boxplot()
        logging.info("Plots generated successfully.")

    except FileNotFoundError as e:
        print(f"\n❌ ERROR: {e}")
        logging.critical(f"Critical Error: {e}")
    except ValueError as e:
        print(f"\n❌ ERROR: Data processing failed. {e}")
        logging.error(f"Processing Error: {e}")
    except Exception as e:
        print(f"\n❌ An unexpected system error occurred: {e}")
        logging.critical(f"System Error: {e}")
    finally:
        print("\n--- UCDA Analysis Complete ---\n")


def main():
    """Sets up the Command Line Interface (CLI) using argparse."""
    parser = argparse.ArgumentParser(
        description="UCDA: University Course Data Analyst - Automate analysis and visualization of student grades.",
        epilog="Example: python main.py data/sample_grades.csv"
    )
    
    # Define the mandatory positional argument for the input file path
    parser.add_argument(
        'input_file', 
        type=str, 
        help="Path to the raw CSV file containing student course data."
    )
    
    # Custom Non-Functional Requirement: Error Handling Strategy
    parser.add_argument(
        '--log', 
        action='store_true', 
        help=f"View the contents of the last execution log file ({LOG_FILE})."
    )

    args = parser.parse_args()
    
    if args.log:
        try:
            with open(LOG_FILE, 'r') as f:
                print(f"\n--- {LOG_FILE} Contents ---")
                print(f.read())
        except FileNotFoundError:
            print(f"Log file '{LOG_FILE}' not found. Run the analysis first.")
        return
    
    process_analysis(args.input_file)

if __name__ == '__main__':
    # Ensure all sub-packages are recognized
    from src.data_manager import * from src.analytics import *
    from src.visualization import *
    
    main()
