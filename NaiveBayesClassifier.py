import os

from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from importChatFile import getFile
from posTagging import posTagsFromObject, posTagsFromFile
from pprint import pprint
import pylangacq as pla
from sklearn import metrics
import numpy as np
from pprint import pprint
from sklearn.preprocessing import OneHotEncoder




train_files = pla.read_chat("/Users/sandeep/Google Drive/Sandeep/College/4th Semester/Computational Linguistics/Computation-Linguistics-Final-Project/Data/Train/*.cha")

types = {'SE' : 3, 'LP' : 1, 'SD' : 2}

X_train = []
y_train = []
for file in train_files.filenames():
    item = posTagsFromFile(file)
    y_train.append(types[os.path.basename(file)[0:2]])
    X_train.append(item)


labels = []
for x in X_train:
    for x1 in x:
        if x1 not in labels:
            labels.append(x1)


###Call your function with X_train as param here###




########################
test_files = pla.read_chat("/Users/sandeep/Google Drive/Sandeep/College/4th Semester/Computational Linguistics/Computation-Linguistics-Final-Project/Data/Test/*.cha")

X_test = []
y_test = []

for file in test_files.filenames():
    item = posTagsFromFile(file)
    y_test.append(types[os.path.basename(file)[0:2]])
    X_test.append(item)

###Call your function with X_train as param here###







#######################



for x in X_test:
    for x1 in x:
        if x1 not in labels:
            labels.append(x1)



for x in X_test:
    for num in range(0, len(x)):
        idx = labels.index(x[num])
        x[num] = idx
for x in X_train:
    for num in range(0, len(x)):
        idx = labels.index(x[num])
        x[num] = idx


X_data = X_train + X_test
y_data = y_train + y_test









print(X_train)

X_data = np.asarray([np.array(xi) for xi in X_data])
y_data = np.asarray([np.array(xi) for xi in y_data])
X_train = np.asarray([np.array(xi) for xi in X_train])
y_train = np.asarray([np.array(xi) for xi in y_train])
X_test = np.asarray([np.array(xi) for xi in X_test])
y_test = np.asarray([np.array(xi) for xi in y_test])


pprint(X_test)

'''
model = GaussianNB()
model.fit(X_train, y_train)


print("Score: ", model.score(X_test, y_test))

predictions = model.predict(X_test)

print('Accuracy Score: ', metrics.accuracy_score(y_test, predictions))

cVal = cross_val_score(GaussianNB(), X_train, y_train, scoring='accuracy', cv=10 )
print("Cross-Validated Score: ", cVal.mean())

'''






