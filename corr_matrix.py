import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('cleaned_data.csv')

# Calculate the correlation between 'fy_gpa' and other columns
corr_matrix = df.corr()['fy_gpa']

# Print the correlation coefficients
print(corr_matrix)
