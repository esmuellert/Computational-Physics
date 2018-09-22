import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def graph():
    names1 = ['0','a/2','a']
    names2 = ['0','Aa/2','0']
    plt.plot(names1,names2)
    plt.ylabel('psi')
    plt.xlabel('x')
    plt.show()

def equ1():
    a,A,x = symbols('a,A,x')
    n = symbols('n',positive = True,integer = True)
    A = 2*sqrt(3)/sqrt(a**3)
    c_n = A*sqrt(2/a)*(integrate(x*sin(n*pi*x/a),(x,0,a/2))+integrate((a-x)*sin(n*pi*x/a),(x,a/2,a)))
    return c_n

graph()
