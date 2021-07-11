import numpy as np

class KNN:
    def __init__(self, K):
        self.K = K
    
    def reset_K(self, K):
        self.K = K
        
    def fit(self, y, X, dist_type = 'l2'):
        dist = self.distance(X, dist_type, X)
        topk_y = self.top_k(y, dist)
        return self.classifier(topk_y)
    
    def predict(self, pt, y, X):
        dist = self.distance(X, dist_type, pt)
        topk_y = self.top_k(y, dist)
        return self.classifier(topk_y)
    
    def distance(self, X, dist_type, pt = X):
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
    
    def classifier(self, arr):
        unique, count = np.unique(arr,return_counts=True)
        most_appear = np.where(count == np.amax(count))
        class_ = np.random.choice(unique[most_appear])
        return class_

    def pick_class(self, y_topk):
        return np.apply_along_axis(self.classifier(), 
                                    axis = 1, 
                                    arr  = y_topk)
    
if __name__=='__main__':
    