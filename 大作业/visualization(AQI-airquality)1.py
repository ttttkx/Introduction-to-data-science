import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read data from a CSV file
df = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\air_quality_data\\air_quality_data(shanghai).csv")

# 将日期字段转换为日期时间类型
df['Time'] = pd.to_datetime(df['month'], format="%Y-%m-%d")

# 提取月份和日期
df['Year'] = df['Time'].dt.year
df['Month'] = df['Time'].dt.month

#variables = ['AQI', 'PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3']
variables = ['AQI', 'PM2.5', 'PM10', 'CO', 'Year']

# 绘图显示
sns.pairplot(df[variables], kind='reg', hue='Year')
plt.show()