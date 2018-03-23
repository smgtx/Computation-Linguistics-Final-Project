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
import os
from ConditionalProbability import condProb




train_files = pla.read_chat("/Users/sandeep/Google Drive/Sandeep/College/4th Semester/Computational Linguistics/Computation-Linguistics-Final-Project/Data/Train/*.cha")

types = {'SE' : 3, 'LP' : 1, 'SD' : 2}

X_train = []
y_train = []
for file in train_files.filenames():
    item = posTagsFromFile(file)
    y_train.append(types[os.path.basename(file)[0:2]])
    X_train.append(item)

for idx in range(0, len(X_train)):
    X_train[idx].insert(0, y_train[idx])





test_files = pla.read_chat("/Users/sandeep/Google Drive/Sandeep/College/4th Semester/Computational Linguistics/Computation-Linguistics-Final-Project/Data/Test/*.cha")


X_test = []
y_test = []
for file in test_files.filenames():
    item = posTagsFromFile(file)
    y_test.append(types[os.path.basename(file)[0:2]])
    X_test.append(item)
    #y_train.append(types[os.path.basename(file)[0:2]])
    #X_train.append(item)

'''
for idx in range(0, len(X_train)):
    X_train[idx].insert(0, y_train[idx])
'''
test = X_test
train = X_train

pos_counts = {}
for item in train:
    if 1 in item:
        if 1 not in pos_counts:
            pos_counts[1] = {}
        #new_item = set(item[11:].split())
        for word in item[1:]:
            if word not in pos_counts[1]:
                pos_counts[1][word] = 0
            pos_counts[1][word] += 1
    if 2 in item:
        if 2 not in pos_counts:
            pos_counts[2] = {}
        #new_item = set(item[5:].split())
        for word in item[1:]:
            if word not in pos_counts[2]:
                pos_counts[2][word] = 0
            pos_counts[2][word] += 1
    if 3 in item:
        if 3 not in pos_counts:
            pos_counts[3] = {}
        #new_item = set(item[5:].split())
        for word in item[1:]:
            if word not in pos_counts[3]:
                pos_counts[3][word] = 0
            pos_counts[3][word] += 1


labels = []
for x in X_train:
    for x1 in x:
        if x1 not in labels:
            labels.append(x1)
for x in X_test:
    for x1 in x:
        if x1 not in labels:
            labels.append(x1)

for x in pos_counts.keys():
    for item in labels:
        if item not in pos_counts[x]:
            pos_counts[x][item] = 1
        else:
            pos_counts[x][item] += 1


predictions = {}
test_case = 1
for item in X_test:
    predictions[test_case] = []
    predictions[test_case].append(y_test[test_case-1])
    prob1 = 1
    prob2 = 1
    prob3 = 1
    for words in item:
        prob1 = prob1 * condProb(1,words,pos_counts,X_train)
        prob2 = prob2 * condProb(2, words, pos_counts, X_train)
        prob3 = prob3 * condProb(3, words, pos_counts, X_train)
    pred = {}
    pred["1"] = prob1
    pred["2"] = prob2
    pred["3"] = prob3
    predictions[test_case].append(pred)
    test_case+=1

correct_pred = 0
total_pred = 0
for key in predictions.keys():
    total_pred += 1
    copy = sorted(predictions[key][1].items(), key=lambda x:x[1]).copy()
    copy.reverse()
    #pprint(copy)

    if predictions[key][0] == int(copy[0][0]):
        correct_pred+=1

    print("correct output:", predictions[key][0])
    print("prediction:", int(copy[0][0]))

print("accuracy:", correct_pred/total_pred)



