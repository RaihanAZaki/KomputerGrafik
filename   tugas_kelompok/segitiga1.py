#PROGRAM UNTUK TITIK DAN GARIS
print("\033c")       #To close all
import numpy as np
import matplotlib.pyplot as plt

#The user informs the coordinates of the two points for the line.
ya = 200; xa = 200
yb = 200; xb = 600
# yc = 600; xc = 600
yd = 600; xd = 200

#The user decides the points' (vertex) diameter and color
pd = int(8); pr = 106; pg = 13; pb = 173
# The user decide the line width and color
lw = int(8); lr = 106; lg = 13; lb = 173

#Setting the size of the canvas
col = int(800)
row = int(800)
print('col, row =', col, ',', row)

## FUNCTION UNTUK MEMBUAT GARIS
## Once x and y known, create a circle and color it red.
def buat_garis(Gambar, y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16) #Preparing the black canvas
    hd = int(pd/2)                               #Calculate the half point diameter.
    hw = int(lw/2)                              #Calculate the half half line width.
    dy = y2-y1
    dx = x2-x1

    # Draw the first point.
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) * 2 + (j - y1) * 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Draw the second point.
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) * 2 + (j - y2) * 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    #Draw the line. Untuk garis yang cenderung horisontal
    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i-x1) + y1)           #Finding y using the line equation
            x = i
            y = j
            print('x, y =', x, ',', y)
            for i in range(x-hw, x+hw):        #Creating a circle surrounding (x,y) and coloring it red
                for j in range(y-hw, y+hw):
                    if ( (i-x)*2 + (j-y)*2 ) < hw **2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    #Draw the line. Untuk garis yang cenderung vertikal
    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j-y1) + x1)           #Finding y using the line equation
            x = i
            y = j
            print('x, y =', x, ',', y)
            for i in range(x-hw, x+hw):        #Creating a circle surrounding (x,y) and coloring it red
                for j in range(y-hw, y+hw):
                    if ( (i-x)*2 + (j-y)*2 ) < hw **2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    return Gambar

## MAIN PROGRAM
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
hasil1 = buat_garis(Gambar, ya, xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)
# hasil2 = buat_garis(Gambar, yb, xb, yc, xc, pd, lw, pr, pg, pb, lr, lg, lb)
hasil3 = buat_garis(Gambar, yd, xd, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)
hasil4 = buat_garis(Gambar, ya, xa, yd, xd, pd, lw, pr, pg, pb, lr, lg, lb)

#perulangan fill in
while ya < 601:
    ya += 1
    hasil5 = buat_garis(Gambar, ya,xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)
    Gambar += hasil5

hasil = hasil1 + hasil3 + hasil4 + Gambar
plt.figure()
plt.imshow(hasil)
plt.show()