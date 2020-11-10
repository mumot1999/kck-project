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



    # code derived from watershed example of scikit-image
# http://scikit-image.org/docs/dev/auto_examples/plot_watershed.html

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

from skimage.morphology import watershed
from skimage.feature import peak_local_max
from skimage.color import rgb2gray
from skimage.io import imread

img = imread('flame.png')
image = rgb2gray(img) > 0.01

# Now we want to separate the two objects in image
# Generate the markers as local maxima of the distance to the background
distance = ndi.distance_transform_edt(image)

# get global maximum like described in
# http://stackoverflow.com/a/3584260/2156909
max_loc = unravel_index(distance.argmax(), distance.shape)

fig, axes = plt.subplots(ncols=4, figsize=(10, 2.7))
ax0, ax1, ax2, ax3 = axes

ax0.imshow(img,interpolation='nearest')
ax0.set_title('Image')
ax1.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax1.set_title('Thresholded')
ax2.imshow(-distance, cmap=plt.cm.jet, interpolation='nearest')
ax2.set_title('Distances')
ax3.imshow(rgb2gray(img), cmap=plt.cm.gray, interpolation='nearest')
ax3.set_title('Detected centre')
ax3.scatter(max_loc[1], max_loc[0], color='red')

for ax in axes:
    ax.axis('off')

fig.subplots_adjust(hspace=0.01, wspace=0.01, top=1, bottom=0, left=0,
                    right=1)
plt.show()
