import sys

sys.path.append("E:\\Aawaz Project\\functions\VoiceAssistant")

import speech_recognition as sr
from speak import engine_speak

r = sr.Recognizer()

def get_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down')
        print(">>", voice_data.lower())
        return voice_data.lower()
