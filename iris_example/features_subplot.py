import numpy as np
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

iris = load_iris()
features = iris.data
feature_names = iris.feature_names
target = iris.target

pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for i,(p0,p1) in enumerate(pairs):
    plt.subplot(2,3,i+1)
    for x,marker,c in zip(range(3),">ox","rgb"):
        plt.scatter(features[target == x,p0], features[target == x,p1], marker=marker, c=c)
    plt.xlabel(feature_names[p0])
    plt.ylabel(feature_names[p1])
    plt.xticks([])
    plt.yticks([])
plt.show()
