import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import glob 
import os  

# Set plot parameters
params = {
    'xtick.labelsize': 17,
    'ytick.labelsize': 17,
    'axes.titlesize': 18,
    'axes.labelsize': 18,
    'legend.fontsize': 16
}
pylab.rcParams.update(params)  # Apply the parameter updates

# Define file pattern and colors
file_pattern = "./DataInelastic/inelastic_2H116Sn_183MeV*.txt"
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown'] 

# Find all matching files
files = sorted(glob.glob(file_pattern))

# Check if files are found
if len(files) == 0:
    raise FileNotFoundError(f"No files matching the pattern {file_pattern} were found.")

data_exp = np.loadtxt("ExperimentalData.txt")

# Initialize the plot
plt.figure(figsize=(10, 6))

# Iterate through files and plot the data
for i, file in enumerate(files):
    data = np.loadtxt(file, skiprows = 1) 
    x = data[:, 0]  
    y = data[:, 1]  
    # Extract the distinguishing part of the file name
    label = os.path.splitext(os.path.basename(file))[0].replace("inelastic_2H116Sn_183MeV", "")
    plt.plot(x, y, label=label, color=colors[i % len(colors)])
plt.plot(data_exp[:, 0], data_exp[:, 1], color = "black", label= "Experimental", linestyle = "--")

# Customize the plot
plt.xlabel(r"$\theta$ (deg)")  
plt.ylabel(r"$\sigma_{inel}$ (mb/sr)") 
plt.yscale("log")  
plt.legend()

# Save the plot as a PDF
plt.savefig("./DataInelastic/InelasticScattering_All.pdf")
plt.show() 
