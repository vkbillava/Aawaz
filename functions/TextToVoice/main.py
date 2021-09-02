import pyttsx3

engine = pyttsx3.init()
print("Enter your text to convert it to speak type stop() to stop conversion")

while 1:
    text = input(">>   ")

    if text.lower() == "stop()":
        exit()
    
    engine.say(text)
    engine.runAndWait()
