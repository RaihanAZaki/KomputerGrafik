print("\033c")  # To close all
import numpy as np
from matplotlib import pyplot as plt
import cv2

# =====================================================================================
# =================================    USER ENTRIES    ================================
# =====================================================================================
# THE USER DECIDES THE ROTATION ANGLES IN DEGREE
alfa = 1;
beta = 1;
step = 45

# THE USER DECIDES THE LINE WIDTH (E.G. 4)
lw = int(4);
pd = int(2 * lw);

# THE USER DECIDES THE ZOOM FACTOR (RECOMMENDED: BETWEEN 0.3 TO 1.2)
zoom = 1.6
print("Zoom =", zoom)

# THE USER DECIDES THE SIZE OF THE 3D ROOM AND THE 2D SCREEN (MAX 1920 BY 1080)
col = 1000;
row = 1000;
length = 1000

# PROGRAMMER SETS THE CAM POSITION
cam = [int(col / 2), int(row / 2), int(-2 * length)]  # Cam position (x, y, z)
cam_x = cam[0];
cam_y = cam[1];
cam_z = cam[2]
print("Camera Position =", cam_z)

# COORDINATES OF ALL POINTS (VERTICES)
no_of_points = 8
x1, x2, x3, x4, x5, x6, x7, x8 = 300, 300, 300, 300, 700, 700, 700, 700
y1, y2, y3, y4, y5, y6, y7, y8 = 400, 400, 600, 600, 400, 400, 600, 600
z1, z2, z3, z4, z5, z6, z7, z8 = 480, 520, 520, 480, 480, 520, 520, 480
c1, c2, c3, c4, c5, c6, c7, c8 = 1, 2, 3, 4, 5, 6, 7, 8  # color of each point

# THE USER DECIDES THE LINES (EDGES) TO BE CREATED BETWEEN POINTS
line = [[0, 0], [1, 2], [2, 3], [3, 4], [4, 1], [5, 6], [6, 7], [7, 8], [8, 5], [1, 5], [2, 6], [3, 7], [4, 8]]


# ================================================================================================
# =======================================   DEFINING FUNCTIONS  ==================================
# ================================================================================================
# FUNCTION TO ROTATE A POINT (px,py,pz) ABOUT A DEFINED CENTER (cx,cy,cz) AS MUCH AS ALFA DEGREE
# AROUND Z-AXIS THEN AS MUCH AS BETA DEGREE AROUND X-AXIS
def rotate(px, py, pz, cx, cy, cz, alfa, beta):
    # Converting degree unit of alfa and beta to radiant unit
    alfa_rad = (alfa / 180) * np.pi  # Converting degree to rad
    beta_rad = (beta / 180) * np.pi  # Converting dgreee to rad
    print("alfa =", alfa, 'degree =', alfa_rad, 'rad')
    print("beta =", beta, 'degree =', beta_rad, 'rad')

    # k = 0.9575                                  #Correction factor
    k = 1
    # ROTATION 1 - Rotating the point as much as alfa_rad around z-axis
    if abs(alfa) > 1e-2:
        # Rotation center is (0, 0, pz)
        px = px - cx  # Converting point's coordinate to be relative to the
        py = py - cy  # rotation center so that rotation matrix applies
        # pz = pz     #pz retains
        px = round(np.cos(alfa_rad * k) * px + np.sin(alfa_rad * k) * py)
        py = round(-np.sin(alfa_rad * k) * px + np.cos(alfa_rad * k) * py)
        # pz =  pz
        px = px + cx  # Putting px back
        py = py + cy  # Putting py back
    # ROTATION 2 - Rotating the point as much as beta rad around x-axis
    if abs(beta) > 1e-2:
        # px = px
        py = py - cy
        pz = pz - cz
        pz = round(np.cos(beta_rad * k) * pz + np.sin(beta_rad * k) * py)
        py = round(-np.sin(beta_rad * k) * pz + np.cos(beta_rad * k) * py)
        # px = px
        py = py + cy
        pz = pz + cz

    return px, py, pz  # Variabel input: px,py,pz, nama untuk variabel output tetap px, py, pz.


# A FUNCTION TO PROJECT A POINT IN THE 3D ROOM (px, py, pz) TO THE 2D SCREEN
def projection_3D_to_2D(px, py, pz, cam_x, cam_y, cam_z, scr_z):
    # The projection is done in the direction of z.
    # As the number of object's points is small, I decide to do projection
    # for the points, one by one. This is the reason that I chose the ray
    # direction from object to the cam to the screen.
    mx = (cam_x - px) / (cam_z - pz)  # mx = dx/dy
    my = (cam_y - py) / (cam_z - pz)  # my = dy/dz
    Dz = scr_z - pz
    # Find the x and y of the landing point of the longer line on the screen using
    # the theorem that the gradient of the longer line is the same as the gradient
    # of the shorter line.
    # (Dx/Dz) = mx  => (scr_x-obj_x) / Dz = mx => scr_x = obj_x + mx*Dz
    # Similarly                                => scr_y = obj_y + my*Dz
    scr_x = int(px + mx * Dz)
    scr_y = int(py + my * Dz)
    return scr_x, scr_y


