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

# Define the file names and the corresponding columns to extract
file_names = ['MatrixS0.txt', 'MatrixS1.txt', 'MatrixS2.txt']
section_labels = ['{0, -1}', '{0, 0}', '{0, 1}']  # Labels for each file's data

# Initialize a dictionary to store data from each file
data = {label: [] for label in section_labels}

# Read each file and extract the specified columns
for i, file_name in enumerate(file_names):
    # Load the file, skipping the first row
    file_data = np.loadtxt(file_name, skiprows=1)
    
    L_values = file_data[:, 0]
    S_Lel_values = file_data[:, 1]

    # Store the extracted data in the dictionary
    data[section_labels[i]] = (L_values, S_Lel_values)

# Function to interpolate and find L when |S^L_{el}| = 0.5
def find_L_at_half_y(L_values, S_Lel_values, target_y=0.5):
    for i in range(len(S_Lel_values) - 1):
        if (S_Lel_values[i] - target_y) * (S_Lel_values[i + 1] - target_y) <= 0:
            # Linear interpolation formula: L = L1 + (target_y - y1) * (L2 - L1) / (y2 - y1)
            L1, L2 = L_values[i], L_values[i + 1]
            y1, y2 = S_Lel_values[i], S_Lel_values[i + 1]
            L_at_target = L1 + (target_y - y1) * (L2 - L1) / (y2 - y1)
            return L_at_target
    return None  # Return None if target_y is not found

# Calculate and display L for |S^L_{el}| = 0.5 for each dataset
results = {}
for section, (L_values, S_Lel_values) in data.items():
    L_at_half_y = find_L_at_half_y(L_values, S_Lel_values, target_y=0.5)
    results[section] = L_at_half_y
    print(f"For section {section}, L when |S| = 0.5 is: {L_at_half_y:.2f} (if found)")

# Plot the data
plt.figure(figsize=(10, 6))
for section, (L_values, S_Lel_values) in data.items():
    plt.plot(L_values, S_Lel_values, label=f'{section}')
    L_at_half_y = results[section]
    #if L_at_half_y is not None:
        # Highlight the point where |S^L_{el}| = 0.5
        #plt.scatter(L_at_half_y, 0.5, color='red', zorder=5)
        #plt.text(L_at_half_y, 0.5, f'L={L_at_half_y:.2f}', color='red', fontsize=12)

# Add labels, title, and legend
plt.xlabel('L')
plt.ylabel(r'$|S^L_{el}|$')
plt.xlim(0, 72)
plt.ylim(0.04, 1.1)
plt.legend()

plt.savefig("SMatrix.pdf")
plt.close()
