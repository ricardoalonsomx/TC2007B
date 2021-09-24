import math
import pandas as pd
from grammar import *

"""
Solución al problema
"""
def df(x,f):
    h = 0.00001
    return (evaluate(x+h, f) - evaluate(x, f)) / h
    #return (f(x+h) - f(x)) / h

#Version 1
#Newton
def newton(x0,f):
    result = {}
    x_n  = x0
    x_n_1 = x_n + 0.01
    step = x_n_1-x_n
    count = 0
    while abs(step) > 0.00001 and count < 100000:
        denominator = df(x_n,f)
        if denominator != 0:
            x_n_1 = x_n - evaluate(x_n, f) / denominator
        else:
            result['value'] = -1
            result['message'] = 'Error div zero'
            return result
        step = x_n_1-x_n
        x_n = x_n_1
        count += 1

    if abs(evaluate(x_n, f)) < 0.00001:
        result['value'] = x_n
        result['message'] = 'solution'
    else:
        result['value'] = -1
        result['message'] = 'Error no root'
    return result

#Version 2
#Biseccion
def bisection(f, a, b):
    result = {}
    if f(a)*f(b) >= 0:
        result['value'] = -1
        result['message'] = 'Error a & b same sign'
        return result
    a_n = a
    b_n = b
    for n in range(1000000):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
        elif abs(f_m_n) < 0.00001:
            result['value'] = m_n
            result['message'] = 'solution'
            return result
        else:
            result['value'] = -1
            result['message'] = 'Root not found'
            return result

    result['value'] = (a_n + b_n)/2
    result['message'] = 'solution'
    return result