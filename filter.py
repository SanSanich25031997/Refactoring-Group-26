from PIL import Image
import numpy as np


def check_image(image_names):
    if image_names[0] == "" or not '.' in image_names[0]:
        quit()
    if len(image_names) == 1:
        image_names.append("output.jpg")


def get_grayscale(i, j, size):
    grayscale = 0
    for row in range(i, i + size):
        for column in range(j, j + size):
            red = image_pixels[row][column][0]
            green = image_pixels[row][column][1]
            blue = image_pixels[row][column][2]
            rgb_total = int(red) + int(green) + int(blue)
            grayscale += rgb_total / 3
    return int(grayscale // (size ** 2))


def set_color(i, j, size, grayscale, gray_spread):
    for row in range(i, i + size):
        for column in range(j, j + size):
            for n in range(3):
                image_pixels[row][column][n] = int(grayscale // gray_spread) * gray_spread


def make_mosaic(size, gray_spread):
    i = 0
    while i < height - 1:
        j = 0
        while j < width - 1:
            set_color(i, j, size, get_grayscale(i, j, size), gray_spread)
            j = j + size
        i = i + size


names_input = input(
    "Введите название входного и выходного изображения, например, \"my_picture.jpg mosaic_picture.jpg\": ").split(
    ' ')
check_image(names_input)
img = Image.open(names_input[0])
image_pixels = np.array(img)
height = len(image_pixels)
width = len(image_pixels[1])
make_mosaic(int(input("Введите высоту ячейки мозайки: ")), int(input("Введите шаг градации серого: ")))
res = Image.fromarray(image_pixels)
res.save(names_input[1])
