import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
df = pd.read_csv('satgpa.csv')

# Create a histogram for each column
for col in df.columns:
    plt.hist(df[col])
    plt.title(col)
    plt.show()


