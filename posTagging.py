from importChatFile import getFile
import nltk


def posTagsFromFile(filepath):
    f = getFile(filepath)
    #print(f.words())

    wordPOS = []
    for word in f.words():
        data = nltk.word_tokenize(word)
        wordPOS.append(nltk.pos_tag(data)[0][1])
    #print(wordPOS)
    return wordPOS

def posTagsFromObject(arr):
    wordPOS = []
    for word in arr.words():
        data = nltk.word_tokenize(word)
        wordPOS.append(nltk.pos_tag(data)[0][1])
    return wordPOS