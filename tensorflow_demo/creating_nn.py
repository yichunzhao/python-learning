import tensorflow as tf

# Define the number of neurons in each layer
input_size = 10  # Size of input features
hidden_size = 20  # Number of neurons in hidden layer
output_size = 1   # Size of output (for example, binary classification)

# Define placeholders for input and output; tf convention is to use 'None' for the variable batch size.
X = tf.placeholder(tf.float32, shape=[None, input_size])
Y = tf.placeholder(tf.float32, shape=[None, output_size])

# Define weights and biases for each layer