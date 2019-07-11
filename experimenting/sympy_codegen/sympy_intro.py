from sympy import *
import numpy as np

# Write the pdf of Normal distribution
mu, s, x, y = symbols('mu s x y')
norm = 1 / sqrt(2 * np.pi * s * s) * \
        exp((x - mu) * (x - mu) / (2 * s * s))
print(norm)

# Common gotchas
# rational numbers vs float
print(x + 1 / 2)
print(x + S(1) / 2)

# All expressions are immutable

# Floating point representation
# Exercise: show 100 digits of pi
print(pi.evalf(100))

# Undefined functions
f = Function('f')
f(x) + 1
print(diff(sin(x + 1) * cos(y), x, y))

# Exercise: write an expression representing the wave equation in one
# dimension:
u = Function('u')
t, c = symbols('t c')
expr = Eq(diff(u(t, x), t, t), c ** 2 * diff(u(t, x), x, x))
print(expr)

# Matrices
print (Matrix([[1, 2], [3, 4]]))

# Exercise
z = symbols('z')
M = Matrix([[1, 0, 1], [-1, 2, 3], [1, 2, 3]])
xyz = Matrix([[x], [y], [z]])
sys = M * xyz
print(sys)
print(sys.jacobian([x, y, z]))


# Matrix symbols
M = MatrixSymbol("M", n, m) # n and m are the shape of M

