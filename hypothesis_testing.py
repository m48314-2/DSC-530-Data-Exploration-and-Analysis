import pandas as pd
import statsmodels.api as sm

# Read CSV file into a DataFrame
df = pd.read_csv('cleaned_data.csv')

# Set the predictor variables (X) and response variable (y)
X = df[['sex','sat_v','sat_m','sat_sum','hs_gpa']]
X = sm.add_constant(X)  # add a constant term
y = df['fy_gpa']

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Print the model summary
print()
print(model.summary())


