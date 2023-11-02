from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def datasets_demo():
    # 1.获取鸢尾花数据集
    iris = load_iris()

    # 2. 对鸢尾花数据集进行划分
    train_x,test_x,train_y,test_y=train_test_split(iris.data,iris.target,test_size=0.2)
 
    print("训练集和目标值",train_x,train_y)
    print("测试集和目标值",test_x,train_y)
    
    return None

if __name__ == '__main__':
    datasets_demo()
