import sympy as sym

x, y = sym.symbols('x y')
expr = 3 * x ** 2 + sym.log(x ** 2 + y ** 2 + 1)
print(expr.subs({x: 17, y:42}).evalf())
# Problem: this is slow /\

g = sym.lambdify([x, y], expr, modules=['math'])
print(g(17, 42))

z = z1, z2, z3 = sym.symbols('z:3')
expr2 = x * y * (z1 + z2 + z3)
func2 = sym.lambdify([x, y, z], expr2)
print(func2(1, 2, (3, 4, 5)))

# Exercise: Create a function from a symbolic expression
# Plot z(x, y) = d2f(x,y)/dxdy as a surface plot for -5 < x < 5, 
# -5 < y  < 5
d2fdxdy = expr.diff(expr, x, y)
func = sym.lambdify([x, y], d2fdxdy)


