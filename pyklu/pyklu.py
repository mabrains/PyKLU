# Copyright (C) 2015 kagami-c
# Licensed under LGPL-2.1

'''
Please use this script as a module.

Detailed usage:

1. Import solver in PyKLU

  >>> from pyklu import solve_linear_system

2. Use solver by inputting NumPy ndarray

  >>> solver_linear_system(n, Ap, Ai, Ax, b)

n, Ap, Ai, Ax, b are numpy.ndarray object in this statement.

More details about these inputs are in the Manual of KLU Library
in SuiteSparse(http://faculty.cse.tamu.edu/davis/suitesparse.html)
'''

import ctypes
import numpy
import scipy.sparse as sparse
import os

__all__ = ['solve_linear_system']

if __name__ == '__main__':
    print(__doc__)

package_path = os.path.dirname(os.path.abspath(__file__))
libklu = ctypes.cdll.LoadLibrary(os.path.join(package_path, 'libpyklu.so'))


def solve_linear_system(A, b):
    Ap = A.indptr
    Ai = A.indices
    Ax = A.data
    check_compress_arrays(Ap, Ai, Ax)
    n = Ap.size - 1
    c_Ap = numpy.ctypeslib.as_ctypes(Ap)
    c_Ai = numpy.ctypeslib.as_ctypes(Ai)
    c_Ax = numpy.ctypeslib.as_ctypes(Ax)
    c_b = numpy.ctypeslib.as_ctypes(b)
    libklu.solve_linear_system(n, c_Ap, c_Ai, c_Ax, c_b)
    return b  # c_b shares the same memory space with b


def check_compress_arrays(Ap, Ai, Ax):
    '''validate the result of scipy.sparse.csc_matrix'''
    assert isinstance(Ap, numpy.ndarray)
    assert isinstance(Ai, numpy.ndarray)
    assert isinstance(Ax, numpy.ndarray)
    assert Ap[-1] == Ai.size == Ax.size

