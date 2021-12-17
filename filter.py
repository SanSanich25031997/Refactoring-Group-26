from PIL import Image
import numpy as np

np.seterr(over='ignore')
arr_img = np.array(Image.open("img2.jpg"))
image_width, image_height = len(arr_img), len(arr_img[1])
mosaic_size, grey_step = 2, 80
pos_x = 0

while pos_x < image_width:
    pos_y = 0
    while pos_y < image_height:
        s = 0
        for x in range(pos_x, pos_x + mosaic_size):
            for y in range(pos_y, pos_y + mosaic_size):
                s += arr_img[x][y][0] / 3 + arr_img[x][y][1] / 3 + arr_img[x][y][2] / 3
        s = int(s // mosaic_size ** 2)
        for x in range(pos_x, pos_x + mosaic_size):
            for y in range(pos_y, pos_y + mosaic_size):
                arr_img[x][y][0] = int(s // grey_step) * grey_step
                arr_img[x][y][1] = int(s // grey_step) * grey_step
                arr_img[x][y][2] = int(s // grey_step) * grey_step
        pos_y += mosaic_size
    pos_x += mosaic_size

res = Image.fromarray(arr_img)
res.save('res.jpg')
