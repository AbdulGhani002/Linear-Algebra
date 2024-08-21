from numpy import array
i_hat1 = array([0, 1])
j_hat1 = array([-1, 0])
transform1 = array([i_hat1, j_hat1]).transpose()
print(transform1)
i_hat2 = array([1, 0])
j_hat2 = array([1, 1])
transform2 = array([i_hat2, j_hat2]).transpose()
print(transform2)
combined = transform2 @ transform1
print("COMBINED MATRIX:\n {}".format(combined))
v = array([1, 2])
# 1st Method
rotated = transform1.dot(v)
sheered = transform2.dot(rotated)
print(sheered)
# Alternative Method
print(combined.dot(v))