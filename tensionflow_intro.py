import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf

w = tf.Variable(0, dtype=tf.float32)
optimizer = tf.keras.optimizers.Adam(0.1)


def train_step():
    with tf.GradientTape() as tape:
        cost = w ** 2 - 10 * w + 25
    trainable_variables = [w]
    gradients = tape.gradient(cost, trainable_variables)
    optimizer.apply_gradients(zip(gradients, trainable_variables))


print(w)


for i in range(1000):
    train_step()

print(w)
