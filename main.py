# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import numpy as np

a = np.random.rand(1000000, 1)
b = np.random.rand(1000000, 1)

# print out a,b shapes and with description strings
print("a shape: " + str(a.shape))
print("b shape: " + str(b.shape))

tic = time.time()
c = np.dot(a.T, b)
toc = time.time()

# print out toc and tic difference in ms
print("Vectorized version: " + str(1000*(toc-tic)) + "ms")

# multiply a and b using for loop

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]

toc = time.time()

print("For loop: " + str(1000*(toc-tic)) + "ms")








