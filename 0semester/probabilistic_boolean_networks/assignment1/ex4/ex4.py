import sys
sys.path.insert (0, '../utils/')
sys.path.insert (0, '../perturbation_model')

from utils import *
from alpha_beta_model import get_alpha_beta_transition_p 

input_buffer = []
n = int (buffered_input (input_buffer))
alpha = float (buffered_input (input_buffer))
beta = float (buffered_input (input_buffer))
M = []
for i in range (n):
    M.append ([])
    for j in range (n):
        M[i].append (int (buffered_input (input_buffer)))

P = get_alpha_beta_transition_p (n, M, alpha, beta)

print (P)
print_latex_representation (P, n)
