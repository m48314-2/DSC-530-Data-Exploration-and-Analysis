import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file into a DataFrame
df = pd.read_csv('cleaned_data.csv')

# compute CDF for hs_gpa
cdf = np.cumsum(np.histogram(df['hs_gpa'], bins=10, density=True)[0])

# plot CDF for hs_gpa
fig, ax = plt.subplots()
ax.plot(np.histogram(df['hs_gpa'], bins=10, density=True)[1][1:], cdf)
ax.set_xlabel('GPA')
ax.set_ylabel('Cumulative Probability')
ax.set_title('CDF Analysis of High School GPA')
plt.show()
