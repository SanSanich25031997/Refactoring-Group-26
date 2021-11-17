from PIL import Image
import numpy as np


def GetCellBrightness(imgArray, i, j, cellHeight, cellWidth):
    sumBright = 0
    for row in range(i, i + cellHeight):
        for col in range(j, j + cellWidth):
            rgbSum = 0
            for rgb in range(3):
                rgbSum += int(imgArray[row][col][rgb])
            sumBright += rgbSum / 3
    return int(sumBright // (cellHeight ** 2))


def ApplyGrayscale(imgArray, brightness, i, j, cellHeight, cellWidth):
    for row in range(i, i + cellHeight):
        for col in range(j, j + cellWidth):
            for rgb in range(3):
                imgArray[row][col][rgb] = int(
                    brightness // grayscaleValue) * grayscaleValue


img = Image.open("img2.jpg")
imgArray = np.array(img)
height = len(imgArray)
width = len(imgArray[0])

cellHeight, cellWidth = 10, 10
grayscaleSteps = 5
grayscaleValue = int(255 / grayscaleSteps)


for i in range(0, height - 1, cellHeight):
    for j in range(0, width - 1, cellWidth):
        brightness = GetCellBrightness(imgArray, i, j, cellHeight, cellWidth)
        ApplyGrayscale(imgArray, brightness, i, j, cellHeight, cellWidth)

res = Image.fromarray(imgArray)
res.save('res.jpg')
