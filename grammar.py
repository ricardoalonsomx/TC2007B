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

E -> TE'
E' -> +TE' | -TE' | EMPTY
T -> FT'
T' -> *FT' | /FT' | EMPTY
F -> GF'
F' -> ^GF' | EMPTY
G -> (E)| num | x | sinG | cosG | ... | expG
    
"""

global counter 
counter = 0
stack = []
stack_operators = []
global sentence 
sentence = '(1+2)*3+5'
x = 0

def FindOperator(operator):
    if operator.find('sin') != -1:
        return math.sin
    elif operator.find('cos') != -1:
        return math.cos
    elif operator.find('tan') != -1:
        return math.tan
    elif operator.find('exp') != -1:
        return math.exp
    return None

#Reduction operator 
def reduction(val1, val2, operator):
    #Reduction
    print(val1,val2)
    if operator == '+':
        result = val1 + val2

    elif operator == '-':
        result = val1 - val2
    
    elif operator == '^':
        result = val1 ** val2

    elif operator == '*':
        result = val1 * val2

    elif operator == '/':
        result = val1 / val2

    return result

def GetFirstCharacters():
    sub_counter = counter

    while sentence[sub_counter].isalpha():
        sub_counter += 1

    return sentence[counter:sub_counter], sub_counter

def G():
    print("G")
    S()
    global counter
    if counter < len(sentence) :
        if sentence[counter] == '(':
            counter = counter + 1
            E()
            if counter < len(sentence) :
                if sentence[counter] == ')':
                    counter = counter + 1
                    if len(stack_operators) > 0:
                        val1 = stack.pop()
                        operator = stack_operators.pop()
                        stack.append(operator(val1))
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
            if sentence[counter-1].isdigit():
                stack.append('x')
            else:
                stack.append(x)
            counter += 1
        else:
            sub_sentence, sub_counter = GetFirstCharacters()
            operator = FindOperator(sub_sentence)
            if operator != None:
                stack_operators.append(operator)
                counter = sub_counter
                E()

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

def S():
    global counter
    print("S")
    while counter < len(sentence) and sentence[counter] == ' ':
        counter += 1

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
        operator = sentence[counter]

        if operator == '*' or sentence[counter] == '/' or stack.head() == 'x':
            val2 = stack.pop()
            val1 = stack.pop()

            if val2 == 'x':
                operator = '*'
                val2 = x
            else:
                counter += 1

            F()
            Tp()
            result = reduction(val1, val2, operator)
            stack.append(result)

def F():
    print("F")
    G()
    Fp()

def Fp():
    print("Fp")
    S()
    global counter
    if counter < len(sentence) :
        val2 = stack.pop()
        val1 = stack.pop()

        operator = sentence[counter]
        if operator == "^":
            counter += 1
            G()
            Fp()
            result = reduction(val1, val2, operator)
            stack.append(result)
        

while 1:
    counter = 0
    stack = []
    x  = float(input("Ingresa el valor de X \n"))
    sentence = '(1+2)*3+5'
    sentence = input("Ingresa la cadena a evaluar\n")
    E()
    print("El resultado es: ",stack.pop())
