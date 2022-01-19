
# importing modules
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
# method to return function
def function(x):
    return x**3-3*x**2+x-2
  
# method to return its derivative
def deriv(x):
    
    p1= derivative(function, x)
    return p1

def deriv2(x):
  
 p2= derivative(deriv, x)
 return p2
  
#range in x-axis
y = np.linspace(-2, 2)
  
# plotting function
plt.plot(y, function(y), color='brown', label='Function')
  
# plotting its derivative
plt.plot(y, deriv(y), color='blue', label='Derivative')

plt.plot(y, deriv2(y), color='red', label='Derivative2')
  
# changing limits of y-axis
plt.gca().spines['left'].set_position('zero',)
  
# changing limits of x-axis
plt.gca().spines['bottom'].set_position('zero',)
plt.legend(loc='upper left')
  
# plotting text in the graph
plt.text(5.0, 1.0, r"f'(x)", horizontalalignment='center',
         fontsize=18, color='blue')
  
plt.text(-4.4, 25.0, r'f(x)', horizontalalignment='center',
         fontsize=18, color='brown')

plt.text(0.0, -25.0, r"f''(x)", horizontalalignment='center',
         fontsize=18, color='red')

plt.grid(True)
plt.show()
