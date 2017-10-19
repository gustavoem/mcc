import sys
import numpy as np

def get_flux_matrix (stationary_distr, P):
    P = np.array (P)
    F = np.empty (P.shape)
    for i in range (P.shape[0]):
        for j in range (P.shape[1]):
            F[i, j] = calc_flux (i, j, stationary_distr, P)
    return F


def calc_flux (i, j, stationary_distr, P):
    p = stationary_distr
    return p[i] * P[i][j] - p[j] * P[j][i]

