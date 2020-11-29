import math

import cv2
import numpy as np

from coin_detector.coin_type import CoinType


class Coin:

    def __init__(self, image, coin_type: CoinType):
        self.coin_type = coin_type
        self.image_used_in_histogram = None
        self.debug_images = []
        self.image = image
        # self.old_histogram = self.calculate_histogram_by_area()
        # self.color_histogram = self.calculate_color_histogram()
        self.histogram = self.calculate_histogram()

    def calculate_histogram(self):
        image = self.image
        image = cv2.GaussianBlur(image, (5,5), 0)
        image = cv2.Canny(image, 200 / 3, 50)
        height, width = image.shape[:2]

        self.debug_images.append(image.copy())

        # Desired "pixelated" size
        w, h = (5,5)

        # Resize input to "pixelated" size
        temp = cv2.resize(image, (w, h), interpolation=cv2.INTER_LANCZOS4)
        self.debug_images.append(temp.copy())

        # m = np.zeros(temp.shape[:2], dtype="uint32")
        #
        # for x in range(w):
        #     for y in range(h):
        #         m[x,y] = 600
        #         self.debug_images.append(m.copy())

        # Initialize output image
        output = cv2.resize(temp, (height, width), interpolation=cv2.INTER_LINEAR)

        # self.debug_images.append(temp)
        # self.debug_images.append(output)

        # self.image_used_in_histogram = temp

        result = (temp.flatten()).tolist()
        return result

    def calculate_histogram_by_area(self):
        image = cv2.GaussianBlur(self.image, (7,7), 0)
        image = cv2.Canny(image, 200 / 3, 50)
        self.image_used_in_histogram = image
        h = image.shape[0]
        w = image.shape[1]
        first = 0
        second = 0
        third = 0
        fourth = 0
        fifth = 0
        sixth = 0
        r = w / 2 + h / 2
        r = r / 2
        pixel_count = (w / 2) * (h / 2) - ((w * h) - (math.pi * ((r / 2) ** 2))) / 5
        pixel_count2 = (w * h) / 6
        for y in range(int(round(h / 2)), h):
            for x in range(0, int(round(w / 3))):
                if image[y, x] != 0:
                    third = third + 1
        for y in range(int(round(h / 2)), h):
            for x in range(int(round(w / 3)), int(round(2 * w / 3))):
                if image[y, x] != 0:
                    second = second + 1
        for y in range(0, int(round(h / 2))):
            for x in range(0, int(round(w / 3))):
                if image[y, x] != 0:
                    fourth = fourth + 1
        for y in range(int(round(h / 2)), h):
            for x in range(int(round(2 * w / 3)), w):
                if image[y, x] != 0:
                    first = first + 1
        for y in range(0, int(round(h / 2))):
            for x in range(int(round(w / 3)), int(round(2 * w / 3))):
                if image[y, x] != 0:
                    fifth = fifth + 1
        for y in range(0, int(round(h / 2))):
            for x in range(int(round(2 * w / 3)), w):
                if image[y, x] != 0:
                    sixth = sixth + 1

        color_histogram = [float(x) for x in self.calculate_color_histogram()]

        array = [first / pixel_count, second / pixel_count2, third / pixel_count, fourth / pixel_count,
                 fifth / pixel_count2, sixth / pixel_count]\
                # + color_histogram

        return array

    def calculate_color_histogram(self):
        # create mask
        img = self.image
        m = np.zeros(img.shape[:2], dtype="uint8")
        (w, h) = (int(img.shape[1] / 2), int(img.shape[0] / 2))
        cv2.circle(m, (w, h), 60, 255, -1)

        # calcHist expects a list of images, color channels, mask, bins, ranges
        h = cv2.calcHist([img], [0, 1, 2], m, [8,8,8], [0, 256, 0, 256, 0, 256])

        # return normalized "flattened" histogram
        return cv2.normalize(h, h).flatten()


