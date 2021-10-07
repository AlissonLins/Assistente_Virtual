import pyttsx3
engine = pyttsx3.init()
engine.say("Olá, eu vou ajudar você")
engine.runAndWait()

def new_func(engine):
    voices = engine.getProperty('voices')

    for voice in voices:
        print(engine.getProperty('voice', voice.id))

new_func(engine)
