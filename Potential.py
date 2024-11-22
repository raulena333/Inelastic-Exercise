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

E_lab = 183  # Energy in the laboratory in MeV
M_projectile = 2  # Mass of lithium-8 in atomic mass units
M_target = 116  # Mass of lead-206 in atomic mass units
Z_projectile = 1 # Charge of the projectile
Z_target = 50 # Charge of the target

# Calculate the center-of-mass energy and other
E_cm = E_lab * (M_target / (M_projectile + M_target))
print(f"Center-of-mass energy: {E_cm:.2f} MeV")

# Load potential values
data = np.loadtxt('PotentialsOptical.txt', skiprows=3)
radius = data[:, 0]
potential_values = data[:, 1]
imaginary_values = data[:, 2]

# Find the maximum potential value and its corresponding radius
max_potential = np.max(potential_values)
max_radius = radius[np.argmax(potential_values)]
theory_radius = 1.45 * (M_projectile**(1/3) + M_target**(1/3))
theory_potential = 1.44 * (Z_projectile * Z_target) / (theory_radius)
print(f"Maximum potential: {max_potential:.3f} MeV at radius: {max_radius:.2f} fm")
print(f"Maximum theorical potential : {theory_potential:.3f} Mev at theorical radius: {theory_radius:.3f} fm")

# Plot the potentials
plt.figure(figsize=(10, 6))
plt.plot(radius, potential_values, label="Real", color = "red")
plt.plot(radius, imaginary_values, label="imaginary", color ="blue")
# plt.plot([0, 25], [E_cm, E_cm], color='black', linestyle='--', label=f"E_cm = {E_cm:.2f} MeV")

# Customize plot
plt.xlabel("r (fm)")
plt.ylabel("V, W (MeV)")
#plt.title("Optical Potential")
plt.legend()
plt.ylim(-40, 10) 
plt.xlim(0, 27.5) 
plt.savefig('PotantialPlot.pdf')

# Load potential values
data1 = np.loadtxt('PotentialsSpin.txt', skiprows=3)
potential_values1 = data1[:, 1]
imaginary_values1 = data1[:, 2]

plt.figure(figsize=(10, 6))
plt.plot(radius, potential_values1, label="Real", color = "red")
plt.plot(radius, imaginary_values1, label="imaginary", color ="blue")
# plt.plot([0, 25], [E_cm, E_cm], color='black', linestyle='--', label=f"E_cm = {E_cm:.2f} MeV")

# Customize plot
plt.xlabel("r (fm)")
plt.ylabel("V, W (MeV)")
#plt.title("Spin orbital-potential")
plt.legend()
plt.ylim(-8, 1) 
plt.xlim(-0.1, 27.5) 
plt.savefig('PotantialPlotSpin.pdf')
plt.close()

