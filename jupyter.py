from sympy import *
import re

x = Symbol('x')

f1 = exp(input('> '))

d = calculus.util.continuous_domain(f1, x, Reals)

domain = input('Domeniu > ')

domain = domain.split(',')

if domain[0]=='R':
    i = Reals
else:
    i = Interval(int(domain[0]), int(domain[1]))

i == d

#f2 = input('derivata 1 > ')

#f3 = input('derivata 2 > ')

#d = diff(f,x)

#d2= diff(d,x)

#d2
