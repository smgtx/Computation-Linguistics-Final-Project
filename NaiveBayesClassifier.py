import os
from sklearn.naive_bayes import GaussianNB
from importChatFile import getFile
from posTagging import posTagsFromObject, posTagsFromFile
from pprint import pprint
import pylangacq as pla


files = pla.read_chat("/Users/sandeep/Google Drive/Sandeep/College/4th Semester/Computational Linguistics/Computation-Linguistics-Final-Project/Data/*.cha")


X_data = []
for file in files.filenames():
    item = posTagsFromFile(os.path.basename(file))
    X_data.append(item)

y_data = [1]

X_test = []




model = GaussianNB()
model.fit(X_data, y_data)


prediction = model.predict(X_test)
score = model.score(X_data, y_data)








