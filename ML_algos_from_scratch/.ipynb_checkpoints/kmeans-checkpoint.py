import numpy as np

class KMeans:
    '''KMeans clustering algorithm for unsupervised learning'''
    def __init__(self, K):
        self.K = K

    def reset_K(self, K):
        '''Reset the number of clusters to K'''
        self.K = K

    def initiate_centroids(self, X: np.array):
        array_len = X.shape[0]
        random = np.random.choice(range(array_len), self.K, replace = False)
        return X[random,:]
    
    def compute_distance(self, centroids, X, d_type = 'e'):
        #broadcast the difference
        pairwise_d = centroids[:,None] - X
        if d_type == 'e':
            dists = np.sum(np.power(pairwise_d,2), axis = 2)
        elif d_type == 'm':
            dists = np.sum(np.abs(pairwise_d), axis = 2)
        return dists

    def get_clusters(self, dists):
        arg_min = np.argmin(dists, axis = 0)
        return arg_min
    
    def new_centroids(self, X, clusters):
        centroids = []
        for i in sorted(np.unique(clusters)):
            c_i = X[np.where(clusters==i)]
            centroids.append(c_i.mean(axis = 0))
        return np.array(centroids)
        
    def convergence(self, new, old, tol = 1e-4):
        diff = np.sum(np.power(new - old,2))
        if diff < tol:
            return True
        else:
            return False
        
    def pip(self, cent, X, dtype):
        dists = self.compute_distance(cent, X, dtype)
        clusters = self.get_clusters(dists)
        new_cent = self.new_centroids(X, clusters)
        return new_cent, clusters
    
    def kmeans(self, X: np.array):
        cent = self.initiate_centroids(X)
        new_cent , _  = self.pip(cent, X, dtype = 'e')
        converged = self.convergence(new_cent, cent)
        while not converged:
            cent = new_cent
            new_cent, clusters = self.pip(cent, X, dtype = 'e')
            converged = self.convergence(new_cent, cent)
        return new_cent, clusters

    def kmedian(self, X: np.array):
        cent = self.initiate_centroids(X)
        new_cent , _  = self.pip(cent, X, dtype = 'd')
        converged = self.convergence(new_cent, cent)
        while not converged:
            cent = new_cent
            new_cent, clusters = self.pip(cent, X, dtype = 'd')
            converged = self.convergence(new_cent, cent)
        return new_cent, clusters
    
if __name__=='__main__':
