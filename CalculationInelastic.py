import numpy as np

beta2 = 0.11 
A_target = 116
r_c = 1.3
r_0_woods_volume = 1.179
r_i_woods_volume = 1.313
r_i_woods_surface = 1.313
Zt = 50
Zp = 1

R_c = r_c * A_target**(1/3)
m_nt = ( 3* Zt * beta2 * R_c**2) / (4 * np.pi ) 
print(f'Valor Mn(E2): {m_nt:.4f}')

deforamtion_volumen_real = beta2 * (r_0_woods_volume * A_target**(1/3))
deforamtion_volumen_imaginary = beta2 * (r_i_woods_volume * A_target**(1/3))
deforamtion_surface_imaginary = beta2 * (r_i_woods_surface * A_target**(1/3))
print(f'Deformation lenght WS volumen imaginary : {deforamtion_volumen_imaginary:.4f} fm')
print(f'Deformation lenght WS volumen real : {deforamtion_volumen_real:.4f} fm')

print(f'Deformation lenght WS surface imaginary : {deforamtion_surface_imaginary:.4f} fm')