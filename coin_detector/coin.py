import math

import cv2

from coin_detector.coin_type import CoinType


class Coin:

    def __init__(self, image, coin_type: CoinType):
        self.coin_type = coin_type
        self.image = image
        self.histogram = self.calculate_histogram()

    def calculate_histogram(self):
        image = cv2.GaussianBlur(self.image, (5, 5), 0)
        image = cv2.Canny(image, 200 / 3, 200)
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
        array = [first / pixel_count, second / pixel_count2, third / pixel_count, fourth / pixel_count,
                 fifth / pixel_count2, sixth / pixel_count]
        return array


