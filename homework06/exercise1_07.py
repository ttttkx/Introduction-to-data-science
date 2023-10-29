import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

def load_data():
    """
    加载数据集
        X: 花瓣宽度
        Y: 鸢尾花类型
    """
    # 加载sklearn包自带的鸢尾花数据;
    iris = datasets.load_iris()

    X = iris['data'][:, 3:]
    # 获取分类的结果
    Y = iris['target']
    return  X, Y


def configure_plt(plt):
    # 配置图形的坐标表信息
    # 获取当前的坐标轴, gca = get current axis
    ax = plt.gca()
    # 设置x轴, y周在(0, 0)的位置
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    # 绘制x，y轴说明
    plt.xlabel('petal width (cm)')  # 花瓣宽度
    plt.ylabel('target')    # 鸢尾花类型
    return  plt


def model_train():
    # 通过上面的数据做逻辑回归
    log_reg = LogisticRegression(multi_class='ovr', solver='sag')
    X, Y = load_data()
    log_reg.fit(X, Y)
    print('w0:', log_reg.coef_)
    print('w1:', log_reg.intercept_)
    return  log_reg


def test_data(log_reg):
    # 创建新的数据集去测试
    #   np.linespace 用于创建等差数列的函数， 会创建一个从0到3的等差数列， 包含1000个值；
    #   reshape生成1000行1列的数组；
    X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
    # print(X_new)
    y_proba = log_reg.predict_log_proba(X_new)
    y_hat = log_reg.predict(X_new)
    print(y_proba)
    print(y_hat)
    return  X_new, y_hat

def draw_pic():
    # 绘制图形
    X, Y = load_data()
    log_reg = model_train()
    test_X, test_Y = test_data(log_reg)
    import matplotlib.pyplot as plt
    plt.scatter(X,  Y,   c='red')
    plt.scatter(test_X,  test_Y,   c='green')
    plt = configure_plt(plt)

    # 显示图
    plt.show()


if __name__ == '__main__':
    draw_pic()
    

iris = datasets.load_iris()
X = iris['data']
Y = iris['target']

log_reg = LogisticRegression(multi_class='ovr', solver='sag', max_iter=10000)
log_reg.fit(X, Y)


X_new = [[5.1, 3.5, 1.4, 0.2]]
print(log_reg.predict_proba(X_new))
print(log_reg.predict(X_new))


