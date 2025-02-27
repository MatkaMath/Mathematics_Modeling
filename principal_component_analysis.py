#implement PCA from scratch and compare the results with SciPy's built-in PCA functions
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA as PCA_sklearn

data = load_iris()
X = data.data
y = data.target

def standardize(X):
    return (X - np.mean(X, axis=0)) / np.std(X, axis=0)

X_standardized = standardize(X)

# PCA implementation
def pca(X, n_components):
    covariance_matrix = np.cov(X.T)
    
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    selected_eigenvectors = sorted_eigenvectors[:, :n_components]
    
    X_reduced = X.dot(selected_eigenvectors)
    
    return X_reduced, sorted_eigenvalues[:n_components]

n_components = 2
X_pca_custom, eigenvalues_custom = pca(X_standardized, n_components)

# SciPy's built-in PCA
pca_sklearn = PCA_sklearn(n_components=n_components)
X_pca_sklearn = pca_sklearn.fit_transform(X_standardized)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_pca_custom[:, 0], X_pca_custom[:, 1], c=y, cmap='plasma', edgecolor='k', s=100)
plt.title('PCA implementation')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.subplot(1, 2, 2)
plt.scatter(X_pca_sklearn[:, 0], X_pca_sklearn[:, 1], c=y, cmap='plasma', edgecolor='k', s=100)
plt.title('SciPy PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.tight_layout()
plt.show()