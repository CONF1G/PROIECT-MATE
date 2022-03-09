from sympy import *
import re

x = Symbol('x')

a = input('> ')

f = sympify(a)

d = calculus.util.continuous_domain(f, x, Reals)

"""

domain = input('Domeniu > ')

domain = domain.split('\| |{|}|,|[|]|(|)')


print(domain)

if domain[0]=='R':
    i = Reals
else:
    i = Interval(int(domain[0]), int(domain[1]))

print(i == d)

"""

f1 = sympify(input('derivata 1 > '))

d = diff(f,x)

if(f1.subs(x,1)!=d.subs(x,1)):
    print("Incorect")
    exit(1)

f2 = sympify(input('derivata 2 > '))

d2= diff(d,x)

if(f2.subs(x,1)!=d2.subs(x,1)):
    print("Incorect")
    exit(1)


print("Felicitari!")


"""
CE ESTE COMENTAT AICI ESTE GRAFICUL
    -derivate
    +graficul functiei
    +domeniu functiei
    
    

# importing modules
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
  
# method to return function
def function(y):
    a = []
    for i in y:
        a.append(f.subs(x,i))
    return a
  
# method to return its derivative
def deriv(y):
    b = [];
    for i in y:
        b.append(d.subs(x,i))
    return b

def deriv2(y):
    c = []
    for i in y:
        c.append(d2.subs(x,i))
    return c

#range in x-axis
y = np.linspace(-6, 6)
  
# plotting function
plt.plot(y, function(y), color='brown', label='Function')
  
# plotting its derivative
#plt.plot(y, deriv(y), color='blue', label='Derivative')

#plt.plot(y, deriv2(y), color='green', label='Derivative 2')
  
# changing limits of y-axis
plt.gca().spines['left'].set_position('zero',)
  
# changing limits of x-axis
plt.gca().spines['bottom'].set_position('zero',)
plt.legend(loc='upper left')
  
# plotting text in the graph

plt.grid(True)

"""
