from PIL import Image
import numpy as np
print("Введите имена исходного изображения и результата")
[imgIn, imgOut] = input().split(' ')
img = Image.open(imgIn)
imgArr = np.array(img)
height = len(imgArr)
width = len(imgArr[1])
cellHeight, cellWidth = 10, 10
grayScaleSteps = 50
i = 0

def getGrayLvlInCell(imgArr, cellHeight, cellWidth, i, j):
    grayLevel = 0
    for n in range(i, i + cellHeight):
        for m in range(j, j + cellWidth):
            red = imgArr[n][m][0]
            green = imgArr[n][m][1]
            blue = imgArr[n][m][2]
            rgbSum = int(red) + int(green) + int(blue)
            grayLevel += rgbSum / 3
    return int(grayLevel // (cellWidth * cellHeight))

def colorCell(imgArr, cellHeight, cellWidth, grayScaleSteps, i, j, grayLevel):
    for n in range(i, i + cellHeight):
        for m in range(j, j + cellWidth):
            imgArr[n][m][0] = int(grayLevel // grayScaleSteps) * grayScaleSteps
            imgArr[n][m][1] = int(grayLevel // grayScaleSteps) * grayScaleSteps
            imgArr[n][m][2] = int(grayLevel // grayScaleSteps) * grayScaleSteps

while i < height - 1:
    j = 0
    while j < width - 1:
        grayLevel = getGrayLvlInCell(imgArr, cellHeight, cellWidth, i, j)

        colorCell(imgArr, cellHeight, cellWidth, grayScaleSteps, i, j, grayLevel)

        j = j + cellWidth
    i = i + cellHeight

res = Image.fromarray(imgArr)
res.save(imgOut)
print("Результат готов!")