import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('cleaned_data.csv')

# compute descriptive statistics for each column
for col in df.columns:
    mean = df[col].mean()
    mode = df[col].mode().iloc[0]
    std = df[col].std()
    min_val = df[col].min()
    max_val = df[col].max()
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    
    print(f"Column '{col}':")
    print(f"\tMean: {mean:.2f}")
    print(f"\tMode: {mode}")
    print(f"\tStandard Deviation: {std:.2f}")
    print(f"\tMinimum Value: {min_val}")
    print(f"\tMaximum Value: {max_val}")
    print(f"\t1st Quartile: {q1:.2f}")
    print(f"\t3rd Quartile: {q3:.2f}")
    print(f"\tInterquartile Range: {iqr:.2f}")


