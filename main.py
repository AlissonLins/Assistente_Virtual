#1 / usr/bin/env python3 
from vosk import Model, KaldiRecognizer
import os, pyaudio 
import pyttsx3
import json
import integraCore 
from nlu import classify 

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-1].id)

def speak(text):
  engine.say(text)
  engine.runAndWait()

def evaluate(text):
# Reconhecer entidade do texto

        entity = classify(text)

        if entity == 'time|getTime':
            speak(integraCore.SystemInfo.get_time())
        elif entity == 'time|getDate':
            speak(integraCore.SystemInfo.get_date())

    # Abrir programas
        elif entity == 'open|notepad':
            speak('Abrindo o bloco de notas')
            os.sytem('notepad.exe')

        # Fechar programas
        elif entity == 'close|notepad':
            speak('Fechando o bloco de notas')
            os.sytem("TASKKILL /F /IM notepad.exe")

        print('Text: {}  Entity: {}'.format(text, entity)) 

        if not entity == classify(text):
         print(text)
         speak(text) 

# Reconhecimento de fala

model = Model ("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Loop do reconhecimento de fala

while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.Acceptwaveform(data):
       result = rec.Result()
       result = json.loads(result)

    if result is not None:
        text = result['text']
        evaluate(text)

     
