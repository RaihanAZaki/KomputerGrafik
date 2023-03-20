import numpy as np

# Membuat Canvas
row = int(1000)
col = int(1000)
print('col, row =', col, ',', row)

# Untuk memberikan warna pada point
pd1 = int(30); #untuk memberikan ketebalan pada point diameter function garis1
pd2 = int(1); #untuk memberikan ketebalan pada point diameter function garis2
pr = 255;
pg = 255;
pb = 255
hd1 = int(pd1 / 2)  # Kalkulasi setengah poin diameter
hd2 = int(pd2 / 2)  # Kalkulasi setengah poin diameter

# Untuk memberikan warna pada garis
lw = int(10);
lr = 0;
lg = 0;
lb = 255
hw = int(lw / 2)  # calculate the half-half line width

Gambar = np.zeros(shape=(row+1, col+1, 3), dtype=np.uint8)  # memberikan latar hitam


# Function buat_garis1
def buat_garis1(Gambar, y1, x1, y2, x2, y3, x3, y4, x4, hw, hd1, pr, pg, pb, lr, lg, lb):

    dy = y2 - y1
    dx = x2 - x1

    # draw the horizontal line
    if dy <= dx: #dapat dikatakan horizontal karena nilai dy lebih kecil dibandingkan dx
        my = dy / dx #menghitung nilai kemiringan
        for j in range(x1, x2):
            i = int(my * (j - x1) + y1)
            x = j
            y = i
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
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
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb


    # draw the first point
    for i in range(x1 - hd1, x1 + hd1):
        for j in range(y1 - hd1, y1 + hd1):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd1 ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # draw the second point
    for i in range(x2 - hd1, x2 + hd1):
        for j in range(y2 - hd1, y2 + hd1):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd1 ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # draw the third point
    for i in range(x3 - hd1, x3 + hd1):
        for j in range(y3 - hd1, y3 + hd1):
            if ((i - x3) ** 2 + (j - y3) ** 2) < hd1 ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # draw the four point
    for i in range(x4 - hd1, x4 + hd1):
        for j in range(y4 - hd1, y4 + hd1):
            if ((i - x4) ** 2 + (j - y4) ** 2) < hd1 ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    return Gambar

# Function buat_garis2
def buat_garis2(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb):
    # draw the first point
    for i in range(x1 - hd2, x1 + hd2):
        for j in range(y1 - hd2, y1 + hd2):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd2 ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb
    # draw the second point
    for i in range(x2 - hd2, x2 + hd2):
        for j in range(y2 - hd2, y2 + hd2):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd2 ** 2:
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
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
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
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    return Gambar

