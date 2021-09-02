import sys
sys.path.append('E:\\finalWorking\Voice')
from convert import convert

from voice import speak

def test():

    text = convert("E:\FinalProject\IMG-20210507-WA0029.jpg")

    print(text)

    speak(text)


test()