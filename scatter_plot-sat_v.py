import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
df = pd.read_csv('cleaned_data.csv')

# Create the scatter plot
plt.scatter(df['sat_v'], df['fy_gpa'])

# Set the plot title and axis labels
plt.title('SAT Verbal Score vs. First Year GPA')
plt.xlabel('SAT Verbal Score')
plt.ylabel('First Year GPA')

# Show the plot
plt.show()
