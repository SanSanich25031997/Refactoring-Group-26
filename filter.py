from PIL import Image
import numpy as np
name=input()
img = Image.open(name)
arr = np.array(img)
lengthOfImg = len(arr)
WidthOfImg = len(arr[1])
areaSize = 2
stepSize = 5
def findAvgColor(i, j, areaSize):
    avgColor = 0
    for areaX in range(i, i + areaSize):
            for areaY in range(j, j + areaSize):
                color1 = arr[areaX][areaY][0]
                color2 = arr[areaX][areaY][1]
                color3 = arr[areaX][areaY][2]
                avgColor += color1/3 + color2/3 + color3/3
    return int(avgColor // (areaSize*areaSize))
i = 0
while i < lengthOfImg - 1:
    j = 0
    while j < WidthOfImg - 1:                   
        avgColor = findAvgColor(i, j, areaSize)
        for areaX in range(i, i + areaSize):
            for areaY in range(j, j + areaSize):
                arr[areaX][areaY][0] = int(avgColor // stepSize) * stepSize
                arr[areaX][areaY][1] = int(avgColor // stepSize) * stepSize
                arr[areaX][areaY][2] = int(avgColor // stepSize) * stepSize
        j = j + areaSize
    i = i + areaSize
res = Image.fromarray(arr)
res.save('new_'+name)
