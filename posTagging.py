from importChatFile import getFile
import nltk

file = 'SE001.cha'

def posTags(filepath):
    f = getFile(file)
    print(f.words())
    wordPOS = []
    for word in f.words():
        data = nltk.word_tokenize(word)
        wordPOS.append(nltk.pos_tag(data)[0][1])
    print(wordPOS)
    return wordPOS
posTags(file)
