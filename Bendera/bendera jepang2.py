import numpy as np
import matplotlib.pyplot as plt

row = 1500
col = 1500

cx = 600
cy = 800
r = 200

image = np.zeros(shape=(row, col, 3), dtype=np.int16)

# Bagian putih bendera
for i in range(200, 1001):
    for j in range(200, 1401):
        image[i, j] = [255, 255, 255]

# Membuat lingkaran merah
for i in range(400, 800):
    for j in range(600, 1000):
        if ((i - cx) ** 2 + (j - cy) ** 2) <= (r ** 2):
            image[i, j] = [255, 0, 0]

plt.figure()
plt.imshow(image)
plt.show()

