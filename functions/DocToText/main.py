import sys
sys.path.append('E:\\Aawaz Project\Voice')

from convert import convert
from voice import speak

text = convert('E:\ProjectTeam.docx')

print(text)

speak(text)