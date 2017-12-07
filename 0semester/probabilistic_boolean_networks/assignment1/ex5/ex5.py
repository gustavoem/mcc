import sys
sys.path.insert (0, '../perturbation_model/')
sys.path.insert (0, '../utils/')

from utils import *
from invert_bit_model import get_invertion_transition_p 


input_buffer = []
n = int (buffered_input (input_buffer))
p = float (buffered_input (input_buffer))
M = []
for i in range (n):
    M.append ([])
    for j in range (n):
        M[i].append (int (buffered_input (input_buffer)))

P = get_invertion_transition_p (n, M, p)

print (P)
# print_latex_representation (P, n)
