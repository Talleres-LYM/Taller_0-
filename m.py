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
            "do", "then", "else", "putCB", "goNorth", 
            "goWest", "goTo", "putcb"]
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

def check_language():
    rta="no"
    for token in tokens:
        if token not in accepted_words:
            rta="no"
    print(rta)


def check_body():
    rta="no"
    open = 0
    closed = 0
    aux = []
    for token in tokens[11:-1]:

        if token == "[":
            new_list = list()
            open +=1
        elif token == "]":
            closed+=1
            new_list.append(token)
        elif open == closed:
            open=0
            closed=0              
        print(new_list)
            

def ejecutar():
    nombre_archivo=input("Ingrese el nombre del archivo: ")
    archivo(nombre_archivo)
    check_language()
ejecutar()