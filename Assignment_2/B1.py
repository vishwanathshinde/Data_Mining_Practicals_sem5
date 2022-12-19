import pandas as pd
df1=pd.read_csv(r'C:\Users\Student\Desktop\Vishwa.csv')
df1
import sklearn
from import preprocessing as per
scaler = per.MinMaxScaler(feature_range=(0,1))
Data=scaler.fit_transform(df1)
Data=pd.DataFrame(Data,index=df1.index,columns=df1.columns)
Data