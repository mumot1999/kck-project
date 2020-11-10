import cv2
import skimage.io
from matplotlib import pyplot as plt
from skimage import color, img_as_ubyte
from skimage.draw import circle_perimeter, ellipse_perimeter
from skimage.transform import hough_ellipse
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
        edges,
        sigma=5,
        # low_threshold=10,
        # high_threshold=50
    )
    # edges = skimage.filters.sobel(edges)
    edges = skimage.morphology.dilation(edges)
    # fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
    #
    # result = hough_ellipse(edges, accuracy=20, threshold=250,
    #                        min_size=100, max_size=120)
    # result.sort(order='accumulator')
    #
    # # Estimated parameters for the ellipse
    # best = list(result[-1])
    # yc, xc, a, b = [int(round(x)) for x in best[1:5]]
    # orientation = best[5]
    #
    # cy, cx = ellipse_perimeter(yc, xc, a, b, orientation)
    # image[cy, cx] = (0, 0, 255)
    #
    # edges = color.gray2rgb(img_as_ubyte(edges))
    # edges[cy, cx] = (250, 0, 0)

    fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4),
                                    sharex=True, sharey=True)

    ax1.set_title('Original picture')
    ax1.imshow(image)

    ax2.set_title('Edge (white) and result (red)')
    ax2.imshow(edges)

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
