from sklearn.datasets import fetch_20newsgroups
news_data = fetch_20newsgroups(subset = 'all')
 
x = news_data.data
y = news_data.target
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=33)
 
from sklearn.feature_extraction.text import CountVectorizer
#文本数据向量化
vec = CountVectorizer()
x_train=vec.fit_transform(x_train)
x_test=vec.transform(x_test)
 
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB() #初始化模型
model.fit(x_train,y_train) #调用fit函数进行模型训练
y_predict = model.predict(x_test) #使用predict 函数进行预测
 
 
from sklearn.metrics import classification_report
print("准确率:%.2f" % (float(model.score(x_test,y_test))*100))

