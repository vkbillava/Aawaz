import pyttsx3

engine = pyttsx3.init()

def speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

def stop():
    engine.stop()