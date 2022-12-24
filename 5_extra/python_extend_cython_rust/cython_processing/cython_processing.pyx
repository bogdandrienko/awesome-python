import numpy as np
cimport numpy as np
cimport cython

cpdef list get_borders_double_loop(np.ndarray[np.float64_t, ndim=1] deposits, int min_length=10):
    cdef int i
    cdef int temp
    cdef list borders = [ ]
    cdef int n_borders
    for i in range(len(deposits)):
        for j in range(len(deposits)):
            temp = 0
        n_borders = len(borders)
        if deposits[i] > 0:
            if n_borders == 0:
                borders.append([i])
            else:
                if i - borders[n_borders - 1][0] >= min_length:
                    borders[n_borders - 1].extend([i])
                    borders.append([i])
    return borders
    