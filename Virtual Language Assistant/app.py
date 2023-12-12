import pyttsx3
import speech_recognition as sr
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import string
import pandas as pd
import random
import numpy as np

from chatbotdata import data

tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=2000)
le = LabelEncoder()

def preprocess_data(data):
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
    return bot_response

def SpeechRecognition():
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as mic:

        r.adjust_for_ambient_noise(mic, duration=0.2)
        audio = r.listen(mic)

        text = r.recognize_google(audio)
        return text
    
def TextToSpeech(bot_response):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(bot_response)
    engine.runAndWait()

def App():
    x_train, y_train, tokenizer, le, responses = preprocess_data(data)
    model, input_shape = train_neural_network(x_train, y_train)

    while True:
        text = SpeechRecognition()

        bot_response = get_bot_response(text, model, tokenizer, le, responses, input_shape)

        TextToSpeech(bot_response)
        if text == 'quit':
            break

if '__main__' == __name__:
    App()