from numpy.linalg import det
from numpy import array
i_hat = array([-2, 1])
j_hat = array([1, 2])
basis = array([i_hat, j_hat]).transpose()
determinant = det(basis)
print(determinant)