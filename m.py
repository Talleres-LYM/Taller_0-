from ast import Str
from lib2to3.pgen2.parse import ParseError
accepted_words = ["ROBOT_R","VARS", "PROCS", 
            "assignTo","goto","move",
            "turn","face","put","pick",
            "moveToThe", "movInDir","jumpToThe",
            "jumpInDir","nop","if",
            "while", "repeat", "left",
            "right","around", "north",
            "south","west","east", "left",
            "front","right","back", "balloons",
            "chips", "[","]", "|", ":", ";", ",", 
            "nom", "x", "y", "one", "two","three",
            "four","five","six","seven","eight",
            "nine", "zero", "1", "2","3","4",
            "5","6","7", "8", "9", "0", "c", "b",
            "do", "then", "else"]
variables= {}
tokens= []  
comandcode =""
""""
def run():
    counter= 0
    for i in tokens:
        counter +=1
        if i == "]":
            break
        
    for i in range(0,counter):
        if i != (counter-1):
            if tokens[i] != (":") and tokens[i] not in directions:
                raise ParseError("no")
            if tokens[i] == (":"):
                if tokens[i+1] not in directions:
                    raise ParseError("no")
            if tokens[i] in directions:
                if tokens[i+1] != (":"):
                    raise ParseError("no")
        else:
            if tokens[i] not in directions:
                raise ParseError("no")
            if tokens[i+1] != "]":
                raise ParseError("no")
    for i in range(0,(counter+1)):
        tokens.remove(tokens[0])

def ifblock():
    iflist=[]
    if tokens[0] != "[":
        raise ParseError("no")
    tokens.remove(tokens[0])
    if tokens[0] == "facing" or tokens[0]=="canMoveInDir" or tokens[0]=="canJumpInDir":
        if tokens[1] not in cardinals:
            raise ParseError("no")
        if tokens[2] != "]":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        ifparser()
    elif  tokens[0] == "canPut" or tokens[0] == "canPick":
        if tokens[1] not in objects:
            raise ParseError("no")
        if tokens[2] not in variables:
             value= int(tokens[2])
        if tokens[3] != "]":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        ifparser()
    if tokens[0]=="canMoveToThe" or tokens[0]=="canJumpToThe":
        if tokens[1] not in directions:
            raise ParseError("no")
        if tokens[2] != "]":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        ifparser()
    elif tokens[0] == "not":
        if tokens[2] != "]":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        ifparser()


def ifparser():
    global tokens
    iflist=[]
    counteropen= 1
    counterclosed= 0
    position= 0
    for token in tokens:
        if token == "]":
            counterclosed+=1
        elif token == "[":
            counteropen +=1
        if counteropen == counterclosed:
            break
        position +=1
    for i in range(0,(position+1)):
        iflist.append(tokens[i])
        
    
    tokensbackup= tokens.copy()
    tokens= iflist
    tokens= tokensbackup
    for i in range(0,(position+1)):
        tokens.remove(tokens[0])
        
    
    
    

def newvar(varname:str,varval:int):
    variables[varname]= varval
"""
def archivo(nombre_archivo:str):
    txtfile = open(nombre_archivo, "r")
    
    for linea in txtfile:
    
        global comandcode
        comandcode += " "+linea
    global tokens
    tokens = comandcode.split()       
    

def check_headline():
    rta="no"
    headers=[]
    i=0
    for token in tokens:
        if token not in accepted_words:
          print(rta)
    while tokens[i] != "PROCS":
        headers.append(tokens[i])
        i+=1
    if len(headers) == 10:    
        rta="yes"
    print(rta)


def check_body():
    rta="no"
    open = 0
    closed = 0
    for token in tokens[11:-1]:
        new_list = list()
        if token not in accepted_words:
          print(rta)
        elif token == "]":
            closed+=1
        elif token == "[":
            
            open +=1
        elif open == closed:
            new_list.append(token)
            open=0
            closed=0              
        print(new_list)
            

def ejecutar():
    nombre_archivo=input("Ingrese el nombre del archivo: ")
    archivo(nombre_archivo)
    check_headline()   
    check_body()
ejecutar()