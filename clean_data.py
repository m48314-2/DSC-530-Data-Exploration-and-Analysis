import pandas as pd
import numpy as np

# Read CSV file into a DataFrame
df = pd.read_csv('satgpa.csv')

# Calculate the z-score for each data point
z_scores = np.abs((df - df.mean()) / df.std())

# Define a threshold z-score
threshold = 3

# Remove outliers from the DataFrame
df = df[(z_scores < threshold).all(axis=1)]

# Save cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False)
