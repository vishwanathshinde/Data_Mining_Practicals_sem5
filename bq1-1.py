# Assigning features and label variables
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
weather = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']
temp = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild']
play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
# Import LabelEncoder
# creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
wheather_encoded = le.fit_transform(weather)
print(wheather_encoded)
# Converting string labels into numbers
temp_encoded = le.fit_transform(temp)
label = le.fit_transform(play)
print("Temp:", temp_encoded)
print("Play:", label)
# Combinig weather and temp into single listof tuples
features = zip(wheather_encoded, temp_encoded)
features = set(features)
print(features)
# Import Gaussian Naive Bayes model
#2
# Create a Gaussian Classifier
model = GaussianNB()
# Train the model using the training sets
model.fit(features, label)
# Predict Output
predicted = model.predict([[0, 2]])  # 0:Overcast, 2:Mild
print("Predicted Value:", predicted)