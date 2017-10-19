import sys
import numpy as np
sys.path.insert (0, '../utils')

def get_stationary_matrix (M):
    Mk = M
    Mkn = np.dot (M, M)
    while (my_norm (Mkn - Mk) > 1e-8):
        Mk = Mkn
        Mkn = Mkn * M
    return Mkn


# I used 1-norm to calculate the matrix norm here
def my_norm (M):
    return np.linalg.norm (M, 1)
