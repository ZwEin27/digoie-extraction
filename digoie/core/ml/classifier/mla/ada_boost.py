
from sklearn.ensemble import AdaBoostClassifier


from digoie.core.ml.classifier.mla.base import MLAlgorithm


class MLAdaBoost(MLAlgorithm):

    # ML_NAME = K_NEIGHBORS

    def __init__(self, training_dataset, training_label):
        self.classifier = AdaBoostClassifier()
        super(MLAdaBoost, self).__init__(self.classifier, training_dataset, training_label)

    def generate(self):
        
        super(MLAdaBoost, self).generate()
        # print 'model for (' + self.ML_NAME + ') has been generated'
        # save_model(self.ML_NAME, classifier)
        return self.classifier

        






