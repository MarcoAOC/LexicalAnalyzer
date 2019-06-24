from Content import Content

def getcontents(filepath):
    #filename = "C:/Users/marco/Documents/GitHub/LexicalAnalyzer/main.txt"
    filename = filepath
    f = open(filename,"r")
    f1 = f.readlines()
    i = 1
    contents = []
    for line in f1:
        aux = Content()
        aux.content = line
        aux.line = i            
        if(aux.content.startswith("//")==False):
            aux.content = aux.content.replace("\n","")
            contents.append(aux)
        if(aux.content == ''):
            contents.pop()
        i=i+1    
    f.close()
    removecommentsblocks(contents)
    return contents

def removecommentsblocks(contents):
    backup = []
    flag = 0
    i = 0
    while i < (len(contents)):
        x = contents[i]
        if(flag == 1):
            if(x.content.find("*/")!= -1):
                backup.append(x)
                contents.pop(i)
                i = i-1
                flag = 0        
            else:
                backup.append(x)
                contents.pop(i)
                i=i-1
        else:
            if(x.content.find("/*")!=-1):
                backup.append(x)
                contents.pop(i)
                i=i-1
                flag = 1
        i=i+1
    if(flag == 1):
        print("Erro com o bloco de comentários")
        exit()
