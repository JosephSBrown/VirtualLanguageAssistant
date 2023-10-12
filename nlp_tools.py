import numpy as np
import nltk
from nltk import WordNetLemmatizer
# nltk.download('punkt')

def tokenize(sentence):
    """
        split sentence into array of words/tokens
        a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)


def lemmatize(word):
    """
        lemmatizing groups words that have the same meanings and analyzes them as a single word
        A more consistent way of Stemming as it provides a context to the words
    """
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word.lower())