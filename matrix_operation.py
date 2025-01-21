import numpy as np

# demo elementwise multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a*b)

# demo elementwise division
print(a/b)

# demo elementwise addition
print(a+b)

# demo matrix multiplication
print(a.dot(b))
