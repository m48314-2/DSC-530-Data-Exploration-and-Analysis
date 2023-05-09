Introduction<br>
This repository contains code for analyzing the first-year grade point average (GPA) of college students. The data provides insights on the factors that affect GPA, such as SAT scores and high school GPA. The goal of this project is to explore the data, generate insights, and identify any limitations of the analysis.

Data<br>
The dataset used in this project is available in the file satgpa.csv. It contains six columns: sex, sat_v, sat_m, sat_sum, hs_gpa, and fy_gpa. The file cleaned_data.csv is a cleaned version of the dataset with missing data and outliers removed.

Analysis<br><br>
The analysis is performed in Python using the following scripts:

<ul>
  <li>analytical_distribution.py: computes the analytical distribution for each column</li>
  <li>cdf_hs_gpa.py: generates a CDF plot for high school GPA</li>
  <li>clean_data.py: cleans the dataset by removing missing data and outliers</li>
  <li>corr_matrix.py: computes the correlation matrix between each column</li>
  <li>descriptive_characteristics.py: computes the mean, mode, standard deviation, and minimum value for each column</li>
  <li>histogram_analysis.py: generates a histogram plot for each column</li>
  <li>hypothesis_testing.py: performs hypothesis testing to determine the significance of each column in predicting first-year GPA</li>
  <li>pmf_sat_m.py: generates a PMF plot for SAT math scores</li>
  <li>pmf_sat_v.py: generates a PMF plot for SAT verbal scores</li>
  <li>regression_analysis.py: performs a linear regression analysis to predict first-year GPA based on the other columns</li>
  <li>scatter_plot-sat_m.py: generates a scatter plot for SAT math scores and first-year GPA</li>
  <li>scatter_plot-sat_v.py: generates a scatter plot for SAT verbal scores and first-year GPA</li>  
</ul>

<br>Results<br>
The EDA reveals the summary statistics and correlation coefficients of the six columns. The mean value of sex is 1.48, indicating that there are more females in the dataset. The mean values of SAT scores are moderate. The mean value of high school GPA is 3.20, and the mean value of first-year GPA is 2.47, which is lower than high school GPA, indicating a drop in performance in the first year.

The correlation matrix shows that the highest correlation with first-year GPA is high school GPA (0.535207), followed by SAT scores. The OLS regression analysis confirms that all four predictors: sex, sat_v, sat_m, and sat_sum, are statistically significant in predicting first-year GPA, along with high school GPA.

However, there are some limitations to this analysis. One significant limitation is the absence of other variables such as socioeconomic status, major, and study habits that could impact the first-year GPA. These variables could potentially confound the relationships found in this analysis. Additionally, there are no insights into the students' personal backgrounds or circumstances that could explain the lower first-year GPA.

Moreover, there is a possibility of incorrect assumptions. For instance, the assumption of linearity may not hold, and there could be a nonlinear relationship between the predictors and the first-year GPA. There is also a chance that the data is not normally distributed, and the summary statistics could be affected by outliers or extreme values.

Conclusion<br>
While this analysis provides insights into the factors that impact the first-year GPA, there are some limitations to the analysis that should be addressed. To better understand the predictors of first-year GPA, future studies should incorporate a broader range of variables and consider nonlinearity and non-normality assumptions.

