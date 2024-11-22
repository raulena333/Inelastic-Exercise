import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

params = {
    'xtick.labelsize': 17,    
    'ytick.labelsize': 17,      
    'axes.titlesize' : 18,
    'axes.labelsize' : 18,
    'legend.fontsize': 16
}
pylab.rcParams.update(params)  # Apply the changes

# Load potential values
data = np.loadtxt('deflection_2116_183MeV.txt', skiprows=1)
b = data[:, 0]  # b-values (distance)
theta = data[:, 1]  # Angle values (theta)

# Find the maximum and minimum values of theta and their corresponding b (angle)
max_index = np.argmax(theta)  # Index of the maximum value
min_index = np.argmin(theta)  # Index of the minimum value

max_b = b[max_index]  # Corresponding b value for maximum
min_b = b[min_index]  # Corresponding b value for minimum

max_theta = theta[max_index]  # Maximum theta value
min_theta = theta[min_index]  # Minimum theta value

# Print out the results
print(f"Maximum value of θ: {max_theta:.2f}° at b = {max_b:.2f} fm (Coulomb interaction)")
print(f"Minimum value of θ: {min_theta:.2f}° at b = {min_b:.2f} fm (Nuclear interaction)")

# Plot the potentials
plt.figure(figsize=(10, 6))
plt.plot(b, theta, color="red")
plt.axhline(0, 20, linestyle='--', color="black")

# Customize plot
plt.xlabel("b (fm)")
plt.ylabel(r"$\theta$ (deg)")
plt.ylim(-27.5, 5)
plt.xlim(-0.1, 20)
plt.legend()

# Save the plot
plt.savefig('ClassicalPlot.pdf')
plt.close()
