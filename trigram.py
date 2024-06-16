import nltk
import regex
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# nltk.download('punkt')
# nltk.download('stopwords')


def prepText(text):
    words = word_tokenize(text)
    words = [word.lower() for word in words]
    # stop_words = set(stopwords.words('english'))
    # words = [word for word in words if word not in stop_words]
    words = [word for word in words if word.isalnum()]
    return words


def genTrigrams(words):
    trigrams = {}
    for trigram in ngrams(words, 3):
        st = (trigram[0], trigram[1])
        sug = trigram[2]
        if st in trigrams:
            trigrams[st].append(sug)
        else:
            trigrams[st] = [sug]
    return trigrams


def genBigrams(words):
    bigrams = {}
    for bigram in ngrams(words, 2):
        st = (bigram[0])
        sug = bigram[1]
        if st in bigrams:
            bigrams[st].append(sug)
        else:
            bigrams[st] = [sug]
    return bigrams


def countFrequency(gramDict, n):
    gramFreqs = {}
    if n == 3:
        for key, value in gramDict.items():
            w1, w2 = key
            if (w1, w2) not in gramFreqs:
                gramFreqs[(w1, w2)] = {}
            for w3 in value:
                if w3 in gramFreqs[(w1, w2)]:
                    gramFreqs[(w1, w2)][w3] += 1
                else:
                    gramFreqs[(w1, w2)][w3] = 1
    elif n == 2:
        for key, value in gramDict.items():
            w1 = key
            if w1 not in gramFreqs:
                gramFreqs[w1] = {}
            for w2 in value:
                if w2 in gramFreqs[w1]:
                    gramFreqs[w1][w2] += 1
                else:
                    gramFreqs[w1][w2] = 1

    return gramFreqs
    
    
def sentenceSuggestion(inputList, suggestions):
    sentences = []
    inputText = ' '.join(inputList)
    for sug in suggestions:
        sentence = inputText + ' ' + sug
        sentences.append(sentence)
    return sentences


# corpus = open("Three-Thousand-Years-of-Mental-Healing.txt", encoding="utf-8")
corpus = open("new.txt", encoding="utf-8")
corpus = corpus.read()
wordsP = prepText(corpus)
tris = genTrigrams(wordsP)
bis = genBigrams(wordsP)

# first I ordered it based on the frequency after counting it, then removed the frequency and kept the shape of the bis/tris dict to avoid issues in the GUI
# this will also be better to remove duplicates and avoid using set and ruining the order.
bis = {key: [word for word, _ in sorted(value.items(), key=lambda item: item[1], reverse=True)] for key, value in countFrequency(bis,2).items()}
tris = {key: [word for word, _ in sorted(value.items(), key=lambda item: item[1], reverse=True)] for key, value in countFrequency(tris,3).items()}
# print(sentenceSuggestion(["mental", "health"], tris[("mental", "health")]))
