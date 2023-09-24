from os import system

system('say -v"Mónica" hola mundo')

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print("Di algo: ")
        audio = r.listen(source)
        try:
            text = r.recognize_whisper(audio, language='es')
            system(f'say -v "Mónica" {text}')

            
            print("Has dicho: {}".format(text))
        except Exception as exception:
            print("No te he entendido: ", exception)