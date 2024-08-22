'''
A transformation i lands at [1, 0] and j lands at [2, 2]. What is the determinant
of this transformation?
'''
from numpy import array
from numpy.linalg import det
i_hat = array([1, 0])
j_hat = array([2, 2])
basis = det(array([i_hat, j_hat]))
print(basis)