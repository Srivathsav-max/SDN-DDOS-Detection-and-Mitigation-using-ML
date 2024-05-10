from __future__ import division
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

# Load data
data = np.loadtxt('result.csv', delimiter=',')

# Define features and labels
X = data[:, [0, 1]]  # sfe, ssip
y = data[:, 3].astype(int)
X2 = data[:, [0, 2]]  # sfe, rfip

# Create a SVM classifier with a pipeline that includes scaling
clf = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', svm.SVC(kernel="linear", probability=True))
])

# Plotting decision regions
def plot_decision_boundary(X, y, clf, title, x_label, y_label, file_name):
    clf.fit(X, y)
    fig = plt.figure(figsize=(10, 8))
    ax = plot_decision_regions(X, y, clf=clf, legend=2)
    plt.title(title, size=16)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(file_name)

# Graph1: sfe & ssip
plot_decision_boundary(X, y, clf, 'SVM DDoS - Decision Region Boundary', 'Speed of Flow Entry', 'Speed of Source IP', 'svm_graph1.png')

# Graph2: sfe & rfip
plot_decision_boundary(X2, y, clf, 'SVM DDoS - Decision Region Boundary', 'sfe', 'rfip', 'svm_graph2.png')
