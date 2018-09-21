from sympy import *
from sympy.physics.units import hbar
init_printing(use_unicode=True) #显示latex公式

x,a,psi = symbols('x,a,psi')
n = symbols('n',integer=True,positive = True);

b = 2/a*integrate(x*(sin(n*pi*(x/a)))**2,(x,0,a))

print(psi)

c = -(hbar**2)*integrate((sin(n*pi*(x/a)))*sqrt(2/a).conjugate()*diff((sin(n*pi*(x/a)))*sqrt(2/a),x,2),(x,0,a))

print(c)