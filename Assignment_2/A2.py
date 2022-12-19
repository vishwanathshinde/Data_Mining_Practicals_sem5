import pandas as pd
dataset=pd.read_csv(r'C:\Users\Vishwanath\Practicals---\Data_Mining_Practicals_sem5\Assignment_2\Vishwanath.csv')
dataset
x=dataset['Remark']
x
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
label=le.fit_transform(x)
label