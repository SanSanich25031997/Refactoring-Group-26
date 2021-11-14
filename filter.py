from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
#python filter.py

mosaic_size = 5
gradation_gray = 5


np.clip(arr, 0, 255)#обработка  возможного переполнения???

height = len(arr)
width = len(arr[1])
print(height, width)

i = 0
while i < height - 1: #полосы справа и снизу обрабатываются корректно, если 11 заменить на 1
    j = 0
    while j < width - 1:
        gray = 0
        for n in range(i, i + mosaic_size):
            for n1 in range(j, j + mosaic_size):
                R = arr[n][n1][0] #место, где запутался с именами переменных
                G = arr[n][n1][1]
                B = arr[n][n1][2]
                gray += (R + G + B) / 3 #при расчетах среднего необходимо поделить на 3
        gray = int(gray // 10)
        for n in range(i, i + mosaic_size):
            for n1 in range(j, j + mosaic_size):
                arr[n][n1][0] = int(gray // gradation_gray) * gradation_gray  #компоненты серого делим на три
                arr[n][n1][1] = int(gray // gradation_gray) * gradation_gray
                arr[n][n1][2] = int(gray // gradation_gray) * gradation_gray
        j = j + mosaic_size
    i = i + mosaic_size

res = Image.fromarray(arr)
res.save('res.jpg')
