import numpy as np
# training data set size
m = 1000
batche_size = 64

# create a Array 1000000 x 1 with random integers
a = np.random.rand(m, 1)

# partition the array into batches with batch-size 64

batch_size = m // batche_size
last_batch_size = m % batche_size
print("Batch size: " + str(batch_size))
print("Last batch size: " + str(last_batch_size))

for i in range(1, batch_size + 1):
    if i == batch_size:
        print("Last batch")
        print("Start index: " + str((i - 1) * batche_size))
        print("End index: " + str(i * batche_size + last_batch_size))
    else:
        print("Start index: " + str((i - 1) * batche_size))
        print("End index: " + str(i * batche_size))
