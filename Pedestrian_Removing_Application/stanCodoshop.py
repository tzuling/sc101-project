"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = pow(pow(red - pixel.red, 2) + pow(green - pixel.green, 2) + pow(blue - pixel.blue, 2), .5)

    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_pixel = 0       # total of red pixel in list
    green_pixel = 0     # total of green pixel in list
    blue_pixel = 0      # total of blue pixel in list

    for pixel in pixels:
        red_pixel += pixel.red
        green_pixel += pixel.green
        blue_pixel += pixel.blue

    return [int(red_pixel/len(pixels)), int(green_pixel / len(pixels)), int(blue_pixel / len(pixels))]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    red_avg = get_average(pixels)[0]
    green_avg = get_average(pixels)[1]
    blue_avg = get_average(pixels)[2]
    dic = {}    # key: pixel, value: pixel_dist

    for pixel in pixels:
        pixel_dist = get_pixel_dist(pixel, red_avg, green_avg, blue_avg)
        dic[pixel] = pixel_dist

    key_min = min(dic, key=(lambda k: dic[k]))
    return key_min


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    pixels = []     # 存入每張照片的 x, y 的 pixel 值

    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    for y in range(0, height):
        for x in range(0, width):
            for image in images:
                pixels.append(image.get_pixel(x, y))

            best_pixel = get_best_pixel(pixels)
            result.set_pixel(x, y, best_pixel)
            pixels.clear()

    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
