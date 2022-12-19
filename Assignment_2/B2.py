import pandas as pd
df2=pd.read_csv(r'C:\Users\Student\Desktop\Vishwanath.csv')
df2
from sklearn.model_selection import train_test_split(x,y,test_size=0.2)

y=df2.Remark
x=df2.drop('Remark',axis=1)
x
y
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
print(x_train)
print(x_test)