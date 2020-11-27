import cv2

import coin_detector

if __name__ == "__main__":
    # image = cv2.imread("resources/new/image4.jpg")
    image = cv2.imread("resources/new/image3.jpg")
    # image = cv2.imread("resources/new/893.png")

    extractor = coin_detector.CoinExtractor(image)

    detector = coin_detector.Detector()
    print(detector.score)

    values = []

    for coin in extractor.coins:
        value = detector.clf.predict([coin.coin.histogram])
        print(value)
        values.append(value[0])
        coin.print(extractor.output, value[0])

    cv2.imshow("RESULT", extractor.output)
    cv2.waitKey()

    print(values)
    print(sum(values))


