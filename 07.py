from numpy import array

i_hat = array([2, 3])
j_hat = array([2, -1])

basis = array([i_hat, j_hat]).transpose()

v = array([2,1])
new_v = basis.dot(v)
print(new_v)