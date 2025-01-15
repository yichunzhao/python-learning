import numpy as np

# create an Array 1000000 x 1 with random integers
np.random.seed(3)
a = np.random.randint(1, 100, (4, 20))
# print out the array and its shape, and its partition
print(a)
print("a shape: " + str(a.shape))
print("a partition: " + str(a[:, (2, 4)]))
