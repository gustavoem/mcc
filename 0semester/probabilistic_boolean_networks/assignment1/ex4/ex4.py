import numpy as np
import math

input_buffer = []
def buffered_input ():
    if (len (input_buffer) == 0):
        line_str = input ()
        line_arr = line_str.split ()
        input_buffer.extend (line_arr)
    res = input_buffer.pop (0)
    return res


def calculate_H_i (i, M, x):
    M = np.array (M)
    x = np.transpose (np.array (x))
    h = sum (M[i][:] * x)
    return h


def int_to_binary_array (n, x):
    b = np.zeros (n)
    i = n - 1
    while x > 0:
        digit = x % 2
        x = x // 2
        b[i] = digit
        i -= 1
    return b.astype (int)


def p_gen_change (i, x1, x2, M, alpha, betha):
    h = calculate_H_i (i, M, x1)
    p = 0
    if (h == 0):
        p_keep = 1 / (1 + math.exp (-alpha))
        if (x1[i] == x2[i]):
            p = p_keep
        else:
            p = 1 - p_keep
    else:
        if (x2[i] == 0):
            p = math.exp (-betha * h)
        else:
            p = math.exp (betha * h)
        p /= (math.exp (-betha * h) + math.exp (betha * h))
    return p


def p_transition (x1, x2, M, alpha, betha):
    n = len (x1)
    total_p = 1
    for i in range (n):
        gen_p = p_gen_change (i, x1, x2, M, alpha, betha)
        total_p *= gen_p
    return total_p

def int_to_binary_string (n, x):
    return "".join (int_to_binary_array (n, x).astype(str).tolist ())


n = int (buffered_input ())
alpha = float (buffered_input ())
betha = float (buffered_input ())
M = []
for i in range (n):
    M.append ([])
    for j in range (n):
        M[i].append (int (buffered_input ()))

P = []
for i in range (2 ** n):
    P.append ([])
    x_t1 = int_to_binary_array (n, i)
    for j in range (2 ** n):
        x_t2 = int_to_binary_array (n, j)
        p = p_transition (x_t1, x_t2, M, alpha, betha)
        P[i].append (p)

print (P)

for j in range (2 ** n):
    print ("& " + int_to_binary_string (n, j), end=" ")
print ("\\\ ", end="")

for i in range (2 ** n):
    print ("\n" + int_to_binary_string (n, i), end=" ")
    for j in range (2 ** n):
        if (P[i][j] < 1e-2):
            p_str = "{:.2e}".format (P[i][j])
        else:
            p_str = "{:.2}".format (P[i][j])
        print ("& " + p_str, end=" ")
    print ("\\\\", end="")

