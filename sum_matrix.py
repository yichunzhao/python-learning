import numpy as np

# creating a matrix 4x4 with random integers
np.random.seed(3)
# printout a separation string
print("Matrix 4x4 with random integers")
a = np.random.randint(1, 100, (4, 4))
print(a)

# sum matrix along with row axis printout a separation string
print("Sum matrix along with row axis")
print(np.sum(a, axis=1).reshape(4, 1))

# mean matrix along with row axis and printout a separation string
print("Mean matrix along with row axis")
print(np.mean(a, axis=1).reshape(4, 1))

# cal. standard deviation along with row axis and printout a separation string
print("Standard deviation along with row axis")
print(np.std(a, axis=1).reshape(4, 1))

# normalize the matrix and printout a separation string
print("Normalize the matrix")
sd = np.std(a, axis=1).reshape(4, 1)
print((a - sd) / sd)
