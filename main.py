import cv2

import coin_detector

if __name__ == "__main__":
    # image = cv2.imread("resources/new/image4.jpg")
    # image = cv2.imread("resources/new/image3.jpg")
    # image = cv2.imread("resources/new/893.png")
    # image = cv2.imread("resources/new/image2.jpg")
    # image = cv2.imread("resources/new/polskie_monety_obiegowe.jpg")
    # image = cv2.imread("resources/200.jpg")
    # image = cv2.imread("resources/406.jpg")
    image = cv2.imread("resources/52.jpg")
    # image = cv2.imread("resources/new/złoty-monety-połysku-pieniądze-pln-waluta-51413867.jpg")

    extractor = coin_detector.CoinExtractor(image)

    detector = coin_detector.Detector()
    # detector.learn()
    # detector.learn()
    print(detector.score)

    values = []

    def get_new_value():
        return detector.clf.predict([coin.coin.histogram])

    for coin in extractor.coins:
        values = detector.clf.predict([coin.coin.histogram])
        print(values)
        values.append(values[0])
        coin.print(extractor.output, values[0])

    cv2.imshow("RESULT", extractor.output)
    cv2.waitKey()

    print(values)
    print(sum(values))


