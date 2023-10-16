import numpy as np

X=np.array([[1,2,3],[1,-1,4],[2,1,3],[1,3,-1]])
print(np.cov(X, rowvar=False))