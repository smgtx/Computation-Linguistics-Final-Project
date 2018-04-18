from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import pandas as pd
from pprint import pprint


train_data = pd.read_csv('SVM_Data.csv')

X_train = train_data.loc[:,"Total Utts" : "WPM"]
y_train = train_data["Output"]

#pprint(y_train)

test_data = pd.read_csv('SVM_Test.csv')

X_test = test_data.loc[:,"Total Utts" : "WPM"]
y_test = test_data["Output"]

model = SVC()
model.fit(X_train, y_train)

print("Score: ", model.score(X_test, y_test))

predictions = model.predict(X_test)

print('Accuracy Score: ', metrics.accuracy_score(y_test, predictions))

cVal = cross_val_score(SVC(), X_train, y_train, scoring='accuracy', cv=3)
print("Cross-Validated Score: ", cVal.mean())