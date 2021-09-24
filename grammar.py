import math
import json

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
global x
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
    elif operator.find('sqrt') != -1:
        return math.sqrt
    return None

#Reduction operator 
def reduction(val1, val2, operator):
    #Reduction
    #print(val1,val2)
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
    # print("G")
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
            while counter < len(sentence) and (sentence[counter].isdigit() or sentence[counter] == "."):
                sub_cadena = sub_cadena + sentence[counter]
                counter = counter + 1
            stack.append(float(sub_cadena))
        elif sentence[counter] == 'x':
            if counter > 0 and sentence[counter-1].isdigit():
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
    #print("E")
    T()
    Ep()

# Regla 3
def T():
    #print("T")
    F()
    Tp()

def S():
    global counter
    #print("S")
    #if len(stack) > 0:
        #print(stack[len(stack) - 1])
    #else:
        #print("empty stack")
    while counter < len(sentence) and sentence[counter] == ' ':
        counter += 1

# Regla 2
def Ep():
    #print("Ep")
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
    # print("Tp")
    S()
    global counter
    if counter < len(sentence) :
        operator = sentence[counter]

        #print(sentence[counter])
        if operator == '*' or sentence[counter] == '/' or sentence[counter] == 'x': # 2*x^(23-x)+3  2 x 23 x 3
            
            if sentence[counter] != 'x':
                counter += 1
            F()
            Tp()

            val2 = stack.pop()
            val1 = stack.pop()

            if val2 == 'x':
                operator = '*'
                val2 = x

            result = reduction(val1, val2, operator)
            stack.append(result)

def F():
    # print("F")
    G()
    Fp()

def Fp():
    # print("Fp")
    S()
    global counter
    if counter < len(sentence) :
        
        operator = sentence[counter]
        if operator == "^":
            counter += 1
            G()
            Fp()
            val2 = stack.pop()
            val1 = stack.pop()
            
            result = reduction(val1, val2, operator)
            stack.append(result)
    
    
def calc(expression):
    global sentence
    global x
    global counter
    global stack
    #x  = float(input("Ingresa el valor de X \n"))
    #sentence = '(1+2)*3+5'
    ans = []
    for i in range(-10, 11):
        
        counter = 0
        stack = []
        sentence = expression
        x = i
        E()
        result = stack.pop()
        ans.append(result)
        
        #print("El resultado es: ", result)

    return ans

    toFile = json.dumps(ans)
    file = open("./jsonDump.json", 'w')
    file.write(toFile)
    file.close()

def evaluate(val, expression):
    global sentence
    global x
    global counter
    global stack
    counter = 0
    stack = []
    x = val
    E()
    sentence = expression
    return stack.pop()