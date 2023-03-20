def buat_titik(Gambar, y1, x1, y2, x2, y3, x3, y4, x4, hd):
    for i in range(x1 - hd, x1 + hd + 1):
        for j in range(y1 - hd, y1 + hd + 1):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, :] = 0
                Gambar[j, i, 0] = 255

    for i in range(x2 - hd, x2 + hd + 1):
        for j in range(y2 - hd, y2 + hd + 1):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, :] = 0
                Gambar[j, i, 0] = 255

    for i in range(x3 - hd, x3 + hd + 1):
        for j in range(y3 - hd, y3 + hd + 1):
            if ((i - x3) ** 2 + (j - y3) ** 2) < hd ** 2:
                Gambar[j, i, :] = 0
                Gambar[j, i, 0] = 255

    for i in range(x4 - hd, x4 + hd + 1):
        for j in range(y4 - hd, y4 + hd + 1):
            if ((i - x4) ** 2 + (j - y4) ** 2) < hd ** 2:
                Gambar[j, i, :] = 0
                Gambar[j, i, 0] = 255
    return Gambar