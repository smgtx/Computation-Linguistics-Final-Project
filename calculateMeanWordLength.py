from importChatFile import getFile
import numpy as np
file = 'SE001.cha'


def meanWordLen(filepath):
    file = getFile(filepath)
    lengthList = []
    for word in file.words():
        lengthList.append(len(word))

    meanWordLength = np.mean(lengthList)
    return meanWordLength


print(meanWordLen(file))