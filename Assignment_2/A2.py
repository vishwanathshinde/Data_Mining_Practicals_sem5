import pandas as pd
dataset=pd.read_csv(r'G:\DM_practicals\Vishwanath_DM\Assign_2\Vishwanath.csv')
dataset
x=dataset['Remark']
x
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
label=le.fit_transform(x)
label
