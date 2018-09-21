from sympy import *

def estimatePi():
    pi = 0
    k = 0
    i = (2*sqrt(2)/9801)*factorial(4*k)*(1103+26390*k)/(factorial(k)**4*396**(4*k))
    while(i>10**-15):
        pi = pi+i
        k = k + 1
        i = (2*sqrt(2)/9801)*factorial(4*k)*(1103+26390*k)/(factorial(k)**4*396**(4*k))
    return 1/pi

a = estimatePi()
print(a.evalf())