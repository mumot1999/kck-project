from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

import coin_detector


class Detector:

    def __init__(self):
        self.clf = MLPClassifier(
            # solver="lbfgs",
            max_iter=10000
        )
        samples_list = [coin_detector.FileReader.get_sample_images(coin) for coin in coin_detector.CoinType]
        self.samples = [s for image in samples_list for s in image]
        self.score = self.learn()

    def learn(self):
        X = [coin.histogram for coin in self.samples]
        y = [coin.coin_type.value for coin in self.samples]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=1)

        self.clf.fit(X_train, y_train)
        return int(self.clf.score(X_test, y_test) * 100)


