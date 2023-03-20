import matplotlib.pyplot as plt
import numpy as np
import warnings

print("\033c")
warnings.filterwarnings('ignore')

# coordinate lines
ya, xa = 200, 275
yb, xb = 200, 275

# point (vertex) diameter and color
pd = int(3)  # ukuran titik
pr = 0
pg = 0
pb = 255

# line width and color
lw = int(10)
lr = 0
lg = 0
lb = 255

# setting size canvas
row = int(1000)
col = int(1000)
print('row, col = ', row, ',', col)

def buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb):
   # draw the first point
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb
    # draw the second point
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    dy = y2 - y1
    dx = x2 - x1
    # draw the horizontal line
    if dy <= dx:
        my = dy / dx
        for j in range(x1, x2):
            i = int(my * (j - x1) + y1)
            x = j
            y = i
            if y % 50:
                print('x, y = ', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 4 + (j - y) ** 4) < hw ** 4:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    # draw the vertical line
    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            x = i
            y = j
            if x % 50:
                print('x, y = ', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb



    return Gambar

# MAIN PROGRAM
# preparing the black canvas
hd = int(pd / 2)  # half point diameter
hw = int(lw / 2)  # half line width
# preparing black canvas
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
Gambar[:, :, :] = 0  #

while ya <= 400:
    yb += 2
    ya += 2
    xb += 1
    xa -= 1
    hasil = buat_garis(Gambar, ya, xa, yb, xb, hd, hw, pr, pg, pb, lr, lg, lb)
    Gambar = hasil

while ya <= 600:
    yb += 2
    ya += 2
    xb -= 1
    xa += 1
    hasil = buat_garis(Gambar, ya, xa, yb, xb, hd, hw, pr, pg, pb, lr, lg, lb)
    Gambar = hasil

plt.figure('Diamond')
plt.imshow(hasil)
plt.show()