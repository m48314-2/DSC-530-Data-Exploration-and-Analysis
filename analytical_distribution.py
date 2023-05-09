import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Read CSV file into a DataFrame
df = pd.read_csv('cleaned_data.csv')

# calculate mean and standard deviation
mu, std = norm.fit(df['sat_sum'])

# create a normal distribution plot
plt.hist(df['sat_sum'], bins=6, density=True, alpha=0.6, color='b')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)

plt.title('Normal Distribution of SAT Scores')
plt.xlabel('SAT Score')
plt.ylabel('Probability Density')
plt.show()
