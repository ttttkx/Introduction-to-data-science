import pandas as pd
from scipy.stats import pearsonr

# Read data from a CSV file
df = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\weather_gdp_data\\weather-gdp.csv")

variables = ['平均AQI', '第二产业所占比率', '人口总量', '人口城镇化率', '人均GDP', '地区生产总值', '专利']
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
