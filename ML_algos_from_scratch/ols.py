import numpy as np

class OLS:
    def __init__(self, regularization = None, intercept = True):
        self.intercept = intercept
        self.regularization = regularization
    
    def fit(self, X, y):
        if self.regularization == 'l1':
            beta = self.lasso(X,y)
        elif self.regularization == 'l2':
            beta = self.ridge(X,y)
        else:
            beta = self.ols(X,y)
            
    def ols(self, X, y):
        if self.intercept:
            length = len(y)
            X = np.concat(np.ones(length), X, axis =1)
        return np.linalg.inv(X.T*X) * (X.T*y)        
    
    def normalization(self, X, transform = 'min_max'):
        if transform == 'min_max':
            X_min = np.min(X, axis = 0)
            X_max = np.max(X, axis = 0)
            X = (X - X_min)/(X_max-X_min)
        else:
            X_mean = np.mean(X, axis = 0)
            X_sd = np.std(X, axis = 0)
            X = (X - X_mean)/X_sd
        return X
    
    def G_l1(self, X, beta, y,  lambdaa):
        return 2 * X.T * X * beta - 2 * X.T * y + lambdaa * np.where(beta>0,1,-1)
    
    def G_l2(self, X, beta, lambdaa):
        return 2 * X.T * X * beta - 2 * X.T * y + 2 * lambdaa * beta
    
    def loss(self, X, w, y, lambdaa):
        if self.regularization == 'l1':
            return (y - X * w).T * (y - X * w) + lambdaa * np.sum(np.abs(w))
        elif self.regularization == 'l2':
            return (y - X * w).T * (y - X * w) + lambdaa * np.sum(w.T * w)
        else:
            return (y - X * w).T * (y - X * w)

    def GD(self, X, w, y, lambdaa, lr = 0.001, tol = 1e-5):
        init_loss = self.loss(X, w, y, lambdaa)
        new_w = 
        while
        
            
        
        