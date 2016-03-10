
from sklearn.ensemble import RandomForestClassifier

from digoie.core.ml.classifier.mla.base import MLAlgorithm


class MLRandomForest(MLAlgorithm):

    # ML_NAME = RANDOM_FOREST

    def __init__(self, training_dataset, training_label):
        self.classifier = RandomForestClassifier()
        super(MLRandomForest, self).__init__(self.classifier, training_dataset, training_label)

    def generate(self):
        
        super(MLRandomForest, self).generate()
        # save_model(self.ML_NAME, classifier)
        return self.classifier

        






