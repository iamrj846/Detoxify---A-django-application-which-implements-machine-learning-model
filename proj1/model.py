# Naive Bayes

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Importing the dataset
dataset = pd.read_csv('C:\\Users\\Raunak Jain\\Desktop\\My_Django_Stuff\\proj1\\proj1\\framingham.csv')
X = dataset.iloc[:, :-1 ].values
y = dataset.iloc[:, 15].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = "mean", axis = 0)
imputer = imputer.fit(X[:, :])
X[:, :] = imputer.transform(X[:, :])

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X) #for training set you need to fit and transform

#splitting the dataset into test set and training set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state = 0)
# Fitting classifier to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 100,
                                    random_state = 0,
                                    criterion = "entropy")
classifier.fit(X_train, y_train)




# save the model to disk
pickle.dump(classifier, open('C:\\Users\\Raunak Jain\\Desktop\\My_Django_Stuff\\proj1\\proj1\\finalized_model.sav', 'wb'))


