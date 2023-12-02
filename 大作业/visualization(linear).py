from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]


import pandas as pd
import numpy
from sklearn.linear_model import LinearRegression

# Read data from a CSV file
df = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\weather_gdp_data\\weather-gdp-part.csv")

x = df[['第二产业所占比率']]
y = df['平均AQI']

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

import matplotlib.pyplot as plt
import seaborn as sns

#plt.scatter(x,y)
for city, data in df.groupby('城市'):
    plt.scatter(data['第二产业所占比率'], data['平均AQI'], label=city)

plt.plot(x,model.predict(x),color='red')
plt.title(u"平均AQI与第二产业占比的关系")
plt.xlabel('第二产业所占比率')
plt.ylabel('平均AQI')
plt.legend()
plt.show()



