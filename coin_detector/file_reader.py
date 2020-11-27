from coin_detector.coin_type import Coin
from skimage.io import imread_collection


class FileReader:

    @staticmethod
    def get_samples_of(coin_type: Coin):
        return imread_collection(FileReader.get_samples_path(coin_type))

    @staticmethod
    def get_samples_path(coin_type: Coin):
        return f'samples/{coin_type.value}'
