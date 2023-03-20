print("\033c")
import numpy as np
from matplotlib import pyplot as plt

nama_file_output = "square.npy"

#the user decides the square size
length = 3

#user decides the positions of square.
a, b = 30, 30

#the user decides the size of the screen
col = 60; row = 60

#----------Preparation---------------------
plt.figure(figsize=(4,4),dpi=200)
Screen_2D = np.zeros(shape=(row, col, 3), dtype=np.uint8)
tes = np.load(nama_file_output)

hl = round(length/2)
for j in range(a-hl, a+hl):
    for i in range(b-hl, b+hl):
        Screen_2D[j, i, 2] = 255

np.save(nama_file_output, Screen_2D)
rotasi = np.load(nama_file_output)

for i in range (30):
    rotasi = np.roll(rotasi, 1, axis=0)
    plt.imshow(rotasi)
    plt.pause(0.1)

for i in range (30):
    rotasi = np.roll(rotasi, 1, axis=1)
    plt.imshow(rotasi)
    plt.pause(0.1)

for i in range (30):
    rotasi = np.roll(rotasi, 1, axis=2)
    plt.imshow(rotasi)
    plt.pause(0.1)

for i in range (30):
    rotasi = np.roll(rotasi, 1, axis=3)
    plt.imshow(rotasi)
    plt.pause(0.1)

for i in range (30):
    rotasi = np.roll(rotasi, 1, 0, axis=4)
    plt.imshow(rotasi)
    plt.pause(0.1)



plt.imshow(rotasi)
plt.show()