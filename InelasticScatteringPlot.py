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
pylab.rcParams.update(params)  # Aplicar los cambios

# Load potential values
data = np.loadtxt('inelastic_2H116Sn_183MeV.txt', skiprows=2)
theta = data[:, 0] 
ruth_cross = data[:, 1]

data_exp = np.loadtxt("exforSNinelastic.txt", skiprows = 1)
theta0 = data_exp[:, 0]
ruth_cross0 = data_exp[:, 1]

# Plot the potentials
plt.figure(figsize=(10, 6))
plt.plot(theta, ruth_cross, color = "black", label = "Theorical data (Excited)")
plt.plot(theta0, ruth_cross0, linestyle ="--",  color = "red", label = "EXFOR data")

# Customize plot
plt.xlabel(r"$\theta$ (deg)")
plt.ylabel(r"$\sigma_{ine}$ (mb/sr)")
plt.legend()
plt.semilogy()
plt.savefig('InelasticScattering.pdf')
plt.close()