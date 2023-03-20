import numpy as np
import matplotlib.pyplot as plt
from library_UTS import *

# USER ENTRY
y1, x1 = 400, 300;
y2, x2 = 400, 700;
y3, x3 = 600, 300;
y4, x4 = 600, 700;

while y1 <= 401:
    y1 += 1
    y2 += 1
    hasil = buat_garis1(Gambar, y1, x1, y2, x2, 0, 0, 0, 0, hw, hd1, pr, pb, pg, lr, lg, lb)
    hasil = buat_garis1(Gambar, y1, x1, y3, x3, 0, 0, 0, 0, hw, hd1, pr, pb, pg, lr, lg, lb)
    hasil = buat_garis1(Gambar, y2, x2, y4, x4, 0, 0, 0, 0, hw, hd1, pr, pb, pg, lr, lg, lb)
    hasil = buat_garis1(Gambar, y3, x3, y4, x4, 0, 0, 0, 0, hw, hd1, pr, pb, pg, lr, lg, lb)
    Gambar = hasil

plt.figure("UJIAN TENGAH SEMESTER")
plt.imshow(hasil)
plt.show()
