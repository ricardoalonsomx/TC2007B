import math


#Definicion de la gramatica
#eliminar la recursion por la izquierda
"""
E -> TE'
E' -> +TE' | -TE' | EMPTY
T -> FT'
T' -> *FT' | /FT' | EMPTY
F -> (E)| N
S -> ..
"""

counter = 0
stack = []
sentence = '(1+2)*3+5'
x = 0
#Reduction operator 
def reduction(val1, val2, operator):
    #Reduction
    print(val1,val2)
    if operator == '+':
        result = val1 + val2

    elif operator == '-':
        result = val1 - val2

    elif operator == '*':
        result = val1 * val2

    elif operator == '/':
        result = val1 / val2

    return result

# Regla 1
def E():
    print("E")
    T()
    Ep()
# Regla 3
def T():
    print("T")
    F()
    Tp()

# Regla 2
def Ep():
    print("Ep")
    S()
    global counter
    if counter < len(sentence) :
        if sentence[counter] == '+' or sentence[counter] == '-':
            operator = sentence[counter]
            counter = counter + 1
            T()
            Ep()
            val2 = stack.pop()
            val1 = stack.pop()
            result = reduction(val1, val2, operator)
            stack.append(result)


def Tp():
    print("Tp")
    S()
    global counter
    if counter < len(sentence) :
        if sentence[counter] == '*' or sentence[counter] == '/':
            operator = sentence[counter]

            counter = counter + 1
            F()
            Tp()
            val2 = stack.pop()
            val1 = stack.pop()
            result = reduction(val1, val2, operator)
            stack.append(result)

def F():
    print("F")
    S()
    global counter
    if counter < len(sentence) :
        if sentence[counter] == '(':
            counter = counter + 1
            E()
            if counter < len(sentence) :
                if sentence[counter] == ')':
                    counter = counter + 1
                else:
                    print ("Error en la sentencia")
        elif sentence[counter].isdigit():
            #Reconomos todos los digitos
            sub_cadena = ''
            while counter < len(sentence) and sentence[counter].isdigit():
                sub_cadena = sub_cadena + sentence[counter]
                counter = counter + 1
            stack.append(float(sub_cadena))
        elif sentence[counter] == 'x':
            stack.append(x)
            counter = counter + 1

def S():
    global counter
    print("S")
    while counter < len(sentence) and sentence[counter] == ' ':
        counter += 1

while 1:
    counter = 0
    stack = []
    x  = float(input("Ingresa el valor de X \n"))
    sentence = '(1+2)*3+5'
    sentence = input("Ingresa la cadena a evaluar\n")
    E()
    print("El resultado es: ",stack.pop())


