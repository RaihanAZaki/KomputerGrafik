print("\833c")
import numpy as np
import matplotlib.pyplot as plt

# USER ENTRIES
row, col = 500,500

# Horizontal Miring
# y1, x1 = 50, 50
# y2, x2 = 70, 450

# Horizontal Tegak
# y1, x1 = 50, 50
# y2, x2 = 50, 450

# # Vertikal Miring
# y1, x1 = 50, 50
# y2, x2 = 450, 70
#
# # Vertikal Tegak
# y1, x1 = 50, 50
# y2, x2 = 450, 50

point_color = [255, 0, 0]
line_color = [220, 220, 220]

pr,pg,pb = point_color
lr,lg,lb = line_color

dy = y2-y1
dx = x2-x1

# Buat canvas
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

# Draw the first point
Gambar[y1, x1, :] = point_color

Gambar[y2, x2, :] = point_color

if abs(dx) > abs(dy):
    my=dy/dx
    for x in range (x1, x2+1):
        y = round (my*(x-x1) + y1)
        Gambar[y, x, :] = point_color

else:
    mx=dx/dy
    for y in range (y1, y2+1):
        x = round (mx*(y-y1) + x1)
        Gambar[y, x, :] = point_color

plt.figure()
plt.imshow(Gambar)
plt.show()