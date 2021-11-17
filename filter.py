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


imgInName = input(
    "Введите название входного изображения в формате \"imageName.jpg\":")

if imgInName == '':
    print('Пустые имена не разрешены!')
    print('Выход из программы...')
    quit()

imgOutName = input(
    "Введите название выходного изображения в формате \"resultName.jpg\":")

if imgOutName == '':
    print('Название выходного изображения будет заменено на \"resultImage.jpg\".')
    imgOutName = 'resultImage.jpg'

img = Image.open(imgInName)
imgArray = np.array(img)
height = len(imgArray)
width = len(imgArray[0])

cellHeight, cellWidth = 10, 10  # Высота и ширина мозаики (в пикселях)
grayscaleSteps = 5  # Количество градаций серого
grayscaleValue = int(255 / grayscaleSteps)

for i in range(0, height - 1, cellHeight):
    for j in range(0, width - 1, cellWidth):
        brightness = GetCellBrightness(imgArray, i, j, cellHeight, cellWidth)
        ApplyGrayscale(imgArray, brightness, i, j, cellHeight, cellWidth)
res = Image.fromarray(imgArray)

try:
    res.save(imgOutName)
except BaseException:
    print('Ошибка в записи файла, проверьте корректность названия выходного изображения.')
    print('Выход из программы...')
    quit()

print('Дело сделано!')
