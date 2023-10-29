from sklearn import datasets
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_datas = datasets.load_iris()

#iris = pd.read_csv(r'iris.csv',header=None)
 
train_x,test_x,train_y,test_y=train_test_split(iris_datas.data,iris_datas.target,test_size=0.3)
 
print("训练集和目标值",train_x,train_y)
print("测试集和目标值",test_x,train_y)