import sympy as sym
import numpy as np
from sympy.utilities.autowrap import autowrap

x = sym.Matrix([1, 2, 3, 4, 5])
y = sym.MatrixSymbol('y', 5, 1)
a = sym.MatrixSymbol('a', 5, 2)
b = sym.MatrixSymbol('b', 5, 2)

eq = sym.Eq(y, x)
auto_odes = autowrap(eq, backend='cython', tempdir='./autowraptmp',
        args=[y, a, b])
