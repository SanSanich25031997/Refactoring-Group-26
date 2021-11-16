from PIL import Image
import numpy as np


def FindMedianSaturation(startX, startY, mosaicPix, imageMatrix):
    medianSat = 0
    for n in range(startX, startX + mosaicPix):
        for n0 in range(startY, startY + mosaicPix):
            redSat = imageMatrix[n][n0][0]
            greenSat = imageMatrix[n][n0][1]
            blueSat = imageMatrix[n][n0][2]
            pixelSat = int(redSat) + int(greenSat) + int(blueSat)
            medianSat += pixelSat/3
    return int(medianSat // 100)


def ApplyMedianSaturation(startX, startY, mosaicPix, medianSat,
                          graySens, imageMatrix):
    for n in range(startX, startX + mosaicPix):
        for n1 in range(startY, startY + mosaicPix):
            imageMatrix[n][n1][0] = int(medianSat // graySens) * graySens
            imageMatrix[n][n1][1] = int(medianSat // graySens) * graySens
            imageMatrix[n][n1][2] = int(medianSat // graySens) * graySens

img = Image.open("img2.jpg")
imageMatrix = np.array(img)
mosaicPix = 5
graySens = 10
height = len(imageMatrix)
width = len(imageMatrix[1])
for i in range(0, height - 1, mosaicPix):
    for j in range(0, width - 1, mosaicPix):
        medianSat = FindMedianSaturation(i, j, mosaicPix, imageMatrix)
        ApplyMedianSaturation(i, j, mosaicPix, medianSat,
                              graySens, imageMatrix)
res = Image.fromarray(imageMatrix)
res.save('res8.jpg')

print('pilik pilik')
