from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
image_pixels = np.array(img)
height = len(image_pixels)
width = len(image_pixels[1])


def get_grayscale(i, j, mosaic_width, mosaic_height):
    grayscale = 0
    for row in range(i, i + mosaic_height):
        for column in range(j, j + mosaic_width):
            red = image_pixels[row][column][0]
            green = image_pixels[row][column][1]
            blue = image_pixels[row][column][2]
            rgb_total = int(red) + int(green) + int(blue)
            grayscale += rgb_total / 3
    return int(grayscale // (mosaic_width * mosaic_height))


def set_color(i, j, mosaic_width, mosaic_height, grayscale, gray_spread):
    for row in range(i, i + mosaic_height):
        for column in range(j, j + mosaic_width):
            for n in range(3):
                image_pixels[row][column][n] = int(grayscale // gray_spread) * gray_spread


def make_mosaic(mosaic_width, mosaic_height, gray_spread):
    i = 0
    while i < height - 1:
        j = 0
        while j < width - 1:
            set_color(i, j, mosaic_width, mosaic_height, get_grayscale(i, j, mosaic_width, mosaic_height), gray_spread)
            j = j + mosaic_width
        i = i + mosaic_height


sizes = input("Введите размеры мозайки (Ш, В): ").split(", ")
make_mosaic(int(sizes[0]), int(sizes[1]), int(input("Введите шаг градации серого: ")))
res = Image.fromarray(image_pixels)
res.save('res.jpg')
