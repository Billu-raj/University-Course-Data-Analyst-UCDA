Steps to Install & Run the Project
Clone the Repository (Version Control - Git Requirement):

Bash

git clone [Your_GitHub_Repo_URL]
cd Project-UCDA
Setup Environment (Technical Expectation): This project requires Python 3.8+ and several packages.

Bash

pip install pandas numpy matplotlib
Create Folders: Ensure the required output folders exist:

Bash

mkdir reports plots
Execute the Analysis (Clear Input/Output Structure): Run the main script, pointing it to the sample data file:

Bash

python src/main.py data/sample_grades.csv
View Output: The analysis reports (analysis_report.txt) will be in the reports/ directory, and the charts (.png files) will be in the plots/ directory.

View Logs (Error Handling Strategy):

Bash

python src/main.py --log
