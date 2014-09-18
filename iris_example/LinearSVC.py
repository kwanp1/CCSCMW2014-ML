from sklearn.datasets import load_iris
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
import numpy as np
iris = load_iris()
training_x = iris.data[::2]
training_y = iris.target[::2]
testing_x = iris.data[1::2]
testing_y = iris.target[1::2]
clf=LinearSVC()
clf=clf.fit(training_x,training_y)
predication=clf.predict(testing_x)
error=sum(predication != testing_y)*1.0/len(testing_y)
print "Error"
print error
print "confusion matrix"
print confusion_matrix(testing_y, predication,labels=None)
