from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arrImg = np.array(img)
height = len(arrImg)
width = len(arrImg[1])

i = 0
while i < height - 1:
    j = 0
    while j < width - 1:
        sumBright = 0
        for y in range(i, i + 10):
            for x in range(j, j + 10):
                R = arrImg[y][x][0]
                G = arrImg[y][x][1]
                B = arrImg[y][x][2]
                rgbSum = int(R) + int(G) + int(B)
                sumBright += rgbSum / 3
        brightness = int(sumBright // 100)

        for y in range(i, i + 10):
            for x in range(j, j + 10):
                arrImg[y][x][0] = int(brightness // 50) * 50
                arrImg[y][x][1] = int(brightness // 50) * 50
                arrImg[y][x][2] = int(brightness // 50) * 50
        j = j + 10
    i = i + 10

res = Image.fromarray(arrImg)
res.save('res.jpg')
