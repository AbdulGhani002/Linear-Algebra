from numpy import array

basis = array(
 [[3, 0],
 [0, 2]]
)

v = array([3,2])
# Matrix Multiplication
new_v = basis.dot(v)
print(new_v)