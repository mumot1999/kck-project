import cv2
import skimage.io
from matplotlib import pyplot as plt
from skimage.draw import circle_perimeter
from skimage.viewer import ImageViewer

import skimage.feature
import skimage.transform
import skimage.filters
import skimage.morphology
import numpy as np
from skimage.viewer.plugins.base import Plugin

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
from skimage.viewer.widgets import Slider

if __name__ == '__main__':
    image = skimage.io.imread("resources/50.jpg")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = skimage.morphology.erosion(image)
    edges = skimage.morphology.erosion(edges)
    edges = cv2.cvtColor(edges, cv2.COLOR_BGR2GRAY)

    edges = skimage.feature.canny(
        gray_image,
        sigma=3,
        # low_threshold=10,
        # high_threshold=50
    )
    edges = skimage.filters.sobel(edges)
    edges = skimage.morphology.dilation(edges)
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))

    hough_radii = np.arange(100, 200, 5)
    hough_res = skimage.transform.hough_circle(edges, hough_radii)

    accums, cx, cy, radii = skimage.transform.hough_circle_peaks(hough_res, hough_radii, total_num_peaks=3)
    for center_y, center_x, radius in zip(cy, cx, radii):
        circy, circx = circle_perimeter(center_y, center_x, radius,
                                        shape=image.shape)
        image[circy, circx] = (220, 20, 20)

    # ax.imshow(edges)
    # plt.show()
    ax.imshow(image)
    plt.show()

    # # image = skimage.feature.canny(image, sigma=4)
    # # image = skimage.filters.sobel(image)
    # # image = skimage.feature.mor(image)
    # # image = skimage.filters.sobel(image)
    # image = skimage.morphology.erosion(image)
    # image = skimage.morphology.erosion(image)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image = skimage.feature.canny(image, sigma=3)
    # image = skimage.filters.sobel(image)
    # image = skimage.morphology.dilation(image)
    #
    #
    # viewer = ImageViewer(image)
    # viewer.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
