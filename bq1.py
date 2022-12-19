#Normalise the data attributes for the iris dataset.
from sklearn.datasets import load_iris
from sklearn import preprocessing 
iris=load_iris()
X=iris.data
Y=iris.target
normalized_x=preprocessing.normalize(x)
