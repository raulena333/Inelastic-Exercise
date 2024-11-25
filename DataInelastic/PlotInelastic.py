import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

# Configuración de los parámetros del gráfico
params = {
    'xtick.labelsize': 17,
    'ytick.labelsize': 17,
    'axes.titlesize': 18,
    'axes.labelsize': 18,
    'legend.fontsize': 16
}
pylab.rcParams.update(params)

# Cargar datos experimentales
data_exp = np.loadtxt("exforSNinelastic.txt")
x_exp = data_exp[:, 0]
y_exp = data_exp[:, 1]

data_exp = np.loadtxt("DataInelastic/inelastic_2H116Sn_183MeV.txt")
x = data_exp[:, 0]
y = data_exp[:, 1]

# Cargar datos teóricos de los otros archivos
file1 = "DataInelastic/inelastic_2H116Sn_183MeVNoCoulomb.txt"
data1 = np.loadtxt(file1)
x1 = data1[:, 0]
y1 = data1[:, 1]

file2 = "DataInelastic/inelastic_2H116Sn_183MeVNoNuclear.txt"
data2 = np.loadtxt(file2)
x2 = data2[:, 0]
y2 = data2[:, 1]

plt.figure(figsize=(10, 6))
plt.plot(x_exp, y_exp, 'r--', label='EXFOR data')
plt.plot(x, y, color = "black", label='Both')
plt.plot(x1, y1, 'b-', label='No Coulomb deformation')
plt.plot(x2, y2, 'g-', label='No Nuclear deformation')

# Customize plot
plt.xlabel(r"$\theta$ (deg)")
plt.ylabel(r"$\sigma_{ine}$ (mb/sr)")
plt.legend()
plt.semilogy()
plt.savefig("DataInelastic/ComparingPotentialDeformation.pdf")
plt.close()

# Cargar datos teóricos de los otros archivos
file1 = "DataInelastic/inelastic_2H116Sn_183MeVOnlyIm.txt"
data1 = np.loadtxt(file1)
x1 = data1[:, 0]
y1 = data1[:, 1]

file2 = "DataInelastic/inelastic_2H116Sn_183MeVOnlyRe.txt"
data2 = np.loadtxt(file2)
x2 = data2[:, 0]
y2 = data2[:, 1]

plt.figure(figsize=(10, 6))
plt.plot(x_exp, y_exp, 'r--', label='EXFOR data')
plt.plot(x, y, color = "black", label='Both')
plt.plot(x1, y1, 'b-', label='No Real deformation')
plt.plot(x2, y2, 'g-', label='No Imaginary deformation')

# Customize plot
plt.xlabel(r"$\theta$ (deg)")
plt.ylabel(r"$\sigma_{ine}$ (mb/sr)")
plt.legend()
plt.semilogy()
plt.savefig("DataInelastic/ComparingNuclearPotentialDeformation.pdf")
plt.close()