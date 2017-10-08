import sys
sys.path.insert (0, '../utils/')

from utils import *
import numpy as np
import math


# Calculates signal coming into a gene i
def calculate_H_i (i, M, x):
    M = np.array (M)
    x = np.transpose (np.array (x))
    h = sum (M[i][:] * x)
    return h


# Calculates the probability o the gene's next state 
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


# Calculates the probability of the next state
def p_transition (x1, x2, M, alpha, betha):
    n = len (x1)
    total_p = 1
    for i in range (n):
        gen_p = p_gen_change (i, x1, x2, M, alpha, betha)
        total_p *= gen_p
    return total_p


input_buffer = []
n = int (buffered_input (input_buffer))
alpha = float (buffered_input (input_buffer))
betha = float (buffered_input (input_buffer))
M = []
for i in range (n):
    M.append ([])
    for j in range (n):
        M[i].append (int (buffered_input (input_buffer)))

P = []
for i in range (2 ** n):
    P.append ([])
    x_t1 = int_to_binary_array (n, i)
    for j in range (2 ** n):
        x_t2 = int_to_binary_array (n, j)
        p = p_transition (x_t1, x_t2, M, alpha, betha)
        P[i].append (p)
print (P)
print_latex_representation (P, n)
