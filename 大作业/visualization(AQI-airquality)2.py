from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

mpl.rcParams['axes.unicode_minus'] = False		# 显示负号

import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from a CSV file
df = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\air_quality_data\\air_quality_data(shanghai).csv")

variables = ['AQI', 'PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3']
df_subset = df[variables]

# Calculate Pearson correlation coefficients
correlation_matrix = df_subset.corr()

# Plot correlation matrix heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

plt.title('AQI和主要污染物的热力图')
plt.show()