'''
So how do we rebuild matrix A from the eigenvectors and eigenvalues? Recall this
formula:
Av = λv
We need to make a few tweaks to the formula to reconstruct A:
A = QΛQ^−1
In this new formula, Q is the eigenvectors, Λ is the eigenvalues in diagonal form,
and Q^−1 is the inverse matrix of Q. Diagonal form means the vector is padded into
a matrix of zeroes and occupies the diagonal line in a similar pattern to an identity
matrix
'''
from numpy import array, diag
from numpy.linalg import eig, inv
A = array([
 [1, 2],
 [4, 5]
])
eigenvals, eigenvecs = eig(A)
print("EIGENVALUES")
print(eigenvals)
print("\nEIGENVECTORS")
print(eigenvecs)
print("\nREBUILD MATRIX")
Q = eigenvecs
R = inv(Q)
L = diag(eigenvals)
# @ is used for matrix multiplication
B = Q @ L @ R
print(B)