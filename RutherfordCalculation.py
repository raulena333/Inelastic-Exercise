import numpy as np
import pandas as pd

# Load the experimental data (with errors)
data_given = np.loadtxt("ExperimentalData.txt")
theta = data_given[:, 0]  # Angles in degrees
sigma_exp = data_given[:, 1]  # Experimental cross-section in barn/sr
error_exp = data_given[:, 2]  # Experimental errors

# Convert angles to radians
theta_rad = np.radians(theta)

def rutherford_cross_section(theta, Z1, Z2, E):
    """
    Calculate the Rutherford differential cross-section.

    Parameters:
        theta (array-like): Scattering angle in radians.
        Z1 (float): Atomic number of the incident particle.
        Z2 (float): Atomic number of the target particle.
        E (float): Kinetic energy of the incident particle in MeV.

    Returns:
        array-like: Rutherford differential cross-section in units of barn/sr.
    """
    # Constants
    e2 = 1.44  # MeV·fm (electric charge squared in MeV·fm units)
    k = Z1 * Z2 * e2  # Coulomb constant in MeV·fm

    # Compute differential cross-section
    d_sigma_dOmega = (k / (2* E))**2 / (np.sin(theta / 2)**4)

    return d_sigma_dOmega

# Parameters
Z1 = 2  # Helium nucleus (alpha particle)
Z2 = 50  # Gold nucleus
E = 183  # Kinetic energy in MeV

# Compute Rutherford differential cross-section
sigma_rutherford = rutherford_cross_section(theta_rad, Z1, Z2, E)

# Calculate the ratio of the experimental cross-section to the Rutherford cross-section
sigma_ratio = sigma_exp / sigma_rutherford

# Combine theta and sigma_ratio into a DataFrame
output_data = pd.DataFrame({
    "Theta (deg)": theta,
    "Sigma Ratio": sigma_ratio
})

# Write to a .txt file with a header
output_file_path = "sigma_ratio_output.txt"
output_data.to_csv(output_file_path, sep="\t", index=False, header=True)

# Print the output file path
print(f"Data written to {output_file_path}")
