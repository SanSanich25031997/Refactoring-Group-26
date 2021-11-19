from PIL import Image
import numpy as np

def FindMedianSaturation(i,j,mosaicPartSide, imageMatrix):
    medianSaturation = 0
    for n in range(i, i + mosaicPartSide):
        for n0 in range(j, j + mosaicPartSide):
            redSat = imageMatrix[n][n0][0]
            greenSat = imageMatrix[n][n0][1]
            blueSat = imageMatrix[n][n0][2]
            pixelSat = int(redSat) + int(greenSat) + int(blueSat)
            medianSaturation += pixelSat/3
    return int(medianSaturation // 100)

def ApplyMedianSaturation(i, j, mosaicPartSide, medianSaturation, graySensitivity, imageMatrix):
    for n in range(i, i + mosaicPartSide):
        for n1 in range(j, j + mosaicPartSide):
            imageMatrix[n][n1][0] = int(medianSaturation // graySensitivity) * graySensitivity
            imageMatrix[n][n1][1] = int(medianSaturation // graySensitivity) * graySensitivity
            imageMatrix[n][n1][2] = int(medianSaturation // graySensitivity) * graySensitivity

print('введите полные названия файлов')
imgadreses=input().split(' ')
img = Image.open(imgadreses[0])
imageMatrix = np.array(img)
mosaicPartSide = 5
graySensitivity = 10
height = len(imageMatrix)
width = len(imageMatrix[1])
for i in range(0, height - 1, mosaicPartSide):
    for j in range(0, width - 1, mosaicPartSide):
        medianSaturation = FindMedianSaturation(i, j, mosaicPartSide, imageMatrix)
        ApplyMedianSaturation(i, j, mosaicPartSide, medianSaturation, graySensitivity, imageMatrix)
res = Image.fromarray(imageMatrix)
res.save(imgadreses[1])

print('pilik pilik')
