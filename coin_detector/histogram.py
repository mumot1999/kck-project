import coin_detector


class Histogram:

    @classmethod
    def get_histograms_of_sample(cls, coin_type: coin_detector.CoinType):
        images = coin_detector.FileReader.get_sample_images(coin_type)




