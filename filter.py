from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img, dtype = np.int32)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 1:
    j = 0
    while j < a1 - 1:
        s = 0
        for n in range(i, i + 10):
            for n0 in range(j, j + 10):
                n1 = arr[n][n0][0]
                n2 = arr[n][n0][1]
                n3 = arr[n][n0][2]
                M = (n1 + n2 + n3) // 3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for n00 in range(j, j + 10):
                arr[n][n00][0] = int(s // 50) * 50
                arr[n][n00][1] = int(s // 50) * 50
                arr[n][n00][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr.astype(np.uint8))
res.save('res.jpg')
