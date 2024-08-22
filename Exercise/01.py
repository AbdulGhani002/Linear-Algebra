'''
Vector v has a value of [1, 2] but then a transformation happens. i lands at [2, 0]
and j lands at [0, 1.5]. Where does v land?
'''
from numpy import array
v = array([1,2])
i_hat = array([2, 0])
j_hat = array([0, 1.5])
basis = array([i_hat, j_hat])
w = basis.dot(v)
print(w)