from datetime import datetime

import cv2
import numpy as np
import coin_detector


class CoinExtractor:

    @staticmethod
    def extract_coins(image):

        # resize image while retaining aspect ratio
        d = 1024 / image.shape[1]
        dim = (1024, int(image.shape[0] * d))
        image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        # create a copy of the image to display results
        output = image.copy()

        # convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # improve contrast accounting for differences in lighting conditions:
        # create a CLAHE object to apply contrast limiting adaptive histogram equalization
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        gray = clahe.apply(gray)

        blurred = cv2.GaussianBlur(gray, (7, 7), 0)

        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=2.5, minDist=100,
                                   param1=200, param2=80, minRadius=35, maxRadius=120)

        count = 0
        coordinates = []

        images = []
        if circles is not None:
            # append radius to list of diameters (we don't bother to multiply by 2)


            # convert coordinates and radii to integers
            circles = np.round(circles[0, :]).astype("int")

            # loop over coordinates and radii of the circles
            for (x, y, d) in circles:
                count += 1

                # add coordinates to list
                coordinates.append((x, y))

                # extract region of interest
                roi = image[y - d:y + d, x - d:x + d]

                images.append(coin_detector.Coin(roi, None))

                # write masked coin to file
                if True:
                    m = np.zeros(roi.shape[:2], dtype="uint8")
                    w = int(roi.shape[1] / 2)
                    h = int(roi.shape[0] / 2)
                    cv2.circle(m, (w, h), d, (255), -1)
                    maskedCoin = cv2.bitwise_and(roi, roi, mask=m)

                    cv2.imshow(f"Coin{count}", maskedCoin);
                    # cv2.waitKey()

                    id = datetime.now().timestamp()
                    cv2.imwrite(f"extracted/coin{count}{id}.png", maskedCoin)

                cv2.circle(output, (x, y), d, (0, 255, 0), 2)
                # cv2.putText(output, material,
                #             (x - 40, y), cv2.FONT_HERSHEY_PLAIN,
                #             1.5, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

        # cv2.imshow("coins", output)
        # cv2.waitKey()

        return images

