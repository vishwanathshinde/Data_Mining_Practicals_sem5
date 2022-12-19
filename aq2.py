from sklearn.preprocessing import LabelEncoder
import pandas as pd
info = ('Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Female'], 'Position': ['Head', 'Asst.Prof', 'Associate Prof', 'Asst.Prof', 'Head', 'Asst.Prof'])
df = pd.DataFrame(info)
print(df)
le = LabelEncoder()
gender_encoded = le.fit_transform(df['Gender'])
enocded_position = le.fit_transform(['Position'])
df['Encoded_Gender'] = gender_encoded
df['Encoded_Position'] = encoded_position
print(df)
