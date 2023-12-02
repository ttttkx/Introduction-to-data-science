import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\weather_gdp_data\\weather-gdp.csv")

X = df[['人口总量','人口城镇化率', '人均GDP', '第二产业所占比率', '年度']]
y = df['平均AQI']

# Add a constant column to the X matrix
X = sm.add_constant(X)

# Create a linear regression model
model = sm.OLS(y, X)

# Fit the model to the data
results = model.fit()

# Print the coefficients and their p-values
print("——————Coefficients:")
print(results.params)
print("——————P-values:")
print(results.pvalues)
