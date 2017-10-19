import sys
sys.path.insert (0, '../ex4/')
sys.path.insert (0, '../utils/')

from utils import *

def next_state (x_t1, M):
    M = np.array (M)
    x_t2 = x_t1 +  np.dot (M, np.transpose (x_t1))
    return apply_state_threshold (x_t2)
        

def apply_gene_threshold (xi):
    if (xi > 0):
        return 1
    else:
        return 0


def apply_state_threshold (state):
    for i in range (len (state)):
        state[i] = apply_gene_threshold (state[i])
    return state


def p_perturbation (x_t1, x_t2, p):
    if (np.array_equal (x_t1, x_t2)):
        return 0

    n = len (x_t1)
    count = 0
    for i in range (n):
        if (x_t1[i] != x_t2[i]):
            count += 1
    return (p ** count) * ((1 - p) ** (n - count))


def p_transition (x_t1, x_t2, M, p):
    n = len (x_t1)
    bool_next_state = next_state (x_t1, M)
    transition_p = 0.0
    if (np.array_equal (x_t2, bool_next_state)):
        transition_p += (1 - p) ** n
    transition_p += p_perturbation (x_t1, x_t2, p)
    return transition_p


input_buffer = []
n = int (buffered_input (input_buffer))
p = float (buffered_input (input_buffer))
M = []
for i in range (n):
    M.append ([])
    for j in range (n):
        M[i].append (int (buffered_input (input_buffer)))

P = []
for i in range (2 ** n):
    P.append ([])
    x_t1 = int_to_binary_array (n, i)
    # print ("".join (x_t1.astype (str).tolist ()) + " -> " + "".join (next_state (x_t1, M).astype (str).tolist ()))
    for j in range (2 ** n):
        x_t2 = int_to_binary_array (n, j)
        p_tran = p_transition (x_t1, x_t2, M, p)
        P[i].append (p_tran)


print (P)
print_latex_representation (P, n)
