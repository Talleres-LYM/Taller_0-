from ast import Str
from lib2to3.pgen2.parse import ParseError
keywords = ["ROBOT_R","VARS", "PROCS", 
            "assignTo","goto","move",
            "turn","face","put","pick",
            "moveToThe","run-dirs",
            "movInDir","jumpToThe",
            "jumpInDir","nop","if",
            "while", "repeat"]
variables= {}
orientations=["left","right","around"]
cardinals=["north","south","west","east"]
directions=["left","front","right","back"]
objects=["balloons","chips"]
tokens= []  

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

def archivo(nombre_archivo:str):
    txtfile = open(nombre_archivo, "r")
    
    for linea in txtfile:
    
        global comandcode
        comandcode += " "+linea
    global tokens
    tokens = comandcode.split()     
    if tokens[0] != "[":
        raise ParseError("no")    

def ejecutar():
    nombre_archivo=input("Ingrese el nombre del archivo: ")
    try:
        archivo(nombre_archivo)
        print("Yes")
    except:
        print("no")
    
ejecutar()