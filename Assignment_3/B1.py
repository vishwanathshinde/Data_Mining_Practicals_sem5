# Assignig features and label variables
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
# Import LabelEncoder
from sklearn import preprocessing
# create LabelEncoder
le=preprocessing.LabelEncoder()
# converting string label into numbers
weather_encoded=le.fit_transform(weather)
print("Weather:",weather_encoded)
temp_encoded=le.fit_transform(temp)
print("Temp:",temp_encoded)
label=le.fit_transform(play)
print("Play:",label)
# combining wheather and temp into single list of tuple
features= list(zip(weather_encoded,temp_encoded))
print(features)
# Import gaussin Naive Bayes model
from sklearn.naive_bayes import GaussianNB
# create a gaussian classifier
model= GaussianNB()
# train the modelusing the training sets
model.fit(features,label)
#predict output
predicted=model.predict([[0,2]])
#0:overcast,2:mild
print("Predicted value:",predicted)