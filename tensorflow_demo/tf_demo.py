import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


classes = tf.constant([1, 3, 3, 5, 6])
print(classes.shape)

# get unique values and their indices
unique, idx = tf.unique(classes)
print(unique)
print(idx)

label = 3
filtering_mask = unique == label
print(filtering_mask)






