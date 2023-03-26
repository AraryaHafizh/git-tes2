import matplotlib.pyplot as plt
import numpy as np

# MODUL 1
# graph tabel 1.2

# Vd = [0, 0.29, 0.45, 0.47, 0.49, 0.48, 0.48, 0.5, 0.55, 0.55, 0.64]
# Id = [0, 0.005, 0.03, 0.09, 0.15, 0.21, 0.28, 0.35, 0.4, 0.46, 0.51]

# plt.plot(Vd, Id, marker='o')
# plt.xlabel('Vd (V)')
# plt.ylabel('Id (mA)')
# plt.title('Hubungan Vd dan Id')
# plt.show()

# graph tabel 1.4

# Vs = np.array([0, 2, 4, 6, 8, 10])
# Vd = np.array([0, 1.98, 3.06, 3.44, 3.57, 3.8])
# Pd = np.array([0, 0.0594, 2.907, 8.9096, 15.92, 23.864])

# fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# ax1.plot(Vs, Vd, '-o')
# ax1.set_title('Hubungan antara Vs dan Vd')
# ax1.set_xlabel('Vs')
# ax1.set_ylabel('Vd')

# ax2.plot(Vs, Pd, '-o')
# ax2.set_title('Hubungan antara Vs dan Pd')
# ax2.set_xlabel('Vs')
# ax2.set_ylabel('Pd')

# plt.show()

# MODUL 2
# graph tabel 1

# Data yang diberikan
# VCE = np.array([0.5, 1, 2, 5, 10])
# Ic = np.array([[0, 0, 0, 0, 0],
#                [2.22, 2.21, 2.23, 2.32, 2.41],
#                [4.4, 4.44, 4.49, 4.63, 4.9],
#                [6.76, 6.85, 7.2, 7.3, 7.58],
#                [9.06, 9.16, 9.31, 9.74, 10.67],
#                [11.36, 11.57, 11.88, 12.62, 13.38]])

# # Membuat plot grafik
# for i in range(Ic.shape[0]):
#     plt.plot(VCE, Ic[i], label=f"Ib = {i+1} mA")
# plt.xlabel("VCE (V)")
# plt.ylabel("Ic (mA)")
# plt.title('plot grafik perubahan nilai Ic terhadap VCE ')
# plt.legend()
# plt.show()

# graph table 2

# Masukkan data ke dalam array numpy
Ib = np.array([10, 20, 30])
Ic = np.array([2.31, 9.84, 5.32])

# Buat plot
plt.plot(Ib, Ic, 'o')

# Tentukan batas sumbu x dan y
plt.xlim(0, 35)
plt.ylim(0, 12)

# Tentukan label sumbu x dan y
plt.xlabel('Ib')
plt.ylabel('Ic')

# Hitung gradien menggunakan numpy.polyfit
m, b = np.polyfit(Ib, Ic, 1)
gain = round(m, 4)
print('Gain =', gain)

# Buat garis regresi
x = np.linspace(0, 35, 100)
y = m * x + b
plt.plot(x, y)

# Tambahkan teks gain pada plot
plt.text(5, 10, f'Gain = {gain}', fontsize=12)

# Tampilkan plot
plt.title('Plot Ic terhadap perubahan Ib')
plt.show()
