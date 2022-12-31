import pandas as pd
# import numpy as np
from matplotlib import pyplot as plt
# from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
dataset = pd.read_csv(r'C:\Users\Vishwanath\Practicals---\Data_Mining_Practicals_sem5\Assignment_6\Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()