from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# 设置数据
df = pd.DataFrame({
    'group': ['A','B'],
    'PM2.5': [96,79],
    'PM10': [91,81],
    'SO2': [25,75],
    'CO': [41,33],
    'NO2': [62,57]
})
 
# 目标数量
categories = list(df)[1:]
N = len(categories)
 
# 角度
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# 初始化
ax = plt.subplot(111, polar=True)
 
# 设置第一处
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# 添加背景信息
plt.xticks(angles[:-1], categories)
ax.set_rlabel_position(0)
plt.yticks([20,40,60,80,100], ["20", "40", "60","80","100"], color="grey", size=6)
plt.ylim(0, 100)
 
# 添加数据图
 
# group A
values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="上海")
ax.fill(angles, values, 'b', alpha=0.1)

# group B
values = df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="南京")
ax.fill(angles, values, 'r', alpha=0.1)

# 添加图例
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()