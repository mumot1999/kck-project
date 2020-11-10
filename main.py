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
from skimage import measure
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
        sigma=5
    )
    edges = skimage.morphology.dilation(edges)
    coords = np.column_stack(np.nonzero(edges))

    model, inliers = measure.ransac(coords, measure.CircleModel,
                                    min_samples=3, residual_threshold=1,
                                    max_trials=1000)

    fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4),
                                    sharex=True, sharey=True)

    ax1.set_title('Original picture')
    ax1.scatter(model.params[1], model.params[0], s=25, c='red')
    ax1.imshow(image)

    ax2.set_title('Edge (white) and result (red)')
    ax2.imshow(edges)

    plt.show()
