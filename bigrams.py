import nltk

print("hello")
count = { }

corpus = """
<s> I am Sam </s>
<s> Sam I am </s>
<s> I do not like green eggs and ham </s>
"""

words = corpus.split()

print(words)
# nltk.bigrams(words) yields a list of pairs, [('<s>', 'I'), ('I', 'am'), ...]
# I could iterate over them by saying 'for pair in nltk.bigrams(words):...'
# Or I can use assignment to multiple variables at once, as I do below.
# Remember: I can say
# word1, word2 = ('I', 'am')
# and that will assign 'I' to word1 and 'am' to word2.
# I am just doing this in a for-loop.
'''
for word1, word2 in nltk.bigrams(words):
    if word1 not in count:
        count[word1] = { }

    if word2 not in count[word1]:
        count[word1][word2] = 1
    else:
        count[word1][word2] += 1

# This printout just demonstrates
# that the code does the right thing
for word1 in count:
    for word2 in count[word1]:
        print(word1, word2, count[word1][word2])
        
'''