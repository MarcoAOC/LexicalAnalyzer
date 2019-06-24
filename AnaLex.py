import re
import os
import FileHandling
from Content import Content

class AnaLex:

    def __init__(self,filepath):
        self.__path = filepath
        self.__contentOfFile = FileHandling.getcontents(filepath)
        self.__token = {
            ":=" : "assign_op",
            ";" : "semicolon",
            "(" : "lp",
            ">=" : "ge",
            "/" : "divide",
            ".." : "dotdot",
            "," : "comma",
            ")" : "rp",
            "<>" : "ne",
            "-" : "minus",
            "@" : "ender",
            "." : "dor",
            "[" : "lb",
            "=" : "equal",
            ">" : "gt",
            "*" : "times",
            ":" : "colon",
            "]" : "rb",
            "<=" : "le",
            "<" : "lt",
            "+" : "plus"
        }
        self.__Tokens = Content()
    
    def test(self):
        for line in self.__contentOfFile:
            for token in line.content:
                if token in self.__token:
                    self.__Tokens.line = line.line
                    self.__Tokens.content = self.__token[token]


