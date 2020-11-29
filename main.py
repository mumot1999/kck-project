import cv2

import coin_detector

if __name__ == "__main__":
    # image = cv2.imread("resources/new/image4.jpg")
    # image = cv2.imread("resources/new/image3.jpg")
    image = cv2.imread("resources/new/893.png")
    # image = cv2.imread("resources/new/image2.jpg")

    extractor = coin_detector.CoinExtractor(image)

    detector = coin_detector.Detector()

    # for i, photo in enumerate(filter(lambda x: x.coin_type.value == 500, detector.samples)):
    #     cv2.imshow(str(i), photo.image)
    #     for id, debug_image in enumerate(photo.debug_images):
    #         cv2.imshow(f"{i}-{id}-debug", debug_image)

    print(detector.score)

    values = []

    for coin in extractor.coins:
        value = detector.clf.predict([coin.coin.histogram])
        print(value)
        values.append(value[0])
        coin.print(extractor.output, value[0])

    cv2.imshow("RESULT", extractor.output)

    print(values)
    print(sum(values))

    cv2.waitKey()
    input()