# FUNCTION OF COLOR CODE TABLE
def color_code(code):
    if code == 1:
        color = [255, 0, 0]  # red
    if code == 2:
        color = [0, 255, 0]  # green
    if code == 3:
        color = [255, 255, 0]  # yellow
    if code == 4:
        color = [255, 255, 255]  # white
    if code == 5:
        color = [255, 0, 0]
    if code == 6:
        color = [0, 255, 0]
    if code == 7:
        color = [255, 255, 0]
    if code == 8:
        color = [255, 255, 255]
    return color
    # Entah kenapa warna biru tidak dapat muncul.


# FUNCTION TO DRAW POINT-m (scr_xm, scr_ym) AND POINT-n (scr_xn, scr_yn)
# AND DRAW THE LINE IN BETWEEN on the 2D SCREEN
def drawing_point_and_line(scr_xm, scr_ym, cm, scr_xn, scr_yn, cn, hd, hw):
    # Drawing point(m)
    for i in range(scr_xm - hd, scr_xm + hd):
        for j in range(scr_ym - hd, scr_ym + hd):
            if ((i - scr_xm) * 2 + (j - scr_ym) * 2) < (hd) ** 2:
                Screen_2D[j, i, 0:2] = cm[0:2]
    # Drawing point👎
    for i in range(scr_xn - hd, scr_xn + hd):
        for j in range(scr_yn - hd, scr_yn + hd):
            if ((i - scr_xn) * 2 + (j - scr_yn) * 2) < (hd) ** 2:
                Screen_2D[j, i, 0:2] = cn[0:2]

    # Drawing the line between point(m) and point👎
    my = 0;
    mx = 0  # Put my and mx initially to zero.

    # Finding the min and max for the loop of creating dots between point[m] and point[n]
    x_min = min(scr_xm, scr_xn);
    x_max = max(scr_xm, scr_xn)
    y_min = min(scr_ym, scr_yn);
    y_max = max(scr_ym, scr_yn)

    dy = scr_yn - scr_ym
    dx = scr_xn - scr_xm
    # print('dy, dx =', dy, ',', dx)

    if abs(dy) <= abs(dx):
        # print('Now creating the line using my........'); print("")
        my = dy / dx
        for i in range(x_min, x_max):
            j = int(my * (i - scr_xm) + scr_ym)  # Finding y using the line equation
            x = i
            y = j
            # print('p_x, p_y =', x, ',', y)
            for i in range(x - hw, x + hw):  # Creating a circle surrounding (x,y) and coloring it.
                for j in range(y - hw, y + hw):
                    if ((i - x) * 2 + (j - y) * 2) < hw ** 2:
                        Screen_2D[j, i, 2] = 255
    if abs(dx) < abs(dy):
        # print('Now creating the line using mx........'); print("")
        mx = dx / dy
        for j in range(y_min, y_max):
            i = int(mx * (j - scr_ym) + scr_xm)  # Finding x using the line equation
            y = j
            x = i
            # print('p_x, p_y =', x, ',', y)
            for i in range(x - hw, x + hw):  # Creating a circle surrounding (x,y) and coloring it red
                for j in range(y - hw, y + hw):
                    if ((i - x) * 2 + (j - y) * 2) < hw ** 2:
                        Screen_2D[j, i, 2] = 255


# ================================================================================================
# ==========================================     MAIN PROGRAM    =================================
# ================================================================================================
print('STEP 1: PREPARATION')
# DECIDING 2D SCREEN POSITION BASED ON CAM POSITION (cam_z) AND ZOOM FACTOR
# PLEASE NOTE THAT ZOOM FACTOR = DIST. BETW. SCREEN AND CAM / DIST. BETW. CAM AND 3D ROOM
d1 = cam_z - 0  # The z position of the 3D room is 0.
d2 = zoom * d1
scr_z = round(d1 + d2)  # The z position of screen.
print('2D Screen Position =', scr_z);
print('')

# Setting the size of the screen
col = col;
row = row

# Preparing the template for 2D screen (initially black)
Screen_2D = np.zeros(shape=(row, col, 3), dtype=np.uint8)

# Preparing template for point coordinates on the 2D screen after projection
scr_x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
scr_y = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Variables for drawing point and lines
hd = int(pd / 2);
hw = int(lw / 2)

print('STEP-2: CREATING THE 3D MODEL...')
# Index 0 is unused. Index 9 is to fix the 3D visualization of the plt.
# Index 1 to 8 corelates to p1 to p8 of the cuboid.
x = [0, x1, x2, x3, x4, x5, x6, x7, x8, col]  # coordinate x of each point
y = [0, y1, y2, y3, y4, y5, y6, y7, y8, row]  # coordinate y of each point
z = [0, z1, z2, z3, z4, z5, z6, z7, z8, length]  # coordinate z of each point
c = [0, c1, c2, c3, c4, c5, c6, c7, c8, c8]  # color of each point

