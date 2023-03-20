print("\033c")       #To close all
import numpy as np
from matplotlib import pyplot as plt

#============================================================================================
#=====================================    USER ENTRIES    ===================================
#============================================================================================
nama_file = "LOGO UPJ"
noise_threshold = 40                          #To anticipate noise color within the 3D space.
object_thickness = 0.2                                        #Relative to the 3D size

# THE USER DECIDES THE ROTATION ANGLES IN DEGREE
alfa_start = 0; beta_start = 0
delta_alfa = 0; delta_beta = 15
no_of_rotation = int(25)

#================================================================================================
#=================    DEFINING FUNCTION FOR DEGREE CONVERSION AND ROTATION    ===================
#================================================================================================
# Converting degree unit of alfa and beta to radiant unit
def degree_to_rad (alfa, beta):
    alfa_rad = (alfa / 180) * np.pi  # Converting degree to rad
    beta_rad = (beta / 180) * np.pi  # Converting dgreee to rad
    return alfa_rad, beta_rad

#FUNCTION TO ROTATE A VOXEL (vx,vy,vz) ABOUT A DEFINED CENTER (cx,cy,cz) AS MUCH AS ALFA RAD
#AROUND Z-AXIS THEN AS MUCH AS BETA RAD AROUND X-AXIS
def rotate(vx,vy,vz,cx,cy,cz,alfa_rad,beta_rad):
    #Check if 0' < alfa, beta < 360'
    if alfa_rad < 0 or alfa_rad > 2*np.pi or beta_rad < 0 or beta_rad > 2*np.pi:
        print ('Error: Each of alfa and beta must be between 0 and 360 degree.')
        quit()
    #This rotation works properly for angle between -180 and 180 degree, thus
    #e.g. 190 degree will be executed as -170 degree.
    if alfa_rad > np.pi: alfa_rad = alfa_rad - 2 * np.pi
    if beta_rad > np.pi: beta_rad = beta_rad - 2 * np.pi
    #Converting point's coordinate to be relative to the rotation center
    #so that the rotation matrix can be applied correctly.
    vx=vx-cx; vy=vy-cy; vz=vz-cz

    k = 0.5                                 #Correction factor
    # ROTATION 1 - Rotating the point as much as alfa around z-axis
    vx = round( np.cos(alfa_rad*k) * vx + np.sin(alfa_rad*k) * vy)
    vy = round(-np.sin(alfa_rad*k) * vx + np.cos(alfa_rad*k) * vy)
    vz = vz                                   #The z-coordinate of the voxel does not change.
    # ROTATION 2 - Rotating the point as much as beta around x-axis
    vz = round( np.cos(beta_rad*k) * vz + np.sin(beta_rad*k) * vy)
    vy = round(-np.sin(beta_rad*k) * vz + np.cos(beta_rad*k) * vy)
    vx = vx                                   #The x-coordinate of the voxel does not change.

    # Converting point's coordinate back, relative to (0,0,0)
    vx = vx + cx; vy = vy + cy; vz = vz + cz

    return vx, vy, vz  #Variabel input: vx,vy,vz, nama untuk variabel output tetap vx, vy, vz.

#============================================================================================
#=========================   CREATING A 3D MODEL FROM A 2D PICTURE   ========================
#============================================================================================
print ("Creating a 3D object...."); print ("")

#READING A PICTURE AS THE MASTER FOR THE 3D OBJECT
#The following technique is to avoid "read-only" error when using plt.imsave..
tampungan = plt.imread(nama_file + ".jpg")
row, col, depth = tampungan.shape
pic  = np.zeros(shape=(row, col, 3), dtype=np.uint8)
pic [:, :, :] = tampungan [:, :, :]

#CREATING THE TEMPLATE FOR THE 3D MODEL
#Ensure making a cubic 3D space and a square 2D screen.
length = row
col, row, length = col, row, length                               #Atau disesuaikan dg instruksi UAS.
#maks = max(pic.shape) + round (1.2 * object_thickness)           #Yang ini lebih aplikatif
#col, row, length = maks, maks, maks
voxel  = np.zeros(shape=(row, col, length, 3), dtype=np.uint8)    #Template for the 3D model
buffer = np.zeros(shape=(row, col, length, 3), dtype=np.uint8)    #Template for the 3D buffer
slice = np.zeros(shape=(row, col, 3), dtype=np.uint8)             #Template for the slice cut

#COPYING THE PICTURE ONTO THE CENTER OF THE 3D MATRIX
half_length = round(0.5*row)
thickness = round (object_thickness*row)
half_thickness = round (0.5*thickness)
for i in range (half_length-half_thickness, half_length+half_thickness):
    voxel[:, :, i, :] = pic [:, :, :]

# #Visualizing the cross slice at the half_length
# slice[:, :, :] = voxel[half_length, :, : :]
# plt.figure(1); plt.imshow(slice)
#
# #Visualizing the cross slice at the half_length
# slice[:, :, :] = voxel[:, half_length, :, :]
# plt.figure(2); plt.imshow(slice)
#
# #Visualizing the cross slice at the half_length
# slice[:, :, :] = voxel[:, :, half_length, :]
# plt.figure(3); plt.imshow(slice)
#
# plt.ion()
# plt.show()
# plt.pause(1)

np.save(nama_file + "_0_0.npy", voxel)


#============================================================================================
#==========================   MAIN PROGRAM TO ROTATE THE 3D OBJECT   ========================
#============================================================================================
print ("Rotating the 3D object...."); print ("")
cx = round(col/2); cy = round(row/2); cz = round(length/2)               #Center of rotation.
alfa = alfa_start
beta = beta_start
for r in range (0, no_of_rotation+1):
    alfa_rad, beta_rad = degree_to_rad(alfa, beta)                    #Convert degree to rad.
    print(''); print('Note: alfa and beta must be between 0 and 360 degree.')
    voxel = np.load(nama_file + "_0_0.npy")                     #Always reads original model.

    for i in range (0, row):                                  #Rotating te whole voxel[:,:,:]
        print('Alfa =', alfa, ', beta =', beta, ', now rotating voxels in row', i, '.')
        for j in range (0, col):
            for k in range (0, length):
                cek1 = int(voxel[i,j,k,0])
                cek2 = int(voxel[i,j,k,1])
                cek3 = int(voxel[i,j,k,2])
                if (cek1 + cek2 + cek3) > noise_threshold:
                    u, v, w = rotate(i,j,k,cx,cy,cz,alfa_rad,beta_rad) #Rotate the voxel
                    i, j, k, u, v, w = int(i), int(j), int(k), int(u), int(v), int(w)
                    buffer[u,v,w,:] = voxel[i,j,k,:]
                    #voxel[i,j,k,:] = 0 #The voxel that has been rotated must be put to black.

    print('Saving the result as a .npy file.')
    np.save(nama_file + "_" + str(alfa) + "_" + str(beta) + ".npy", buffer)
    voxel[:, :, :] = 0        #The 3D model must be reset so it's ready for the next job.
    buffer[:, :, :] = 0                                        #The same with the buffer.
    alfa = alfa + delta_alfa                                     #Angle for the next job.
    beta = beta + delta_beta                                     #Angle for the next job.
