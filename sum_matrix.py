import numpy as np

# creating a matrix 4x4 with random integers
np.random.seed(3)
a = np.random.randint(1, 10, (4, 4))
print(a)

# sum matrix along with row axis
print(np.sum(a, axis=1).reshape(4, 1))

# mean matrix along with row axis
print(np.mean(a, axis=1).reshape(4, 1))
