# visualization/plots.py
import pandas as pd
import matplotlib.pyplot as plt
import os
from config import PLOT_OUTPUT_DIR

class Plotter:
    """Handles the generation and saving of data visualizations."""

    def __init__(self, df):
        self.df = df
        os.makedirs(PLOT_OUTPUT_DIR, exist_ok=True)

    def generate_grade_distribution(self):
        """Generates a histogram for the 'FinalGrade' column."""
        
        plt.figure(figsize=(10, 6))
        
        # Plotting the histogram
        plt.hist(self.df['FinalGrade'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
        
        # Adding labels and title
        plt.title('Final Grade Distribution Across All Courses')
        plt.xlabel('Final Grade (%)')
        plt.ylabel('Number of Students')
        plt.grid(axis='y', alpha=0.5)
        
        # Save the plot
        plot_path = os.path.join(PLOT_OUTPUT_DIR, 'final_grade_distribution.png')
        plt.savefig(plot_path)
        plt.close() # Close plot to free memory
        
        print(f"✅ Grade Distribution Plot saved to: {plot_path}")
        return plot_path

    def generate_course_boxplot(self):
        """Generates a box plot to compare grade spread per CourseID."""
        
        plt.figure(figsize=(12, 7))
        
        # Generating a boxplot for FinalGrade grouped by CourseID
        self.df.boxplot(column='FinalGrade', by='CourseID', grid=True, patch_artist=True)
        
        plt.suptitle('') # Suppress the default suptitle created by pandas boxplot
        plt.title('Final Grade Spread by Course ID (Box Plot)')
        plt.xlabel('Course ID')
        plt.ylabel('Final Grade (%)')
        
        # Save the plot
        plot_path = os.path.join(PLOT_OUTPUT_DIR, 'course_grade_boxplot.png')
        plt.savefig(plot_path)
        plt.close()
        
        print(f"✅ Course Box Plot saved to: {plot_path}")
        return plot_path
