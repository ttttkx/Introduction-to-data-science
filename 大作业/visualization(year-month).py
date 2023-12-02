from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]


import pandas as pd

df1 = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\air_quality_data\\air_quality_data(2014).csv")
df2 = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\air_quality_data\\air_quality_data(2015).csv")
df3 = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\air_quality_data\\air_quality_data(2016).csv")
df4 = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\air_quality_data\\air_quality_data(2017).csv")

df1_AQI = df1['AQI']
df2_AQI = df2['AQI']
df3_AQI = df3['AQI']
df4_AQI = df4['AQI']

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['1月', '2月', '3月', '4月', '5月','6月','7月','8月','9月','10月','11月','12月']

x = np.arange(len(labels))  # the label locations

plt.xticks(x,labels)
plt.ylabel('AQI')
plt.title('AQI与月份的关系')

plt.plot(x,df1_AQI,label='2014')
plt.plot(x,df2_AQI,label='2015')
plt.plot(x,df3_AQI,label='2016')
plt.plot(x,df4_AQI,label='2017')
plt.legend()
plt.show()