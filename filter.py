from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a:
    j = 0
    while j < a1:
        s = 0
        for row in range(i, i + 10):
            for column in range(j, j + 10):
                red = arr[row][column][0]
                green = arr[row][column][1]
                blue = arr[row][column][2]
                M = int(red) + int(green) + int(blue)
                s += M / 3
        s = int(s // 100)
        for row in range(i, i + 10):
            for column in range(j, j + 10):
                arr[row][column][0] = int(s // 50) * 50
                arr[row][column][1] = int(s // 50) * 50
                arr[row][column][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
