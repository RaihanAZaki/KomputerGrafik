import numpy as np
from matplotlib import pyplot as plt
from skimage.io import imsave, imread
import time

print ("Acquiring user entries.")

th = 20
th2 = 20

green_lw = 4
print("th, th2, green_lw =", th, th2, green_lw)
print (" ")
path = "C://Users//Usern//PycharmProjects//pythonProject//Visi Komputer//Pertemuan10_n_11//"
nama_file_input = path + "coneicecream.jpg"; th2 = 20

#########################################################################
print ("Reading the input file, acquiring its size and creating array templates for processing.")
#########################################################################

pic = plt.imread(nama_file_input)
row, col, depth = np.shape(pic)
print("col, row, depth =", row, col, depth)
ori = np.zeros(shape=(row, col, depth), dtype = np.uint8)
buffer = np.zeros(shape=(row, col, depth), dtype = np.uint8)
ori[:, :, :] = pic[:,:,:]
buffer[:, :, :] = pic[:,:,:]
plt.figure('Original Image')
plt.imshow(ori)
plt.ion()
plt.show()
plt.pause(0.01)
print("")
#########################################################################
print ("Preliminary edge detection (Algoritma #1) is taking place.")
print ("Every pixel that idicates any kind of object edge will be colored red. Check it out.")
print ("At the same time, we are finding object weight center, x_min, x_max, y_min, and y_max.")
#########################################################################
y_start = 0; y_end = row
x_start = 0; x_end = col
n = 0
yc = y_start
xc = x_start
y_min = y_end
y_max = y_start
x_min = x_end
x_max = x_start
for i in range (0+1, row-1):
    for j in range (0+1, col-1):
        cek1, cek2, cek3, cek4, cek5, cek6, cek7, cek8, cek9 = \
        False, False, False, False, False, False, False, False, False

        point_r = ori[i,j,0]; point_g = ori[i,j,1]; point_b = ori[i,j,2]
        neigh1_r = ori[i-1, j, 0]; neigh1_g = ori[i-1, j, 1]; neigh1_b = ori[i-1, j, 2]
        neigh2_r = ori[i , j-1, 0]; neigh2_g = ori[i , j-1, 1]; neigh2_b = ori[i , j-1, 2]
        neigh3_r = ori[i+1, j, 0]; neigh3_g = ori[i+1, j, 1]; neigh3_b = ori[i+1, j, 2];
        neigh4_r = ori[i, j+1, 0]; neigh4_g = ori[i, j+1, 1]; neigh4_b = ori[i, j+1, 2];
        cek_n1r = abs(int(neigh1_r) - int(point_r))
        cek_n2r = abs(int(neigh2_r) - int(point_r))
        cek_n3r = abs(int(neigh3_r) - int(point_r))
        cek_n4r = abs(int(neigh4_r) - int(point_r))

        if cek_n1r > th2 or cek_n2r > th2 or cek_n3r > th2 or cek_n4r > th2:
            buffer[i,j,:] = 255,0,0
            n = n + 1
            yc = yc + i
            xc = xc + j
            if i < y_min: y_min = i
            if i > y_max: y_max = i
            if j < x_min: x_min = j
            if j > x_max: x_max = j

yc = round (yc/n)
xc = round (xc/n)
print("y_min, yc, y_max =", y_min, yc, y_max, ".")
print("x_min, xc, x_max =", x_min, xc, x_max, ".")
print("")
plt.figure('Preliminary Edge Detection')
# imsave("edgepertama.jpg", buffer)
plt.imshow(buffer)
plt.ion()
plt.show()
plt.pause(0.01)

#########################################################################
print("Final edge detection (Algorithm #2) is taking place.")
print("Paint the outmost edge pixels is every line green.")
#########################################################################
print("Preparing arrays to accomodate edge pixel properties: coordinates and colors.")
print("The edge array has a length and contains index number, y_edge, x_edge, R_edge, G_edge, and B_edge.")
time.sleep(5)
len_edge = max(2*(y_max-y_min), 2*(x_max-x_min)) + 2
indeks_edge = np.zeros(shape = (len_edge), dtype = int)
y_edge = np.zeros(shape = (len_edge), dtype = int)
x_edge = np.zeros(shape = (len_edge), dtype = int)
R_edge = np.zeros(shape = (len_edge), dtype = int)
G_edge = np.zeros(shape = (len_edge), dtype = int)
B_edge = np.zeros(shape = (len_edge), dtype = int)
G_edge[:] = 255


