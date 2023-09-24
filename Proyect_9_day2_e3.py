from os import system
import speech_recognition as sr

from gpt4all import GPT4ALL 

brain = GPT4ALL("llama-2-7b-chat.ggmlv.q4_K_M.bin")

prompt = """
You are a useful assistant

Question: {user_input}
Answer:"
"""
r = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print("Di algo: ")
        audio = r.listen(source)
        try:
            # STT
            text = r.recognize_whisper(audio, language='es')
            # CEREBRO
            response = brain.generate(promp.replace("{user_input}", text))
            # TTS
            system(f'say -v "Mónica" {response}')
        except Exception as exception:
            print("No te he entendido: ", exception)