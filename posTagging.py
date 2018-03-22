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

def posTrigrams(words):
    sample = []
    for trigram in nltk.trigrams(words):
        sample.append(trigram)
    return sample
text = "My name is Alli and I'm programming again whudduppp"
wordy = text.split()
print(posTrigrams(wordy))
n=0


