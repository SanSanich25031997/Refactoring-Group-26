from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
for i in range(0, a -1,10):
    for j in range(0, a1 -1,10):
        s = 0
        for n in range(i, i + 10):
            for n0 in range(j, j + 10):
                n1 = arr[n][n0][0]
                n2 = arr[n][n0][1]
                n3 = arr[n][n0][2]
                M = int(n1) + int(n2) + int(n3)
                s += M/3
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
res = Image.fromarray(arr)
res.save('res5.jpg')

print('pilik pilik')
