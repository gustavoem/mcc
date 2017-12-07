import sys
sys.path.insert (0, '../utils/')

from utils import *


# Calculates the next state according to the Boolean Network function
def next_state (x_t1, M):
    M = np.array (M)
    x_t2 = x_t1 +  np.dot (M, np.transpose (x_t1))
    return apply_state_threshold (x_t2)
        

# Applies threshold on gene value
def apply_gene_threshold (xi):
    if (xi > 0):
        return 1
    else:
        return 0

# Applies threshold on state
def apply_state_threshold (state):
    for i in range (len (state)):
        state[i] = apply_gene_threshold (state[i])
    return state


# Calculates the probability of transitioning from x_t1 to x_t2 on a 
# time step with only bit inversions (not counting probability of this
# event when x_t2 = f (x_t1)).
def p_perturbation (x_t1, x_t2, p):
    if (np.array_equal (x_t1, x_t2)):
        return 0
    n = len (x_t1)
    count = 0
    for i in range (n):
        if (x_t1[i] != x_t2[i]):
            count += 1
    return (p ** count) * ((1 - p) ** (n - count))


# Calculates the probability of transitioning from state x_t1 to state
# x_t2 on a time step 
def p_transition (x_t1, x_t2, M, p):
    n = len (x_t1)
    bool_next_state = next_state (x_t1, M)
    transition_p = 0.0
    if (np.array_equal (x_t2, bool_next_state)):
        transition_p += (1 - p) ** n
    transition_p += p_perturbation (x_t1, x_t2, p)
    return transition_p


# Calculates the transition matrix of the PBN with bit inversion model 
def get_invertion_transition_p (n, M, p):
    P = []
    for i in range (2 ** n):
        P.append ([])
        x_t1 = int_to_binary_array (n, i)
        for j in range (2 ** n):
            x_t2 = int_to_binary_array (n, j)
            p_tran = p_transition (x_t1, x_t2, M, p)
            P[i].append (p_tran)
    return P
