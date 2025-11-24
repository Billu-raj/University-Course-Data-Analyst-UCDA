# analytics/reports.py
import pandas as pd
import numpy as np
import os
from config import LOW_PERFORMANCE_THRESHOLD, REPORT_OUTPUT_DIR

class ReportGenerator:
    """Generates various analytical reports from cleaned course data."""

    def __init__(self, df):
        self.df = df
        # Ensure output directory exists
        os.makedirs(REPORT_OUTPUT_DIR, exist_ok=True)
        self.report_path = os.path.join(REPORT_OUTPUT_DIR, 'analysis_report.txt')

    def _calculate_descriptive_stats(self, series):
        """Helper to calculate descriptive stats for a score series."""
        return {
            'Mean': series.mean(),
            'Median': series.median(),
            'StdDev': series.std(),
            'Min': series.min(),
            'Max': series.max(),
            'Count': series.count()
        }

    def generate_class_summary(self):
        """Generates a summary of performance across all score categories."""
        summary = {}
        score_columns = [col for col in self.df.columns if 'Score' in col or 'Grade' in col]

        with open(self.report_path, 'w') as f:
            f.write("="*60 + "\n")
            f.write("      UCDA: UNIVERSITY COURSE DATA ANALYST SUMMARY REPORT\n")
            f.write("="*60 + "\n\n")
            f.write(f"Total Records Analyzed: {len(self.df)}\n")
            f.write(f"Unique Courses: {self.df['CourseID'].nunique()}\n\n")

            for col in score_columns:
                stats = self._calculate_descriptive_stats(self.df[col])
                f.write(f"-- {col} Statistics --\n")
                for key, value in stats.items():
                    f.write(f"  {key:<10}: {value:,.2f}\n")
                f.write("-" * 25 + "\n")
            
            self._identify_low_performers(f)

        print(f"✅ Class Summary Report generated at: {self.report_path}")
        return self.report_path

    def _identify_low_performers(self, file_handle):
        """Identifies students whose final grade falls below the set threshold."""
        
        low_performers = self.df[self.df['FinalGrade'] < LOW_PERFORMANCE_THRESHOLD]
        
        file_handle.write(f"\n--- Low Performance Alert (FinalGrade < {LOW_PERFORMANCE_THRESHOLD}) ---\n")
        
        if low_performers.empty:
            file_handle.write("No students identified below the threshold.\n")
        else:
            file_handle.write(f"Total Low Performers: {len(low_performers)}\n")
            # Select relevant columns for the report
            report_data = low_performers[['StudentID', 'CourseID', 'FinalGrade']].sort_values(by='FinalGrade')
            
            # Convert to string and write to file
            file_handle.write(report_data.to_string(index=False))
            file_handle.write("\n")

    def generate_individual_reports(self):
        """(Future Enhancement) Would generate detailed reports per student."""
        print("\nNote: Individual student report generation skipped in this version.")
