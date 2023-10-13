import pandas as pd
import numpy as np
import string
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import random

## data set
data = {
    "intents" : 
    [
        {
            "tag" : "greeting",
            "inputs" : [
                "hello",
                "hi"
            ],
            "responses" : [
                "Hello There"
            ]
        },
        {
            "tag" : "goodbye",
            "inputs" : [
                "Goodbye"
            ],
            "responses" : [
                "Goodbye!"
            ]
        },
        {
            "tag" : "greeting-jp",
            "inputs" : [
            "おはようございます"
            ],
            "responses" : [
            "おはようございます"
            ]
        }
    ]
}

tags = []
inputs = []
responses = {}
for intent in data['intents']:
    responses[intent['tag']] = intent['responses']
    for lines in intent['inputs']:
        inputs.append(lines)
        tags.append(intent['tag'])


df = pd.DataFrame(
    {
        "inputs" : inputs,
        "tags" : tags
    }
)

df = df.sample(frac=1)

## data pre processing
df['inputs'] = df['inputs'].apply(lambda wrd:[ltrs.lower() for ltrs in wrd if ltrs not in string.punctuation])
df['inputs'] = df['inputs'].apply(lambda wrd: ''.join(wrd))

tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=2000)
tokenizer.fit_on_texts(df['inputs'])
train = tokenizer.texts_to_sequences(df['inputs'])
X_train = tf.keras.preprocessing.sequence.pad_sequences(train)

## encode outputs to binary for the machine to understand
encoder = LabelEncoder()
y_train = encoder.fit_transform(df['tags'])

input_shape = X_train.shape[1]

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(input_shape,)),
    tf.keras.layers.Dense(64, activation = 'relu'),
    tf.keras.layers.Dense(64, activation  ='relu'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
  ]
)

initial_learning_rate = 0.06
decay_steps = 1000
decay_rate = 0.9

learning_rate_schedule = tf.optimizers.schedules.ExponentialDecay(initial_learning_rate, decay_steps, decay_rate)

optimiser = tf.keras.optimizers.Adam(learning_rate = learning_rate_schedule)

model.compile(optimizer = optimiser, loss = 'binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=200)

while True:
    texts_p = []
    prediction_input = input('You: ')

    prediction_input = [letters.lower() for letters in prediction_input if letters not in string.punctuation]
    prediction_input = ''.join(prediction_input)
    texts_p.append(prediction_input)

    prediction_input = tokenizer.texts_to_sequences(texts_p)
    prediction_input = np.array(prediction_input).reshape(-1)
    prediction_input = tf.keras.preprocessing.sequence.pad_sequences([prediction_input], input_shape)

    output = model.predict(prediction_input)
    output = output.argmax()

    response_tag = encoder.inverse_transform([output])[0]
    bot_name = 'bob'

    print(f'{bot_name}: ', random.choice(responses[response_tag]))
    if response_tag == "goodbye":
        break