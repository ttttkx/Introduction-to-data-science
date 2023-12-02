import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\数据科学导论\\研究报告和数据\\长三角地区空气质量数据及说明\\weather_gdp_data\\weather-gdp(discrete).csv")

X = df[['人口总量','人口城镇化率', '人均GDP', '第二产业所占比率', '年度']]
y = df['空气质量']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)

# Create a logistic regression model
model = LogisticRegression()

# Fit the model to the data
model.fit(X_train, y_train)

# Print the coefficients
print("——————Coefficients:")
print(model.coef_)

y_pred = model.predict(X_test)

#Print the accuracy
from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred,y_test)
print("预测准确率：",score)
