import speech_recognition as sr

def speechrecognition_en():
    
    r = sr.Recognizer()
    
    while True:
        try:
            with sr.Microphone() as mic:

                r.adjust_for_ambient_noise(mic, duration=0.2)
                audio = r.listen(mic)

                text = r.recognize_google(audio)

                print(f'Heard: {text}')
                return

        except sr.UnknownValueError():
            r = sr.Recognizer()
            continue

def speechrecognition_jp():
    
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:

                r.adjust_for_ambient_noise(mic, duration=0.2)
                audio = r.listen(mic)

                text = r.recognize_google(audio, language='ja-JP')

                print(f'Heard: {text}')
                return

        except sr.UnknownValueError():
            r = sr.Recognizer()
            continue

def speechrecognition_fr():
    
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:

                r.adjust_for_ambient_noise(mic, duration=0.2)
                audio = r.listen(mic)

                text = r.recognize_google(audio, language='fr-FR')

                print(f'Heard: {text}')
                return

        except sr.UnknownValueError():
            r = sr.Recognizer()
            continue

def App():
    print('If You Wish to Speak in English Press 1')
    print('If You Wish to Speak in Japanese Press 2')
    print('If You Wish to Speak in French Press 3')
    o = input('Option: ')
    if o == '1':
        speechrecognition_en()
    elif o == '2':
        speechrecognition_jp()
    elif o == '3':
        speechrecognition_fr()
    else:
        App()

if __name__ == '__main__':
    App()