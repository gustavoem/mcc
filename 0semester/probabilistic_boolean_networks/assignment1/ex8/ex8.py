import sys
sys.path.insert (0, '../utils/')
sys.path.insert (0, '../perturbation_model/')
sys.path.insert (0, '../ex6/')
sys.path.insert (0, '../ex7/')

from utils import *
import numpy as np
import math
from stationary_matrix import get_stationary_matrix
from alpha_beta_model import get_alpha_beta_transition_p
from flux_matrix import get_flux_matrix

# Reads network from user input
input_buffer = []
n = int (buffered_input (input_buffer))
alpha = float (buffered_input (input_buffer))
beta = float (buffered_input (input_buffer))
M = []
for i in range (n):
    M.append ([])
    for j in range (n):
        M[i].append (int (buffered_input (input_buffer)))

# Calculates transition probability matrix
P = get_alpha_beta_transition_p (n, M, alpha, beta)

# Calculates stationary distribution 
Pi_matrix = get_stationary_matrix (P) 
stationary_distribution = Pi_matrix[0]
# print (stationary_distribution)

# Calculates flux matrix
F = get_flux_matrix (stationary_distribution, P)

print (F)
