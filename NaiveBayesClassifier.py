import os

from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from importChatFile import getFile
from posTagging import posTagsFromObject, posTagsFromFile, posTrigrams
from pprint import pprint
import pylangacq as pla
from sklearn import metrics
import numpy as np
from pprint import pprint
from sklearn.preprocessing import OneHotEncoder
from posTagging import posTrigrams




train_files = pla.read_chat("/Users/Alli/Desktop/Spring 2018/Comp. Ling/LingProject 2/IntermediateTrainingFIles/*.cha")

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
test_files = pla.read_chat("/Users/Alli/Desktop/Spring 2018/Comp. Ling/LingProject 2/IntermediateTestingFiles/*.cha")

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
        x[num] = str(idx)
for x in X_train:
    for num in range(0, len(x)):
        idx = labels.index(x[num])
        x[num] = str(idx)


X_test_trigrams = []
X_train_trigrams = []
for x in X_train:
    X_train_trigrams.append(posTrigrams(x))

for x in X_test:
    X_test_trigrams.append(posTrigrams(x))



X_test0 = []
y_test0 = []
counter = 0
for x in X_test_trigrams:
    classification = y_test[counter]
    for y in x:
        X_test0.append(y)
        y_test0.append(classification)

    counter+=1

X_train0=[]
y_train0=[]
counter = 0
for x in X_train_trigrams:
    classification = y_train[counter]
    for y in x:
        X_train0.append(y)
        y_train0.append(classification)
    counter+=1
print(y_test0)
print(y_train0)



X_data = X_train0 + X_test0
y_data = y_train0 + y_test0
X_train00=[]


print(X_train0)
counter = 0
'''for x in X_train0:
    X_train00[counter] = []
    for y in x:
        X_train00[counter].append(y)
    counter+=1
'''

for x in X_train0:
    temp = []
    for y in x:
        inty = int(y)
        temp.append(inty)
    X_train00.append(temp)


X_test00=[]
for x in X_test0:
    temp = []
    for y in x:
        inty = int(y)
        temp.append(inty)
    X_test00.append(temp)

'''

X_data = np.asarray([np.array(xi) for xi in X_data])
y_data = np.asarray([np.array(xi) for xi in y_data])
X_train = np.asarray([np.array(xi) for xi in X_train0])
y_train = np.asarray([np.array(xi) for xi in y_train0])
X_test = np.asarray([np.array(xi) for xi in X_test0])
y_test = np.asarray([np.array(xi) for xi in y_test0])


pprint(X_test)
'''

X = np.array(X_train00)
Y = np.array(y_train0)
X_test01 = np.array(X_test00)
y_test01 = np.array(y_test0)


from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X,Y)
print("Score: ", clf.score(X_test01, y_test01))

predictions = clf.predict(X_test01)

print('Accuracy Score: ', metrics.accuracy_score(y_test01, predictions))

cVal = cross_val_score(GaussianNB(), X, Y, scoring='accuracy', cv=10 )
print("Cross-Validated Score: ", cVal.mean())








