from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 读取数据集
df = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\weather_gdp_data\\weather-gdp(discrete).csv")

varX='第二产业所占比率'
varY='平均AQI'

# 按城市分组并绘制散点图
for city, data in df.groupby('城市'):
    plt.scatter(data[varX], data[varY], label=city)

# 添加图例和标签
plt.xlabel(varX)
plt.ylabel(varY)
plt.title(varX+ ' vs '+varY)
plt.legend()

# 显示图表
plt.show()