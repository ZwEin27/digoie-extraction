
from sklearn import tree


from digoie.core.ml.classifier.mla.base import MLAlgorithm


class MLDecisionTree(MLAlgorithm):

    # ML_NAME = DECISION_TREE

    def __init__(self, training_dataset, training_label):
        self.classifier = tree.DecisionTreeClassifier()
        super(MLDecisionTree, self).__init__(self.classifier, training_dataset, training_label)
        

    def generate(self):
        # classifier = tree.DecisionTreeClassifier()
        super(MLDecisionTree, self).generate()
        # print 'model for (' + self.ML_NAME + ') has been generated'
        # save_model(self.ML_NAME, classifier)
        return self.classifier

        






