import pandas as pd
from scipy.stats import pearsonr

# Read data from a CSV file
df = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\air_quality_data\\air_quality_data(shanghai).csv")

variables = ['AQI', 'PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3']
df_subset = df[variables]

# Calculate Pearson correlation coefficients
correlation_matrix = df_subset.corr()

# Print correlation matrix
print(correlation_matrix)

# Perform two-tailed t-test
p_values = []
for i in range(len(variables)):
    for j in range(i + 1, len(variables)):
        corr, p_value = pearsonr(df[variables[i]], df[variables[j]])
        p_values.append(p_value)

# Print p-values of the t-test
print(p_values)