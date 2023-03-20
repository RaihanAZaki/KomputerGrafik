print("\833c")
import numpy as np
import matplotlib.pyplot as plt

# The user informs the coordinates of the two points for the line
y1 = 100; x1 = 100
y2 = 400; x2 = 400

pd = int(20)
lw = int(20)

hw = int(lw/2)

col = int(500)
row = int(500)

Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
# Gambar[:, :, :] = 255
# Gambar[x1, y1, 0] = 255
# Gambar[x2, y2, 0] = 255

# Gambar[y1, x1-1, 0] = 255
# Gambar[y1, x1, 0] = 255
# Gambar[y1, x1+1, 0] = 255
# Gambar[y1-1, x1-1, 0] = 255
# Gambar[y1-1, x1, 0] = 255
# Gambar[y1-1, x1+1, 0] = 255
# Gambar[y1+1, x1-1, 0] = 255
# Gambar[y1+1, x1, 0] = 255
# Gambar[y1+1, x1+1, 0] = 255
#
# Gambar[y2, x2-1, 0] = 255
# Gambar[y2, x2, 0] = 255
# Gambar[y2, x2+1, 0] = 255
# Gambar[y2-1, x2-1, 0] = 255
# Gambar[y2-1, x2, 0] = 255
# Gambar[y2-1, x2+1, 0] = 255
# Gambar[y2+1, x2-1, 0] = 255
# Gambar[y2+1, x2, 0] = 255
# Gambar[y2+1, x2+1, 0] = 255

for i in range (y1-5, y1+6):
    for j in range (x1-5, x1+6):
        Gambar[i, j, 0]=255

for i in range (y2-5, y2+6):
    for j in range (x2-5, x2+6):
        Gambar[i, j, 0]=255

plt.figure()
plt.imshow(Gambar)
plt.show()