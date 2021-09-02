import sys

sys.path.append("E:\\Aawaz Project\\functions\VoiceAssistant")

from check import exists
from speak import engine_speak
from record import get_audio 
from name import person_obj, asistant_obj
from time import ctime
import webbrowser
import ssl
import certifi
import time
from PIL import Image
import subprocess
#import pyautogui
import pyttsx3
import bs4 as bs
import urllib.request
import requests


def response(voice_data):
    
    if exists(['hey','hi','hello'], voice_data ):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    
    if exists(["what is your name","what's your name","tell me your name"], voice_data ):

        if person_obj.name:
            engine_speak(f"My name is {asistant_obj.name}, {person_obj.name}")
        else:
            engine_speak(f"My name is {asistant_obj.name}. what's your name?")

    if exists(["my name is"], voice_data ):
        person_name = voice_data .split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name)
    
    if exists(["what is my name"], voice_data ):
        engine_speak("Your name must be " + person_obj.name)
    
    if exists(["your name should be"], voice_data ):
        asis_name = voice_data .split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asistant_obj.setName(asis_name)


    if exists(["how are you","how are you doing"], voice_data ):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

   
    if exists(["what's the time","tell me the time","what time is it","what is the time"], voice_data ):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

   
    if exists(["search for"], voice_data ) and 'youtube' not in voice_data :
        search_term = voice_data .split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")
    
    if exists(["search"], voice_data ) and 'youtube' not in voice_data :
        search_term = voice_data .replace("search","")
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    
    if exists(["youtube"], voice_data ):
        search_term = voice_data .split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

     
    if exists(["price of"], voice_data ):
        search_term = voice_data .split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")
    


    
    if exists(["show my time table"], voice_data ):
        im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
        im.show()
    
    
    if exists(["weather"], voice_data ):
        search_term = voice_data .split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")
     


    if exists(["game"], voice_data ):
        voice_data  = get_voice_data ("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data 
        

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")

    
    if exists(["toss","flip","coin"], voice_data ):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)

    
    if exists(["plus","minus","multiply","divide","power","+","-","*","/"], voice_data ):
        opr = voice_data .split()[1]

        if opr == '+':
            engine_speak(int(voice_data .split()[0]) + int(voice_data .split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data .split()[0]) - int(voice_data .split()[2]))
        elif opr == 'multiply' or 'x':
            engine_speak(int(voice_data .split()[0]) * int(voice_data .split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data .split()[0]) / int(voice_data .split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data .split()[0]) ** int(voice_data .split()[2]))
        else:
            engine_speak("Wrong Operator")
        
     
    if exists(["capture","my screen","screenshot"], voice_data ):
        import pyautogui
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D:/screenshot/screen.png')
    
    
    
    if exists(["definition of"], voice_data ):
        definition=get_voice_data ("what do you need the definition of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found '+definitions[1])
            else:
                engine_speak ('Here is what i found '+definitions[2])
        else:
                engine_speak("im sorry i could not find the definition for "+definition)


    if exists(["exit", "quit", "goodbye"], voice_data ):
        engine_speak("bye")
        exit()

    
    if exists(["where am i"], voice_data ):
        Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
        loc = Ip_info['region']
        engine_speak(f"You must be somewhere in {loc}")    
   

    if exists(["what is my exact location"], voice_data ):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")    