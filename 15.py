#Eigen Decomposition
'''
If we have a square matrix A, it has the following eigenvalue equation:
                        Av = λv
If A is the original matrix, it is composed of eigenvector v and eigenvalue λ. There is
one eigenvector and eigenvalue for each dimension of the parent matrix, and not all
matrices can be decomposed into an eigenvector and eigenvalue. Sometimes complex
(imaginary) numbers will even result.
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
print("EIGENVECTORS")
print(eigenvecs)
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
