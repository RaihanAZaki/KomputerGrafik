print("\833c")
import numpy as np
import matplotlib.pyplot as plt

# USER ENTRIES
row, col = int(100), int(100)
y1, x1 = 10, 10
y2, x2 = 80, 10
point_color = [255, 0, 0]
line_color = [220, 220, 220]

pr,pg,pb = point_color
lr,lg,lb = line_color

dy = y2-y1
dx = x2-x1
my = dx/dy

# Buat canvas
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

# Draw the first point
Gambar[y1, x1, :] = point_color

Gambar[y2, x2, :] = point_color

for y in range (y1, y2+1):
    x = round (my*(y-y1) + y1)
    Gambar[y, x, :] = point_color

plt.figure()
plt.imshow(Gambar)
plt.show()