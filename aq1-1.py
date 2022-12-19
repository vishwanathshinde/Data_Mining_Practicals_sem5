import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

pima = pd.read_csv("C:\\Users\\Asus\\Desktop\\DMDWLAb Book Material\diabetes.csv")
pima.head()
import seaborn as sns
corr=pima.corr()
ax=sns.heatmap(corr,vmin=1,vmax=1,center=0,cmap=sns.diverging_palette(20,220,n=200),square=True)
ax.set_xticklabels(ax.get_xticklabels(),rotation=45,horizontalalignment='right');
#feature selection
feature_cols=['Pregancies','Insulin','BMI','Age','Gluocse','BloodPressure','DiabetesPedigreeFunction']
x=pima.Outcome
#split data
X_train,X_test,Y_train=train_test_split(x,y,test_size=0.3,random_state=1)
#build model
classifier=DecisonTreeClassifier()
classifier=classifier.fit(X_train,Y_train)
#predict
y_pred=classifier.predict(X_test)
print(Y_pred)
from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,y_pred)
print(confusion_matrix(Y_test,y_pred))
#accuracys
print("Accuracy:",metric.accuracy_score(Y_test,y_pred))
from six import StringIO
from IPython.display import image
from sklearn.tree import export_graphviz
import pydotplus
dot_data=StringIO()
export_graphviz(classifier,out_file=dot_data,filled=True,rounded=True,special_characters=True,feature_names=feature_cols,class_names=['0','1'])
graph=pydotsplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetes.png')
Image(graph.create_png())
