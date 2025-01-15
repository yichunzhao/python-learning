import numpy as np

# create an Array 1000000 x 1 with random integers
np.random.seed(3)
a = np.random.randint(1, 100, (4, 20))
# print out the array and its shape, and its partition
print(a)
print("a shape: " + str(a.shape))
print("a partition: " + str(a[:, (2, 4)]))

# create a (4,10) matrix
b = np.random.randint(1, 100, (4, 1))
# print out b with description string
print("b: " + str(b))

# create matrix zeros_like b
c = np.zeros_like(b)
# print out c with description string
print("c: " + str(c))

