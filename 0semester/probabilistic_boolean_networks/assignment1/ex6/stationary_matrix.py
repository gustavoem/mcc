import sys
import numpy as np

def get_stationary_matrix (P):
    Pk = P
    Pkn = np.dot (P, P)
    while (my_norm (Pkn - Pk) > 1e-10):
        Pk = Pkn
        Pkn = np.dot (Pkn, P)
    return Pkn


# I used matrix 1-norm to calculate the matrix norm here, which is 
# taking the highest sum of elements of a column
def my_norm (P):
    return np.linalg.norm (P, 1)
