# config.py

# Required columns for the input CSV data
REQUIRED_COLUMNS = [
    'StudentID', 
    'CourseID', 
    'Quiz1_Score', 
    'Midterm_Score', 
    'Final_Score', 
    'FinalGrade'
]

# Defines the expected data types for validation
COLUMN_DTYPES = {
    'StudentID': 'int64',
    'CourseID': 'object',
    'Quiz1_Score': 'float64',
    'Midterm_Score': 'float64',
    'Final_Score': 'float64',
    'FinalGrade': 'float64' 
}

# Threshold for identifying low performance (e.g., C grade or below)
LOW_PERFORMANCE_THRESHOLD = 70.0

# Output file paths
REPORT_OUTPUT_DIR = 'reports/'
PLOT_OUTPUT_DIR = 'plots/'
LOG_FILE = 'ucda_app.log'
