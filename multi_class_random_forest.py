#Importing Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib
print('Libraries Imported')

#Creating Dataset and including the first row by setting no header as input
dataset = pd.read_csv('iris.data.csv', header = None)
#Renaming the columns
dataset.columns = ['sepal length in cm', 'sepal width in cm','petal length in cm','petal width in cm','species']
print('Shape of the dataset: ' + str(dataset.shape))
print(dataset.head())

#Creating the dependent variable class
factor = pd.factorize(dataset['species'])
dataset.species = factor[0]
definitions = factor[1]
print(dataset.species.head())
print(definitions)

#Splitting the data into independent and dependent variables
X = dataset.iloc[:,0:4].values
y = dataset.iloc[:,4].values
print('The independent features set: ')
print(X[:5,:])
print('The dependent variable: ')
print(y[:5])

# Creating the Training and Test set from data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 21)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Fitting Random Forest Classification to the Training set
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 42)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
#Reverse factorize (converting y_pred from 0s,1s and 2s to Iris-setosa, Iris-versicolor and Iris-virginica
reversefactor = dict(zip(range(3),definitions))
y_test = np.vectorize(reversefactor.get)(y_test)
y_pred = np.vectorize(reversefactor.get)(y_pred)
# Making the Confusion Matrix
print(pd.crosstab(y_test, y_pred, rownames=['Actual Species'], colnames=['Predicted Species']))

lookup_iris_name = dict(zip(range(3),definitions))

iris_prediction = classifier.predict([[2.0, 1.3, 0.5, 0.90]])
print('[2.0, 1.3, 0.5, 0.90]: ' + lookup_iris_name[iris_prediction[0]])
