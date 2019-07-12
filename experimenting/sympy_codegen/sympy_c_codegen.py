import sympy as sym
def python_fib(n):
    a = 0
    b = 1
    for i in range(n):
        tmp = a
        a = a + b
        b = tmp
    return a


from chem import load_large_ode
rhs_of_odes, states = load_large_ode()
print(rhs_of_odes[0])


from sympy.utilities.codegen import codegen
# codegen(name_expr, language=None)
# (c_filename c_source_code), (header_file_name, header source code)
[(cf, cs), (hf, hs)] = codegen(('c_odes', rhs_of_odes), language='c')
print(cs)


y = sym.MatrixSymbol('y', *states.shape)
print(y)

# We need to replace the use of y0, y1 with the elements of our matrix
# symbol. 
state_array_map = dict(zip(states, y))
# print(state_array_map)

rhs_of_odes_idxed = rhs_of_odes.xreplace(state_array_map)
[(cf, cs), (hf, hs)] = codegen(('c_odes', rhs_of_odes_idxed), \
        language='c')
# print(cs)

dY = sym.MatrixSymbol('dY', *y.shape)
ode_eq = sym.Eq(dY, rhs_of_odes_idxed)
# [(cf, cs), (hf, hs)] = codegen(('c_odes', ode_eq), language='c')
# print(cs)

codegen(('c_odes', ode_eq), language='c', to_files=True)
