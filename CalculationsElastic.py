import numpy as np

# Constants and given values
E_lab = 183  # Energy in the laboratory in MeV
M_projectile = 2  # Mass of lithium-8 in atomic mass units
M_target = 116  # Mass of lead-206 in atomic mass units
Z_projectile = 1  # Charge of the projectile
Z_target = 50  # Charge of the target
e2 = 1.44  # e^2/(4πε₀) in MeV·fm (Coulomb constant)
massUnits_toMev = 931.5 # conversion for mass units to energy units

# Calculate the center-of-mass energy
E_cm = E_lab * (M_target / (M_projectile + M_target))
print(f"Center-of-mass energy: {E_cm:.2f} MeV")

# Calculate the reduced mass
mu = (M_projectile * M_target) / (M_projectile + M_target)
muMev = mu * massUnits_toMev
print(f"Reduced mass: {mu:.2f} uma")
print(f'Reduced mass, {muMev:.2f} Mev/c^2')

# Calculate the Coulomb diffusion parameter (a₀)
a_0 = (Z_projectile * Z_target * e2) / (2 * E_cm)
print(f"Coulomb diffusion parameter (a₀): {a_0:.3f} fm")

# Calculate the closest distance of approach (r₀)
r_0 = 2 * a_0
print(f"Closest approach distance (r₀): {r_0:.2f} fm")

# Planck's constant (reduced h-bar) in MeV·fm/c
hbar = 4.135667696e-12  # MeV /s (value of h-bar in these units)
hbarc = 197.327 # Value in Mev/fm

# Calculate the wave number (k) and lambda_0 (De Broglie wavelength)
k = (np.sqrt(2 * muMev * E_cm)) /hbarc
lambda_0 = 1 / k
print(f" Wavelenght : {lambda_0:.3f} fm^-1")
print(f' Wavenumber : {k:.3f} fm')

# Sommerfeld parameter (η)
sommerfield = k * r_0 / 2
sommerfield2 = a_0 * k
print(f"Sommerfeld parameter (η): {sommerfield:.3f}")
print(f'Sommerfield parameter : {sommerfield2:.3f}')

var_theta = 4.5
print(f"The value of grazing momentum is : {np.pi / np.radians(var_theta)}")
R_g = (np.pi / np.radians(var_theta)) / k
print(f"The value of R_grazing is : {R_g} fm")
R_g_theory = 1.44 * (M_projectile**(1/3) + M_target**(1/3))
R_g_theory0 = 1.44 * M_target**(1/3)
print(f'Value of R_g theory is : {R_g_theory} fm')
print(f'Value of R_g theory is : {R_g_theory0} fm')
