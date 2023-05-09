import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
df = pd.read_csv('cleaned_data.csv')

# compute PMF for sat_v
pmf_v = df['sat_v'].value_counts(normalize=True).sort_index()

# plot PMF for sat_v
fig, ax = plt.subplots()
ax.plot(pmf_v.index, pmf_v.values)
ax.set_xlabel('Score')
ax.set_ylabel('Probability')
ax.set_title('PMF of SAT Verbal Scores')
plt.show()
