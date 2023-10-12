import numpy as np
import nltk
from nltk import WordNetLemmatizer
import MeCab #pip install mecab-python3 ##pip install unidic-lite
#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('omw-1.4')

def tokenize(sentence, language):
    """
        this returns a sentence as 'tokens' each word gets separated onto its own
        a token can be classified as either a word or a punctuation mark
    """
    if language == "japanese":
        jpt = MeCab.Tagger("-Owakati")
        tokens = jpt.parse(sentence).split()
        print(tokens)
    else:
        tokens = nltk.word_tokenize(sentence)

    return tokens

def lemmatize(word):
    """
        lemmatizing groups words that have the same meanings and analyzes them as a single word
        a more consistent way of Stemming as it provides a context to the words
    """
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word.lower())

def bag(tokenizedSentence):
    lemmatizedSentence = [lemmatize(word) for word in tokenizedSentence]
    print(lemmatizedSentence)


sen = "おはようございます."
sen1 = tokenize(sen, "japanese")
bag(sen1)

