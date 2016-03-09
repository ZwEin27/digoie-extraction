# print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelBinarizer
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA



X, Y = make_multilabel_classification(n_classes=3, n_labels=1,
                                      allow_unlabeled=True,
                                      random_state=1)
from sklearn import tree

classif = OneVsRestClassifier(tree.DecisionTreeClassifier())
# classif = OneVsRestClassifier(SVC(kernel='linear'))
classif.fit(X, Y)
test = X[0]

# print classif.estimators_[1].predict(test)

zero_class = np.where(Y[:, 0])
one_class = np.where(Y[:, 1])
# print zero_class
# print one_class




print type(Y)
# print Y


a = [[1, 2, 3], [1, 2, 3]]
x = np.array(a)
print x

