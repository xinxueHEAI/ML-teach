import numpy as np

class KNN:
    def __init__(self, K):
        self.K = K
    
    def fit(self,y,X):
        return None
    
    def predict(self, pt, y, X):
        return None
    
    def distance(self, X, pt = X, dist_type = 'l2'):
        X_expand = X[:,None]
        if dist_type == 'l2':
            distance = np.power(X_expand - pt,2).sum(axis = 2)
        else:
            distance = np.abs(X_expand - pt).sum(axis = 2)
        return distance

    def top_k(self, y, dist):
        yranker = np.argsort(dist, axis = 1)
        y_ranked = y[yranker]
        y_topk = y_ranked[:,:self.K]
        return y_topk
    
    def pick_class(self, y_topk):
        