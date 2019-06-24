from AnaLex import AnaLex
import re
a = AnaLex("C:/Users/marco/Documents/GitHub/LexicalAnalyzer/main.txt")
tokens = a.AnaLex()

for i in tokens:
    print("<"+str(i.line)+",'"+i.content+"','"+i.att+"')")


