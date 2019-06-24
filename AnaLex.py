import re
import os
import FileHandling
from Content import Content

class AnaLex:

    def __init__(self,filepath):
        self.__path = filepath
        self.__contentOfFile = FileHandling.getcontents(filepath)
        self.__token = {
            ":=" : "as  sign_op",
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
            "==" : "equalequal",
            ">" : "gt",
            "*" : "times",
            ":" : "colon",
            "]" : "rb",
            "<=" : "le",
            "<" : "lt",
            "+" : "plus"}
        self.__keywords = { #palavras chaves devem estar separadas por espaço
            "while" : "while",
            "if" : "if",
            "else" : "else",
            "function" : "function",
            "let" : "let"
        }

        self.__Tokens = []
    

    def regularexpressions(self,test_string):
        letter = '[A-Za-z]'
        digit = '[0-9]'
        identifier = letter + '(' + letter + '|' +digit + ")*"
        digits = digit + '+'
        optional_fraction =  '(.' + digits +')?'
        optional_expoent = '((E|e)?'+digits+')?' #erro na definição
        num = digits + optional_expoent
        char1 = '[^\n]'
        string1 = '"' + char1 + '"' # erro
        character = ''
        regulardict = {
            0 : identifier,
            1 : num,
            2 : char1
        }
        i = 0
        while i < 3:
            result = re.match(regulardict[i],test_string)
            if(result != None):
                if i==0:
                    return "identifier"
                elif i==1:
                    return "num"
                elif i==2:
                    return "string"
            i+=1 
        return "Undefined"
        
    def evaluateTokensNoAtt(self):
        index = 0
        for line in self.__contentOfFile:
            i = 0 
            while i < len(line.content):
                ContentAux = Content()
                token = line.content[i]
                if(i+1 < len(line.content)):
                    token2 = line.content[i+1]
                    aux = token + token2
                    if (aux) in self.__token:
                        ContentAux.line = line.line
                        ContentAux.content = self.__token[aux]
                        ContentAux.att = aux
                        self.__Tokens.append(ContentAux)
                        self.__contentOfFile[index].content = self.__contentOfFile[index].content.replace(aux,'')
                    elif(i>0):
                        if(line.content[i-1]==' ' and token2 not in self.__token and token in self.__token):
                            ContentAux.line = line.line
                            ContentAux.content = self.__token[token]
                            ContentAux.att = token
                            self.__Tokens.append(ContentAux) 
                            self.__contentOfFile[index].content = self.__contentOfFile[index].content.replace(token,'')
                else:
                    if (token) in self.__token:
                        ContentAux.line = line.line
                        ContentAux.content = self.__token[token]
                        ContentAux.att = token
                        self.__Tokens.append(ContentAux)
                        self.__contentOfFile[index].content = self.__contentOfFile[index].content.replace(token,'')
                i+=1
            index += 1
    def AnaLex(self):
        res = []
        index = 0
        for i in self.__contentOfFile:
            ContentAux = Content()
            aux = i.content.split()
            for j in aux:
                if(j in self.__keywords):
                    ContentAux.line = i.line
                    ContentAux.content = self.__keywords[j]
                    ContentAux.att = j
                    self.__Tokens.append(ContentAux)
                    self.__contentOfFile[index].content = self.__contentOfFile[index].content.replace(j,'')
            index +=1
        self.evaluateTokensNoAtt()
        for i in self.__contentOfFile:
            splitted = i.content.split()
            for j in splitted:
                ContentAux = Content()
                if(j!=''):
                    atribute = self.regularexpressions(j)
                    ContentAux.line = i.line
                    ContentAux.att = atribute
                    ContentAux.content = j
                    self.__Tokens.append(ContentAux)
        return self.__Tokens

        