print("If any object resides too close to image margin, edge detection can cause 'Index is out of bound'.")
margin = int(green_lw)
if y_min < 0 + margin: y_min = 0 + margin
if y_max > row - margin: y_max = row - margin
if x_min < 0 + margin: x_min = 0 + margin
if x_max > col - margin: x_max = col - margin

if (x_max - x_min >= y_max - y_min) or (x_max - x_min < y_max - y_min):
    counter = 0
    for i in range (y_min, y_max+1):
        print("")
        indeks_edge[counter] = counter
        y_edge[counter] = i
        n = 0
        x = 0
        for j in range (xc, x_max+1):
            cek1 = bool(buffer[i,j,0] == 255 and buffer[i,j,1] == 0 and buffer[i,j,2] == 0)
            cek2 = bool(buffer[i, j+1, 0] == 255 and buffer[i, j+1, 1] == 0 and buffer[i, j+1, 2] == 0)
            cek3 = bool(buffer[i, j+2, 0] == 255 and buffer[i, j+2, 1] == 0 and buffer[i, j+2, 2] == 0)
            if cek1 == True and cek2 == False and cek3 == False:
                print('Finding a rightmost edge in a row:', i, ",", j)
                x_edge[counter] = j
        counter = counter + 1

    print(""); print("It's now halfway."); print("")

    for i in range (y_max, y_min-1, -1):
        print("")
        indeks_edge[counter] = counter
        y_edge[counter] = i
        n = 0
        x = 0
        for j in range(xc, x_min-1, -1):
            cek1 = bool(buffer[i, j, 0]     == 255 and buffer[i, j, 1]     == 0 and buffer[i, j, 2]     == 0)
            cek2 = bool(buffer[i, j - 1, 0] == 255 and buffer[i, j - 1, 1] == 0 and buffer[i, j - 1, 2] == 0)
            cek3 = bool(buffer[i, j - 2, 0] == 255 and buffer[i, j - 2, 1] == 0 and buffer[i, j - 2, 2] == 0)
            if cek1 == True and cek2 == False and cek3 == False:
                print('Finding a leftmost edge in a row:', i, ",", j)
                x_edge[counter] = j
        counter = counter + 1

#######################################################################
print("Now applying the edge arrays to color the outermost edge pixels in picture green. Check it out.")
#######################################################################
for i in range (0, len_edge):
    buffer[y_edge[i], x_edge[i], 0:3] = R_edge[i], G_edge[i], B_edge[i]
    buffer[y_edge[i], x_edge[i]-1, 0:3] = R_edge[i], G_edge[i], B_edge[i]
    buffer[y_edge[i], x_edge[i]+1, 0:3] = R_edge[i], G_edge[i], B_edge[i]
    buffer[y_edge[i], x_edge[i]-2, 0:3] = R_edge[i], G_edge[i], B_edge[i]
    buffer[y_edge[i], x_edge[i]+2, 0:3] = R_edge[i], G_edge[i], B_edge[i]

# cropimage = np.zeros(shape=(y_max - y_min, x_max - x_min, depth), dtype= np.uint8)
# print(cropimage)
# cropimage[:, :, :] = 0
# x_max_crop = x_max - x_min
# y_max_crop = y_max - y_min
# x_min = 0
# y_min = 0
#
# for i in range (x_min, x_max_crop):
#     for j in range (y_min, x_max_crop):
#         cropimage[i,j,0] = buffer[i+y_min, j+x_min, 0]
#         cropimage[i,j,1] = buffer[i+y_min, j+x_min, 1]
#         cropimage[i,j,2] = buffer[i+y_min, j+x_min, 2]
#
#
# plt.figure('Final Crop')
# # imsave("Final_edge2.jpg", buffer)
plt.imshow(buffer)
# plt.imshow(cropimage)
plt.ion()
plt.show()
plt.pause(200)
