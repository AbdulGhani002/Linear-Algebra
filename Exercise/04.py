'''
Solve the system of equations for x, y, and z:
3x + 1y + 0z = = 54
2x + 4y + 1z = 12
3x + 1y + 8z = 6
'''
from numpy import array
from numpy.linalg import inv
A = array([
 [3, 1, 0],
 [2, 4, 1],
 [3, 1, 8]
])
B = array([
 54,
 12,
 6
])
X = inv(A).dot(B)
print(X)