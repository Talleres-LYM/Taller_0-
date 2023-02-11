accepted_words = ["ROBOT_R","VARS", "PROCS", 
            "assignTo","goto","move",
            "turn","face","put","pick",
            "moveToThe", "moveInDir","jumpToThe",
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
            "do", "then", "else", "putCB", "goNorth", 
            "goWest", "goTo", "putcb", "facing", "canPut",
            "canPick", "canMoveInDir", "canJumpInDir",
            "canMoveToThe", "canJumpToThe", "not"]
tokens= []  
leer =""

def archivo(nombre_archivo:str):
    txtfile = open(nombre_archivo, "r")
    for linea in txtfile:
        global leer
        leer += " "+linea
    global tokens
    tokens = leer.split()       
    

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

def check_language(lista):
    rta="yes"
    for token in lista:
        if token not in accepted_words:
            rta="no"
    return rta


def check_body():
    rta1="yes"
    count = 1
    i = 13
    aux = []
    while i < len(tokens):
        aux.append(tokens[i])
        if tokens[i] == "[":
            count += 1
        if tokens[i] == "]":
            count -= 1
        if count == 0:
            i += 1 
        i += 1
    if check_language(aux) == "no":
        rta1 = "no"        
    if count != 0:
        rta1 = "no"
    print(rta1)
            

def ejecutar():
    nombre_archivo=input("Ingrese el nombre del archivo: ")
    archivo(nombre_archivo)
    check_body()
ejecutar()