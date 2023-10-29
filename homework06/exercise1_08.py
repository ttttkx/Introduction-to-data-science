import numpy as np
from sklearn.datasets import load_iris
from scipy.spatial import distance

# 加载鸢尾花数据集
iris = load_iris()
data = iris.data
target = iris.target

# 计算各类别数据的中心点
labels = np.unique(target)
centers = []
for label in labels:
    indices = np.where(target == label)
    class_data = data[indices]
    center = np.mean(class_data, axis=0)
    centers.append(center)

# 打印中心点坐标
for i, center in enumerate(centers):
    print(f"Center of class {i}: {center}")
    
# 计算每个数据点到中心点的欧式距离
distances = []
for point in data:
    point_distances = []
    for center in centers:
        point_distances.append(distance.euclidean(point, center))
    distances.append(point_distances)

# 存储到txt文件中
np.savetxt('distances.txt', distances)
