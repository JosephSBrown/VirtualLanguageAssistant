import pyttsx3
import speech_recognition as sr
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import string
import pandas as pd
import random
import numpy as np
import MeCab

from chatbotdata import data

bot_name = "Artie"
name = "Joseph"

tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=2000)
le = LabelEncoder()

def preprocess_data(data, language):
    tags = []
    inputs = []
    responses = {}
    for intent in data['intents']:
        responses[intent['tag']] = intent['responses']
        for lines in intent['input']:
            inputs.append(lines)
            tags.append(intent['tag'])

    df = pd.DataFrame({"inputs": inputs, "tags": tags})
    df = df.sample(frac=1)

    if language.lower() == 'japanese':
        mecab = MeCab.Tagger()
        df['inputs'] = df['inputs'].apply(lambda wrd: mecab.parse(wrd).split())
    else:
        df['inputs'] = df['inputs'].apply(lambda wrd: [ltrs.lower() for ltrs in wrd if ltrs not in string.punctuation])
        df['inputs'] = df['inputs'].apply(lambda wrd: ''.join(wrd))

    tokenizer.fit_on_texts(df['inputs'])
    train = tokenizer.texts_to_sequences(df['inputs'])
    x_train = tf.keras.preprocessing.sequence.pad_sequences(train)

    y_train = le.fit_transform(df['tags'])

    return x_train, y_train, tokenizer, le, responses

def build_model(input_shape, vocabulary, output_length):
    i = tf.keras.layers.Input(shape=(input_shape,))
    x = tf.keras.layers.Embedding(vocabulary + 1, 10)(i)
    x = tf.keras.layers.LSTM(10, return_sequences=True)(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(output_length, activation="softmax")(x)
    model = tf.keras.Model(i, x)
    model.compile(loss="sparse_categorical_crossentropy", optimizer='adam', metrics=['accuracy'])
    return model

def train_neural_network(x_train, y_train):
    input_shape = x_train.shape[1]
    vocabulary = len(tokenizer.word_index)
    output_length = le.classes_.shape[0]

    model = build_model(input_shape, vocabulary, output_length)

    model.fit(x_train, y_train, epochs=100)
    return model, input_shape

def get_bot_response(text, model, tokenizer, le, responses, input_shape):
    texts_p = []
    
    prediction_input = text

    prediction_input = [letters.lower() for letters in prediction_input if letters not in string.punctuation]
    prediction_input = ''.join(prediction_input)
    texts_p.append(prediction_input)

    prediction_input = tokenizer.texts_to_sequences(texts_p)
    prediction_input = np.array(prediction_input).reshape(-1)
    prediction_input = tf.keras.preprocessing.sequence.pad_sequences([prediction_input], input_shape)

    output = model.predict(prediction_input)
    output = output.argmax()

    response_tag = le.inverse_transform([output])[0]
    print("max output: ", np.max(output))
    print("Prediction Rating (Class Probabilities):", output.flatten())
    if np.max(output) < 0.7:
        bot_response="I Do Not Understand"
    else:
        bot_response = random.choice(responses[response_tag])
    bot_response = bot_response.replace("<NAME>", name)
    bot_response = bot_response.replace("<BOTNAME>", bot_name)
    return bot_response

def SpeechRecognition(srlang):
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as mic:

        r.adjust_for_ambient_noise(mic, duration=0.2)
        audio = r.listen(mic)

        text = r.recognize_google(audio, language=srlang)
        return text
    
def TextToSpeech(bot_response):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(bot_response)
    engine.runAndWait()

def Start():
    print("Choose a Number to Select a Language to Learn in\n[1]English\n[2]French\n[3]Japanese")
    choice = float(input("Choice: "))
    if choice == 1:
        language = "English"
        srlang = ""
    if choice == 2:
        language = "French"
        srlang = "fr-FR"
    elif choice == 3:
        language = "Japanese"
        srlang = "ja-JP"
    else:
        language = "English"
        srlang = ""

    App(language, srlang)

def App(language, srlang):
    x_train, y_train, tokenizer, le, responses = preprocess_data(data, language)
    model, input_shape = train_neural_network(x_train, y_train)

    while True:
        text = SpeechRecognition(srlang)
        print(f'You: {text}')

        bot_response = get_bot_response(text, model, tokenizer, le, responses, input_shape)

        print(f'{bot_name}: {bot_response}')
        TextToSpeech(bot_response)
        if text == 'quit':
            break

if '__main__' == __name__:
    Start()