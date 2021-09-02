import speech_recognition as sr

r = sr.Recognizer()

def get_audio():
    
    with sr.Microphone() as source:

        audio = r.listen(source, 5, 5)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            return 'I did not get that'
        except sr.RequestError:
            return 'Sorry, the service is down'
        return voice_data.lower()
