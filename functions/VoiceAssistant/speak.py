
import pyttsx3

engine = pyttsx3.init()

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()