import numpy as np
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
# using numpy to create a matrix
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(X)

# cal. X mean along with row axis
mean = np.mean(X, axis=1).reshape(3, 1)
print("mean: ", mean)

# cal. deviation along with row axis
std = (X - mean)
print("{deviation: }", std)
