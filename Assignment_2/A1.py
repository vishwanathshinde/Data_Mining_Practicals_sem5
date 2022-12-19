import pandas as pd
dataset=pd.read_csv(r'G:\DM_practicals\Vishwanath_DM\Assign_2\Vishwanath.csv')
dataset
dataset.isnull()
dataset=dataset.dropna()
dataset