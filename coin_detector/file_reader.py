import os

import cv2

from coin_detector.coin_type import CoinType
from coin_detector.coin import Coin


class FileReader:

    @staticmethod
    def get_sample_images(coin_type: CoinType) -> [Coin]:
        path = os.getcwd() + '/coin_detector/' + FileReader.get_samples_path(coin_type)
        images = [Coin(cv2.imread(os.path.join(path, image_name)), coin_type) for image_name in os.listdir(path)]
        return imagesf

    @staticmethod
    def get_samples_path(coin_type: CoinType):
        return f'samples_real/{coin_type.value}'
