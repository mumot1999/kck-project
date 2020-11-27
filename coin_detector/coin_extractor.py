from datetime import datetime

import cv2
import numpy as np
import coin_detector


class CoinExtractor:

    class CoinContainer:
        def __init__(self, coin, coordinates):
            self.coin = coin
            self.coordinates = coordinates

        def print(self, output_image, text):
            x,y = self.coordinates
            cv2.putText(output_image, str(text),
                        (x - 40, y), cv2.FONT_HERSHEY_PLAIN,
                        1.5, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

    def __init__(self, image):

        # resize image while retaining aspect ratio
        d = 1024 / image.shape[1]
        dim = (1024, int(image.shape[0] * d))
        image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        # create a copy of the image to display results
        self.output = image.copy()

        # convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # improve contrast accounting for differences in lighting conditions:
        # create a CLAHE object to apply contrast limiting adaptive histogram equalization
        clahe = cv2.createCLAHE(clipLimit=2.0)
        gray = clahe.apply(gray)

        blurred = cv2.GaussianBlur(gray, (7, 7), 0)

        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=2.5, minDist=100,
                                   param1=200, param2=80, minRadius=35, maxRadius=120)

        count = 0
        self.coordinates = []
        self.coins = []
        if circles is not None:
            # append radius to list of diameters (we don't bother to multiply by 2)


            # convert coordinates and radii to integers
            circles = np.round(circles[0, :]).astype("int")

            # loop over coordinates and radii of the circles
            for (x, y, d) in circles:
                count += 1

                # add coordinates to list
                self.coordinates.append((x, y))

                # extract region of interest
                roi = image[y - d:y + d, x - d:x + d]

                coin = coin_detector.Coin(roi, None)
                if len(roi.flatten()):
                    self.coins.append(self.CoinContainer(
                        coin,
                        (x, y)
                    ))

                    # write masked coin to file
                    if True:
                        m = np.zeros(roi.shape[:2], dtype="uint8")
                        w = int(roi.shape[1] / 2)
                        h = int(roi.shape[0] / 2)
                        cv2.circle(m, (w, h), d, (255), -1)
                        maskedCoin = cv2.bitwise_and(roi, roi, mask=m)

                        # cv2.imshow(f"Coin{count}", np.concatenate((cv2.cvtColor(coin.image_used_in_histogram, cv2.COLOR_GRAY2BGR)
                        #                                            , roi), axis=1))
                        # cv2.waitKey()

                        id = datetime.now().timestamp()
                        if maskedCoin is not None:
                            cv2.imwrite(f"extracted/coin{count}{id}.png", maskedCoin)

                cv2.circle(self.output, (x, y), d, (0, 255, 0), 2)

        # cv2.imshow("coins", output)
        # cv2.waitKey()



