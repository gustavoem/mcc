import sympy as sym
import numpy as np
from chem import load_large_ode
rhs_of_odes, states = load_large_ode()


from sympy.utilities.autowrap import autowrap

y = sym.MatrixSymbol('y', *states.shape)
state_array_map = dict(zip(states, y))
rhs_of_odes_idxed = rhs_of_odes.xreplace(state_array_map)
dY = sym.MatrixSymbol('dY', *y.shape)
ode_eq = sym.Eq(dY, rhs_of_odes_idxed)
auto_odes = autowrap(ode_eq, backend='cython', tempdir='./autowraptmp')

def auto_odes_wrapper(y, t):
    dY = auto_odes(y[:, np.newaxis])
    return dY.squeeze()

y = np.random.rand(14)
print(auto_odes_wrapper(y, 0))
