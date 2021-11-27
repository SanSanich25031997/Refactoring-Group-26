from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
width = len(arr)
height = len(arr[1])
i = 0
while i < width - 1:
    j = 0
    while j < height - 1:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                r = int(arr[n][n1][0])
                g = int(arr[n][n1][1])
                b = int(arr[n][n1][2])
                M = int(r) + int(g) + int(b)
                s += M / 3
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')

