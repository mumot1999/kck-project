import cv2

import coin_detector

if __name__ == "__main__":
    image = cv2.imread("resources/new/70.jpg")

    coins = coin_detector.CoinExtractor.extract_coins(image)

    detector = coin_detector.Detector()

    values = [detector.clf.predict([coin.histogram]) for coin in coins]
    print(values)


