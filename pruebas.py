import pandas as pd
import math
import numpy as np
#from Parser import *
from grammar import *
from rootFinder import *
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


if __name__ == '__main__':
    testExpressions = ["1+1", "2*2", "(2+5)*4", "sin(2)", "cos(2)", "sqrt(2)", "10 / 2", "2*x", "(x+4)/2", "x*x", "x^(x + 2)", "x*exp(x)", "22.22+12"]
    # Do not test -> invalidValues = ["+=1", "1/ ", "xx", "5x", "#", "((12+12)", ")(12)", "--12", "x* *12", "45. 2*12", "x.3+1", "4.x - 12", "1\""]
    def f1(x):
        return 1+1

    def f2(x):
        return 2*2

    def f3(x):
        return 4*(2+5)

    def f4(x):
        return math.sin(2)

    def f5(x):
        return math.cos(2)

    def f6(x):
        return math.sqrt(2)

    def f7(x):
        return 10/2

    def f8(x):
        return 2*x

    def f9(x):
        return (x+4)/2

    def f10(x):
        return x*x

    def f11(x):
        return x**(x+2)

    def f12(x):
        return x*math.exp(x)

    def f13(x):
        return 22.22+12
    
    realExpressions = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13]

    def calc2(y):
        ans = []

        for i in range(-10, 11):
            ans.append(y(i))
        return ans

    for i in range(len(testExpressions)):
        ans1 = np.array(calc2(realExpressions[i]))
        ans2 = np.array(calc(testExpressions[i]))
        if not np.array_equal(ans1, ans2):
            print("Error en expresión", i)
        print("Expresión", i, "resuelta")
        #print(ans1, ans2)

    for i in range(len(testExpressions)):
        print(newton(0, testExpressions[i]))
    
    def selenium():
        # Poner path de driver de compu de fer
        driver = webdriver.Chrome("./ChromeDriver/chromedriver.exe")
        # driver.get("index.html")
        driver.get("file:///Users/ferna/OneDrive/Desktop/tec/5to Semestre/testing/aplicacionWEB/TC2007B.100")
        driver.find_element_by_id("function").send_keys("2*4+x")
        driver.close()