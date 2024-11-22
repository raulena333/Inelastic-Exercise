import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

# Set plot parameters
params = {
    'xtick.labelsize': 17,    
    'ytick.labelsize': 17,      
    'axes.titlesize' : 18,
    'axes.labelsize' : 18,
    'legend.fontsize': 16
}
pylab.rcParams.update(params)  # Apply changes

# Load potential values
data = np.loadtxt('Elastic_plot_mb_sr.txt', skiprows=2)
theta = data[:, 0] 
cross = data[:, 1]

# Load experimental data
data_exp = np.loadtxt("ExperimentalData.txt", skiprows=1)
theta0 = data_exp[:, 0]
cross0 = data_exp[:, 1]
error = data_exp[:, 2]

# Plot the potentials
plt.figure(figsize=(10, 6))
plt.plot(theta, cross, color="black", label="Theoretical Data")
plt.errorbar(theta0, cross0, yerr=error, fmt='--', color="red", label="Experimental Data")

# Customize plot
plt.xlabel(r"$\theta$ (deg)")
plt.ylabel(r"$d\sigma/d\Omega$ (mb/sr)")
plt.semilogy()

# Save the plot
plt.legend()
plt.savefig('ElasticScatteringSigma.pdf')
plt.close()