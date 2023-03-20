import matplotlib.pyplot as plt
import numpy as np
import warnings


print("\033c")
warnings.filterwarnings('ignore')

# coordinate lines
y1 = 200
x1 = 200
y2 = 200
x2 = 800

# point (vertex) diameter and color
pd = int(5)  # ukuran titik
pr = 0
pg = 0
pb = 255
# line width and color
lw = int(5)
lr = 255
lg = 0
lb = 0

row = int(1000)
col = int(1000)
print('row, col = ', row, ',', col)
def buat_garis(Gambar, y1, x1, y2, x2, hw, lr, lg, lb):
    # draw the first point
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) * 2 + (j - y1) * 2) < hd ** 2:
                Gambar[j, i, 0] = lr
                Gambar[j, i, 1] = lg
                Gambar[j, i, 2] = lb
    # draw the second point
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) * 2 + (j - y2) * 2) < hd ** 2:
                Gambar[j, i, 0] = lr
                Gambar[j, i, 1] = lg
                Gambar[j, i, 2] = lb

    dy = y2-y1
    dx = x2-x1
    # draw the line horizontal
    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i-x1) + y1)
            x = i
            y = j
            print('x, y = ', x, ',', y)
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if ((i-x)*2 + (j-y)**2) < hw * 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    # draw the line vertikal
    if dy > dx:
        mx = dy / dx
        for j in range(y1, y2):
            i = int(mx * (j-y1) + x1)
            x = i
            y = j
            print('x, y = ', x, ',', y)
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if ((i-x)*2 + (j-y)**2) < hw * 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    return Gambar

# MAIN PROGRAM
# preparing the black canvas
hd = int(pd/2)  # half point diameter544p[
hw = int(lw/2)  # half line width
# preparing black canvas
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
Gambar[:, :, :] = 0  # white canvas

while y1 < 601:
    y1 += 1
    y2 += 1
    hasil = buat_garis(Gambar, y1, x1, y2, x2, hw, lr, lg, lb)

Gambar = hasil

plt.figure('Canvas')
plt.imshow(hasil)
plt.show()