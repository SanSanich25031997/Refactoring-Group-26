from PIL import Image
import numpy as np
#python filter.py

def count_average_value(col, row):
    average_value = 0

    for i in range(col, col + mosaic_size):
        for j in range(row, row + mosaic_size):
            R = arr[i][j][0]
            G = arr[i][j][1]
            B = arr[i][j][2]
            average_value += (R + G + B) / 3

    return int(average_value // 10) if mosaic_size < 10 else int(average_value // 100)

def paint_mosaic(col, row):
    conversion_factor = 255 / (number_of_shades - 1)

    for i in range(col, col + mosaic_size):
        for j in range(row, row + mosaic_size):
            arr[i][j][0] = int(average_value / conversion_factor + 0.5) * conversion_factor
            arr[i][j][1] = int(average_value / conversion_factor + 0.5) * conversion_factor
            arr[i][j][2] = int(average_value / conversion_factor + 0.5) * conversion_factor


input_img = input("Введите имя исходного изображения: ")
input_result = input("Введите имя результирующего изображения: ")
img = Image.open(input_img)
arr = np.array(img)
mosaic_size = int(input('Введите размер мозайки: '))
number_of_shades = int(input('Введите градацию серого: '))
height = len(arr)
width = len(arr[1])

col = 0
while col < height - mosaic_size + 1:
    row = 0
    while row < width - mosaic_size + 1:
        average_value = count_average_value(col, row)
        paint_mosaic(col, row)
        row = row + mosaic_size
    col = col + mosaic_size

res = Image.fromarray(arr)
res.save(input_result)
