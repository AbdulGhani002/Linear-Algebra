'''
Vector v has a value of [1, 2] but then a transformation happens. i lands at
[-2, 1] and j lands at [1, -2]. Where does v land?
'''
from numpy import array
v = array([1,2])
i_hat = array([-2, 1])
j_hat = array([1, -2])
basis = array([i_hat, j_hat])
w = basis.dot(v)
print(w)