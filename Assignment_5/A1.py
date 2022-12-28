import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats
import numpy as np
x = np.array([0,1,2,3,4,5,6,7,8,9,11,13])
y = np.array([1,3,2,5,7,8,8,9,10,12,16,18])
slope, intercept, r, p, std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept
    
mymodel = list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()