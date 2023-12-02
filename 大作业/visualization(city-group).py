from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 从CSV文件读取数据集
df = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\weather_gdp_data\\weather-gdp(discrete).csv")

# 提取需要进行聚类的特征
features = df[['第二产业所占比率', '平均AQI']]

# 创建聚类模型
kmeans = KMeans(n_clusters=3)

# 进行聚类
kmeans.fit(features)

# 获取聚类结果的标签
labels = kmeans.labels_

# 将聚类结果添加到数据集中
df['Cluster'] = labels

# 绘制聚类结果的散点图
plt.scatter(df['第二产业所占比率'], df['平均AQI'], c=df['Cluster'])
plt.xlabel('第二产业占比')
plt.ylabel('AQI')
plt.title('聚类结果可视化')
plt.show()

