from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr_img = np.array(img)
rows = len(arr_img)
columns = len(arr_img[1])

def set_clarity(size,number_column, number_row):
    gray_tier = 0
    for n in range(number_row, number_row + size):
        for h in range(number_column, number_column + size):
            r = arr_img[n][h][0]
            g = arr_img[n][h][1]
            b = arr_img[n][h][2]
            sum_rgb = int(r) + int(g) +int(b)
            gray_tier += sum_rgb/3
    return int(gray_tier // (size**2))

def set_grey_color(gray_tier, size, number_column, number_row, gradations):    
    for n in range(number_row, number_row + size):
        for h in range(number_column, number_column + size):
            arr_img[n][h][0] = int(gray_tier // gradations) * gradations
            arr_img[n][h][1] = int(gray_tier // gradations) * gradations
            arr_img[n][h][2] = int(gray_tier // gradations) * gradations

def create_mosaic(size, gradations):
    number_row = 0
    while number_row < rows :
        number_column = 0
        while number_column < columns :
            set_grey_color(set_clarity(size,number_column, number_row), size, number_column, number_row, gradations )
            number_column = number_column + size
        number_row = number_row + size

create_mosaic(2,10)
res = Image.fromarray(arr_img)
res.save('res.jpg')
