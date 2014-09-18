from sklearn.datasets import load_boston
boston = load_boston()
from matplotlib import pyplot as plt
import scipy as sp
from sklearn.metrics import mean_square_error

plt.figure(1)
plt.hist(boston.target)
plt.xlabel('price ($1000s)')
plt.ylabel('count')

from sklearn.linear_model import LinearRegression

clf = LinearRegression()

clf.fit(boston.data[::2], boston.target[::2])

predicted = clf.predict(boston.data[1::2])
plt.figure(2)
plt.scatter(boston.target[1::2], predicted)
plt.plot([0, 50], [0, 50], '--k')
plt.axis('tight')
plt.xlabel('True price ($1000s)')
plt.ylabel('Predicted price ($1000s)')


print mean_square_error(boston.target[1::2],predicted) 

plt.show() 
