# distutils: sources = c_odes.c

import cython
cimport c_odes_def
cimport numpy as cnp
import numpy as np

def cy_odes(cnp.ndarray[cnp.double_t, ndim=1] y, double t):
    # preallocate our output array
    cdef cnp.ndarray[cnp.double_t, ndim=1] dY = np.empty(y.size, \
            dtype=np.double)
    # now call the C function
    c_odes_def.c_odes(<double *> y.data, <double *> dY.data)
    return dY
