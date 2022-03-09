from sympy import *
import re

x = Symbol('x')

punctaj = 0

for i in range(5):

    a = input('\nIntrodu Functia > ')

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

    f1 = sympify(input('\nIntrodu Derivata 1 > '))

    d = diff(f,x)

    if(f1.subs(x,1)!=d.subs(x,1)):
        print("Incorect")
        continue
    else:
        punctaj = punctaj+1

    f2 = sympify(input('\nIntrodu Derivata 2 > '))

    d2= diff(d,x)

    if(f2.subs(x,1)!=d2.subs(x,1)):
        print("Incorect")
        continue
    else:
        punctaj = punctaj+1
    


print(f"\nFelicitari! Ai {punctaj} din 10 puncte")

