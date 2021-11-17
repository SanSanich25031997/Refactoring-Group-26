from PIL import Image
import numpy as np
from numpy.lib.shape_base import tile

img = Image.open("img2.jpg")
tile_step = int(input("Введите размер мозаики: "))
gray_step = int(input("Введите количество градаций серого: "))
arr = np.array(img, dtype = np.int32)
arr_length = len(arr)
arr_1_length = len(arr[1])

def paintGray(arr, tile_step, gray_step, sum):
    sum = int(sum // 100)
    for a in range(i, i + tile_step):
        for b in range(j, j + tile_step):
            arr[a][b][0] = int(sum // 50) * gray_step
            arr[a][b][1] = int(sum // 50) * gray_step
            arr[a][b][2] = int(sum // 50) * gray_step

def drawImage(arr, tile_step, gray_step):
    sum = 0
    for x in range(i, i + tile_step):
        for y in range(j, j + tile_step):
            n1 = arr[x][y][0]
            n2 = arr[x][y][1]
            n3 = arr[x][y][2]
            M = (n1 + n2 + n3) // 3
            sum += M
    paintGray(arr, tile_step, gray_step, sum)


i = 0
while i < arr_length - 1:
    j = 0
    while j < arr_1_length - 1:
        drawImage(arr, tile_step, gray_step)
        j = j + tile_step
    i = i + tile_step
res = Image.fromarray(arr.astype(np.uint8))
res.save('res.jpg')