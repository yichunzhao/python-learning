import numpy as np
import matplotlib.pyplot as plt

# Define the exponential function
def exp_z(z):
    return np.exp(z)

# Generate z values (real numbers, e.g., from -5 to 5)
z = np.linspace(-5, 5, 100)  # 100 points from -5 to 5
y = exp_z(z)  # Compute e^z for each z

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(z, y, label='e^z', color='blue')
plt.title('Exponential Function e^z')
plt.xlabel('z')
plt.ylabel('e^z')
plt.grid(True)
plt.legend()
plt.show()