from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
#python filter.py

mosaic_size = 5
number_of_shades = 10
height = len(arr)
width = len(arr[1])

i = 0
while i < height - mosaic_size + 1:
    j = 0
    while j < width - mosaic_size + 1:
        average_value = 0
        for n in range(i, i + mosaic_size):
            for n1 in range(j, j + mosaic_size):
                R = arr[n][n1][0]
                G = arr[n][n1][1]
                B = arr[n][n1][2]
                average_value += (R + G + B) / 3
        average_value = int(average_value // 10)
        conversion_factor = 255 / (number_of_shades - 1) # conversion_factor позволяет контролировать колличество оттенков серого
        for n in range(i, i + mosaic_size):
            for n1 in range(j, j + mosaic_size):
                arr[n][n1][0] = int(average_value / conversion_factor + 0.5) * conversion_factor  #тут была ошибка при преобразовании чисел с плавающей запятой
                arr[n][n1][1] = int(average_value / conversion_factor + 0.5) * conversion_factor
                arr[n][n1][2] = int(average_value / conversion_factor + 0.5) * conversion_factor
        j = j + mosaic_size
    i = i + mosaic_size

res = Image.fromarray(arr)
res.save('res.jpg')
