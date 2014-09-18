import numpy as np
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

iris= load_iris()
features = iris.data
feature_names = iris.feature_names
target = iris.target

plt.figure(1)
for x,marker,c in zip(range(3),">ox","rgb"):
        plt.scatter(features[target == x,0], features[target == x,1], marker=marker, c=c)
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.xticks([])
plt.yticks([])

plt.figure(2)
for x,marker,c in zip(range(3),">ox","rgb"):
        plt.scatter(features[target == x,0], features[target == x,2], marker=marker, c=c)
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[2])
plt.xticks([])
plt.yticks([])

plt.figure(3)
for x,marker,c in zip(range(3),">ox","rgb"):
        plt.scatter(features[target == x,0], features[target == x,3], marker=marker, c=c)
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[3])
plt.xticks([])
plt.yticks([])

plt.figure(4)
for x,marker,c in zip(range(3),">ox","rgb"):
        plt.scatter(features[target == x,1], features[target == x,2], marker=marker, c=c)
plt.xlabel(feature_names[1])
plt.ylabel(feature_names[2])
plt.xticks([])
plt.yticks([])


plt.figure(4)
for x,marker,c in zip(range(3),">ox","rgb"):
        plt.scatter(features[target == x,1], features[target == x,2], marker=marker, c=c)
plt.xlabel(feature_names[1])
plt.ylabel(feature_names[2])
plt.xticks([])
plt.yticks([])

plt.figure(5)
for x,marker,c in zip(range(3),">ox","rgb"):
        plt.scatter(features[target == x,1], features[target == x,3], marker=marker, c=c)
plt.xlabel(feature_names[1])
plt.ylabel(feature_names[3])
plt.xticks([])
plt.yticks([])

plt.figure(6)
for x,marker,c in zip(range(3),">ox","rgb"):
        plt.scatter(features[target == x,2], features[target == x,3], marker=marker, c=c)
plt.xlabel(feature_names[2])
plt.ylabel(feature_names[3])
plt.xticks([])
plt.yticks([])


plt.show()