print('Showing the 3D model...')
plt.figure(figsize=(3, 3), dpi=200)  # width and height in inches
gambar_3D = plt.axes(projection='3d');
gambar_3D.scatter3D(x, y, z)
gambar_3D.set_xlabel('x');
gambar_3D.set_ylabel('y');
gambar_3D.set_zlabel('z')
plt.ion()
plt.pause(2)
plt.show()
print("")

print('STEP-3: PROJECTING THE 3D MODEL TO THE 2D SCREEN...')
for i in range(1, no_of_points + 1):
    scr_x[i], scr_y[i] = projection_3D_to_2D(x[i], y[i], z[i], cam_x, cam_y, cam_z, scr_z)
    print('Projecting the still object...', 'scr_x', i, '=', scr_x[i], ', scr_y', i, '=', scr_y[i])
for r in range(1, len(line)):
    m = line[r][0]
    n = line[r][1]
    cm = color_code(c[m])
    cn = color_code(c[n])
    scr_xm = scr_x[m];
    scr_ym = scr_y[m];
    scr_xn = scr_x[n];
    scr_yn = scr_y[n]
    drawing_point_and_line(scr_xm, scr_ym, cm, scr_xn, scr_yn, cn, hd, hw)
plt.imsave("screen_2D_" + str(alfa) + ".jpg", Screen_2D)
proyeksi = cv2.imread("screen_2D_" + str(alfa) + ".jpg")
cv2.imshow("3D Animation", proyeksi)
cv2.waitKey(1000)
Screen_2D[0:255, 0:255, 0:2] = 0  # Put the 2D Screen back to black.

print('STEP-4: NOW ROTATING, PROJECTING, DRAWING AND SHOWING POINTS AND LINES...')
for s in range(1, step + 1):
    Screen_2D[:, :, :] = 0  # Put the 2D screen back to black.
    print('======  Rotating Step  ======', r);
    print('')
    print("Point locations before being rotated:")
    print(x);
    print(y);
    print(z);
    print("")
    print("alfa, beta =", alfa, ",", beta);
    print("")
    cx = int(col / 2);
    cy = int(row / 2);
    cz = int(length / 2)  # Rotation axis is the 3D room center.
    for i in range(1, no_of_points + 1):
        print('Rotating point', i, ':')
        px, py, pz = rotate(x[i], y[i], z[i], cx, cy, cz, alfa, beta)
        x[i] = px;
        y[i] = py;
        z[i] = pz
    print("Point locations after being rotated:")
    print(x);
    print(y);
    print(z);
    print('')

    print('Now projecting 3D tO 2D for every point...')
    # x[i], y[i] dan z[i] is the 3D object to be projected
    for i in range(1, no_of_points + 1):
        scr_x[i], scr_y[i] = projection_3D_to_2D(x[i], y[i], z[i], cam_x, cam_y, cam_z, scr_z)
        print('scr_x', i, '=', scr_x[i], ', scr_y', i, '=', scr_y[i])
    print('')

    print('Now drawing points and lines on the 2D screen...')
    for r in range(1, len(line)):
        # Finding which two points are to be connected with a line
        # Point[m] and point[n] are to be connected.
        m = line[r][0]
        n = line[r][1]
        cm = [0, 0, 0];
        cn = [0, 0, 0]
        cm = color_code(c[m])
        cn = color_code(c[n])
        print('Now coloring point m and point n where m, cm, n, cn =', m, ',', cm, ',', n, ',', cn)
        # print('scr_x, scr_y', [m], '=', scr_x[m], ',', scr_y[m])
        # print('scr_x, scr_y', [n], '=', scr_x[n], ',', scr_y[n])
        scr_xm = scr_x[m];
        scr_ym = scr_y[m];
        scr_xn = scr_x[n];
        scr_yn = scr_y[n]
        drawing_point_and_line(scr_xm, scr_ym, cm, scr_xn, scr_yn, cn, hd, hw)
    print('')
    # animasi = plt.imread("screen_2D_"+ str(alfa) + ('') + str(beta) + ('') + str(s) + ".jpg")
    plt.imsave("screen_2D_" + str(alfa) + ('') + str(beta) + ('') + str(s) + ".jpg", Screen_2D)
    animasi = cv2.imread("screen_2D_" + str(alfa) + ('') + str(beta) + ('') + str(s) + ".jpg")
    cv2.imshow("3D ANIMATION", animasi)
    cv2.waitKey(1)
    Screen_2D[0:255, 0:255, 0:2] = 0  # Put the 2D Screen back to black.
    # cv2.destroyAllWindows()

print('STEP-5: SHOWING THE LAST IMAGE FOR A WHILE')
cv2.imshow("3D ANIMATION", animasi)
cv2.waitKey(100000)
