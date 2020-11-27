import coin_detector


def test_get_path_of_sample_test():
    assert coin_detector.FileReader.get_samples_path(coin_detector.CoinType.GR_20) == "samples/20"
