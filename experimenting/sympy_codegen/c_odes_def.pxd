import numpy as np
cimport numpy as cnp

cdef extern from "c_odes.h":
    void c_odes(double *y, double *dY)
