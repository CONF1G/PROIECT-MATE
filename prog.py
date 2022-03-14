from sympy import *
import re

x = Symbol('x')


def Domain_Chk(f, d):
    f = sympify(f)
    if d == 'R':
        d = Reals
    dom = calculus.util.continuous_domain(f, x, Reals)
    if d == dom:
        return True
    else:
        return False


def D1_Chk(f, d):
    f = sympify(f)
    d = sympify(d)
    deriv = diff(f,x)
    if(d.subs(x,1) == deriv.subs(x,1)):
        return True
    else:
        return False


def D2_Chk(f, d):
    f = sympify(f)
    d = sympify(d)
    deriv = diff(f,x,x)
    if(d.subs(x,1) == deriv.subs(x,1)):
        return True
    else:
        return False


"""

f = sympify(input('> '))

d = calculus.util.continuous_domain(f, x, Reals)



domain = input('Domeniu > ')

domain = domain.split('\| |{|}|,|[|]|(|)')


print(domain)

if domain[0]=='R':
    i = Reals
else:
    i = Interval(int(domain[0]), int(domain[1]))

print(i == d)



f1 = sympify(input('derivata 1 > '))

d = diff(f,x)

if(f1.subs(x,1)!=d.subs(x,1)):
    print(d)
    exit(1)

f2 = sympify(input('derivata 2 > '))

d2= diff(d,x)

if(f2.subs(x,1)!=d2.subs(x,1)):
    print(d2)
    exit(1)


print("Congrats!!!!1")

"""
