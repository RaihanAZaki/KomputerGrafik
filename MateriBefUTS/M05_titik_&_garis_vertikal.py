import numpy as np
import matplotlib.pyplot as plt

row, col = int(100), int(100)
# y1, x1 = 10, 10
# y2, x2 = 190, 190
y1, x1 = 10, 10
y2, x2 = 90, 10
point_Color = [255, 0, 0]
line_Color = [220, 220, 220]

pr, pg, pb = point_Color
lr, lg, lb = line_Color

dy = y2-y1
dx = x2-x1
mx = dx/dy

# buat canvas
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

# draw the first point
Gambar[y1, x1, :] = point_Color

# draw the second point
Gambar[y2, x2, :] = point_Color

for y in range (y1, y2+1) :
    x = round(mx*(y-y1) + x1)
    Gambar[y, x, :] = point_Color

plt.figure()
plt.imshow(Gambar)
plt.show()