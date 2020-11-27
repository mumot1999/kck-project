import cv2
import math
import os
import numpy as np
import coin_detector
#nazwy folderow z samplami
dirimg = ['1g', '2g', '5g', '10g', '20g', '50g', '1z', '2z', '5z']


def histogram(image_o, isDir=None):
    if isDir is not None:
        image = cv2.imread(image_o)  # image
        image = cv2.GaussianBlur(image, (5, 5), 0)
        image = cv2.Canny(image, 200 / 3, 200)
    else:
        image = cv2.GaussianBlur(image_o, (5, 5), 0)
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


def similarity(array1, array2):
    first = abs(array1[0] - array2[0])
    second = abs(array1[1] - array2[1])
    third = abs(array1[2] - array2[2])
    fourth = abs(array1[3] - array2[3])
    fifth = abs(array1[4] - array2[4])
    sixth = abs(array1[5] - array2[5])
    return (1 - math.sqrt((first ** 2 + second ** 2 + third ** 2 + fourth ** 2 + fifth ** 2 + sixth ** 2) / 6))


def run_main():
    detector = coin_detector.Detector()

    roi = cv2.imread('../resources/new/70.jpg')
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#wykrwyanie okręgów
    gray_blur = cv2.GaussianBlur(gray, (7, 7), 0)
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, dp=2.2, minDist=50, param1=200, param2=150, minRadius=60,
                               maxRadius=150)
    circles = np.uint16(np.around(circles))
    diameter = []
    coordinates = []
    histogram_array_names = []
    histogram_array = []
    first = 1;
    count = 0
    coins =0;
    if circles is not None:

        # convert coordinates and radii to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over coordinates and radii of the circles
        for (x, y, d) in circles:
            count += 1

            # add coordinates to list
            coordinates.append((x, y))

            # extract region of interest
            roi2 = roi[y - d:y + d, x - d:x + d]

            # cv2.imshow('Detected coins', roi2)
            # cv2.waitKey()

            coin = coin_detector.Coin(roi2, None)
            value = detector.clf.predict([coin.histogram])

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(roi2, str(value[0]), (0, 20), font, 0.5, (0, 0, 0), 2,
                        cv2.LINE_AA)
            print('Coin nr:', coins, value[0])
            coins=coins+1
            # print(similar, '\n', similar_value)
            # cv2.imshow('Detected coins', roi2)
            # cv2.waitKey()

    # text = "Total value: " + str("%.2f" % round(change, 2)) + " turkish lira"
    # cv2.putText(roi, text, (0, 400), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('Detected coins', roi)
    cv2.waitKey()



if __name__ == "__main__":
    run_main()
