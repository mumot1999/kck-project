import cv2

import coin_detector

def test_coin_extractor_893():
    image = cv2.imread("images/893.png")
    extractor = coin_detector.CoinExtractor(image)
    assert len(extractor.coins) == 10

def test_coin_extractor_170():
    image = cv2.imread("images/70.jpg")
    extractor = coin_detector.CoinExtractor(image)
    assert len(extractor.coins) == 6
