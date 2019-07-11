from sympy import *

x = symbols('x')
expr = abs(sin(x**2))
print(expr)
print(ccode(expr))
print(julia_code(expr))
print(octave_code(expr))
