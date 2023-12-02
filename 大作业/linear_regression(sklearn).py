import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\weather_gdp_data\\weather-gdp.csv")

X = df[['人口总量','人口城镇化率', '人均GDP', '第二产业所占比率', '年度']]
y = df['平均AQI']

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Print the coefficients
print("——————Coefficients:")
print(model.coef_)
