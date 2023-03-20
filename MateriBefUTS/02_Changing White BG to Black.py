print("\033c")       #To close all
import numpy as np
from matplotlib import pyplot as plt

#=====================================================================================
#=================================    USER ENTRIES    ================================
#=====================================================================================
nama_file = "LOGO UPJ"
noise_threshold = 40

#=====================================================================================
#============ #CHANGING THE WHITE BACKGROUND TO BLACK (IF NECESSARY)  ================
#=====================================================================================
#The following reading technique is to avoid "read-only" error when using plt.imsave.
tampungan = plt.imread(nama_file + ".jpg")
row, col, depth = tampungan.shape
pic  = np.zeros(shape=(row, col, 3), dtype=np.uint8)
pic [:, :, :] = tampungan [:, :, :]

plt.figure()
plt.imshow(pic)
plt.ion()
plt.show()
plt.pause(2)

#The master logo has lots of noise color at its edges thus it should be purified at first.
#Defining the correct red, green and blue tone for UPJ logo for purification.
UPJ_pr = [235, 50, 55]; UPJ_pg = [0, 136, 84]; UPJ_pb = [1, 128, 195]  #UPJ's color (pure)

for i in range (0, row):
    for j in range (0, col):
        #Pixels with noise colors must be purified
        y, r, g, b = 0, 0, 0, 0
        pr = float(pic[i,j,0]) +1 ; pg = float(pic[i,j,1]) + 1; pb = float(pic[i,j,2]) + 1
        if (pr + pg + pb) > noise_threshold and pr/pg > 1.2 and pr/pb > 1.2:
            pic[i, j, 0], pic[i, j, 1], pic[i, j, 2] = UPJ_pr
        elif (pr + pg + pb) > noise_threshold and pg/pr > 1.2 and pg/pb > 1.2:
            pic[i, j, 0], pic[i, j, 1], pic[i, j, 2] = UPJ_pg
        elif (pr + pg + pb) > noise_threshold and pb/pr > 1.2 and pb/pg > 1.2:
            pic[i, j, 0], pic[i, j, 1], pic[i, j, 2] = UPJ_pb
        #Anything elses must be changed to black.
        else:
            pic[i, j, :] = 0

plt.imsave (nama_file + "b.jpg", pic)               #The "b" indicates "black"

plt.figure()
plt.imshow(pic)
plt.ion()
plt.show()
plt.pause(200)