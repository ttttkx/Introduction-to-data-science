from sklearn.feature_extraction.text import CountVectorizer
 
# 创建文本数据集
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
 
# 创建词袋模型对象
vectorizer = CountVectorizer()
 
# 将文本数据集转换为词袋特征向量矩阵
X = vectorizer.fit_transform(corpus)
 
# 输出词汇表
print("Vocabulary:", vectorizer.get_feature_names_out())
 
# 输出特征向量矩阵
print("Feature Matrix:\n", X.toarray())