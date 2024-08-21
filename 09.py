import numpy as np

a = np.random.rand(8,13,13)
b = np.random.rand(8,13,13)
c = a @ b  
d = np.dot(a, b)
print(d)