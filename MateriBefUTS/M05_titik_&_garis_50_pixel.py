import numpy as np
import matplotlib.pyplot as plt

row, col = int(300), int(300)
# y1, x1 = 10, 10
# y2, x2 = 190, 190
y1, x1 = 90, 60
y2, x2 = 120, 60
y3, x3 = 90, 90
y4, x4 = 120, 90
point_Color = [255, 0, 0]
line_Color = [220, 220, 220]

pr, pg, pb = point_Color
lr, lg, lb = line_Color

dy = y2-y1
dx = x2-x1
my = dy/dx

# buat canvas
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

# draw the first point
Gambar[y1, x1, :] = point_Color

# draw the second point
Gambar[y2, x2, :] = point_Color

# draw the second point
Gambar[y3, x3, :] = point_Color

# draw the second point
Gambar[y4, x4, :] = point_Color

for x in range (x1, x2+1) :
    y = round(my*(x-x1) + y1)
    Gambar[y, x, :] = point_Color

for x in range (x2, x3+1) :
    y = round(my*(x-x2) + y2)
    Gambar[y, x, :] = point_Color

plt.figure()
plt.imshow(Gambar)
plt.show()