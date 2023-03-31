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
# VCE = [0, 0.5, 1, 2, 5, 10]
# Ib_10 = [0, 2.22, 4.4, 6.76, 9.06, 11.36]
# Ib_20 = [0, 2.21, 4.44, 6.85, 9.16, 11.57]
# Ib_30 = [0, 2.23, 4.49, 7.2, 9.31, 11.88]
# Ib_40 = [0, 2.32, 4.63, 7.3, 9.74, 12.62]
# Ib_50 = [0, 2.41, 4.9, 7.58, 10.67, 13.38]

# plt.plot(VCE, Ib_10, 'r--', label='Ib=10uA')
# plt.plot(VCE, Ib_20, 'g--', label='Ib=20uA')
# plt.plot(VCE, Ib_30, 'b--', label='Ib=30uA')
# plt.plot(VCE, Ib_40, 'c--', label='Ib=40uA')
# plt.plot(VCE, Ib_50, 'm--', label='Ib=50uA')

# plt.xlabel('VCE (V)')
# plt.ylabel('Ic (mA)')
# plt.title('grafik perubahan nilai Ic terhadap VCE')
# plt.legend()
# plt.show()


# graph table 2

# Masukkan data ke dalam array numpy
Ib = [10, 20, 30]
Ic = [2.31, 4.54, 5.32]

plt.plot(Ib, Ic, '-o')
plt.xlabel('Ib (uA)')
plt.ylabel('Ic (mA)')
plt.title('Perubahan Ic terhadap Ib')

gain = (Ic[-1] - Ic[0]) / (Ib[-1] - Ib[0])
plt.text(25, 2.3, "Gain = {:.2f}".format(gain))

plt.show()
