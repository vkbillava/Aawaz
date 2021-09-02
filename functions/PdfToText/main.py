import sys
sys.path.append('E:\\finalWorking\Voice')

from convert import convert
from voice import speak

text = convert('E:\web&HTML 5mk.pdf')

print(text)

speak(text)