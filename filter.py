from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 1:
    j = 0
    while j < a1 - 1:
        s = 0
        for n in range(i, i + 10):
            for h in range(j, j + 10):
                r = arr[n][h][0]
                g = arr[n][h][1]
                b = arr[n][h][2]
                M = int(r) + int(g) +int(b)
                s += M/3
        s = int(s // 100)
        for n in range(i, i + 10):
            for h in range(j, j + 10):
                arr[n][h][0] = int(s // 50) * 50
                arr[n][h][1] = int(s // 50) * 50
                arr[n][h][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
