from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 导入数据
load_data = load_iris()
x = load_data.data
y = load_data.target

# 数据预处理，分割数据分别为训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25)

# 对训练集和测试集中的特征数据进行标准化
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)

# 进行算法处理，使用K-近邻
knn = KNeighborsClassifier()

# 输入训练集数据
knn.fit(x_train,y_train)

# 输入测试集，查看训练结果
result = knn.predict(x_test)

# 查看准确率
r_result = knn.score(x_test,y_test)
print("训练的结果为：",result)
print("正确的结果为：",y_test)
print("识别成功率为：",r_result)

