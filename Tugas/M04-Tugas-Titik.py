import numpy as np
import matplotlib.pyplot as plt
import warnings

#Memanggil function buat_titik pada class library
from Kuliah.KompGraf.Tugas.library import buat_titik
print("\033c")
warnings.filterwarnings('ignore')

# User menentukan titik koordinat.
y1 = 100;x1 = 100
y2 = 200;x2 = 200
y3 = 300;x3 = 300
y4 = 400;x4 = 400

#User menentukan point diameter
pd = 20
#Melakukan kalkulasi setengah diameter
hd = int(pd/2)

#User menentukan lebar titik
lw = 10

#Melakukan kalkulasi setengah lebar titik
hw = int(lw/2)

#Mengatur Ukuran canvas
row = int(500)
col = int(500)
print('col, row =', col, ',', row)

#Membuat canvas
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
Gambar[:, :, :] = 255 # Mengubah warna canvas menjadi putih

hasil = buat_titik(Gambar, y1, x1, y2, x2, y3, x3, y4, x4, hd)

plt.figure()
plt.imshow(hasil)
plt.show()