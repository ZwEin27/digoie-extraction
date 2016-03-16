
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.metrics import precision_recall_fscore_support
from sklearn import cross_validation
import numpy as np

from digoie.conf.machine_learning import DECISION_TREE, RANDOM_FOREST, MACHINE_LEARNING_ALGORITHMS, K_NEIGHBORS, SVM_SVC, AdaBoost, Gaussian_Naive_Bayes
from digoie.core.ml.dataset.model import save_model
from digoie.core.ml.classifier.mla.decision_tree import MLDecisionTree
from digoie.core.ml.classifier.mla.random_forest import MLRandomForest
from digoie.core.ml.classifier.mla.knn import MLKNeighbors
from digoie.core.ml.classifier.mla.svc import MLSVC
from digoie.core.ml.classifier.mla.ada_boost import MLAdaBoost
from digoie.core.ml.classifier.mla.gaussian_nb import MLGaussianNaiveBayes
from sklearn.metrics import precision_recall_curve

def generate_multilabel_classifier(X, y, mla=None):
    from sklearn.multiclass import OneVsRestClassifier
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    from sklearn.metrics import average_precision_score
    from sklearn.cross_validation import train_test_split
    from sklearn.preprocessing import label_binarize

    random_state = np.random.RandomState(24)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=random_state)

    n_samples, n_features = X.shape
    n_classes = y.shape[1]

    # model = MLDecisionTree(X_train, y_train)
    model = MLSVC(X_train, y_train)
    
    clf = model.get_classifier()
    classif = OneVsRestClassifier(clf)
    # print y_train
    # y_score = classif.fit(X_train, y_train).decision_function(X_test)
    y_score = classif.fit(X_train, y_train).predict(X_test)
    save_model('OneVsRest', classif)



    # print 'y_score'
    # print y_score
    
    # Compute Precision-Recall and plot curve
    precision = dict()
    recall = dict()
    average_precision = dict()
    for i in range(n_classes):
        precision[i], recall[i], _ = precision_recall_curve(y_test[:, i],
                                                            y_score[:, i])
        average_precision[i] = average_precision_score(y_test[:, i], y_score[:, i])

    print 'precision'
    print precision
    print 'recall'
    print recall

    """
    # predict_label = list(classif.predict(X_test))
    # target_label = y_test
    # print X_test
    # print predict_label
    # print target_label
    # print classification_report(target_label, predict_label)
    
    # Plot Precision-Recall curve
    
    plt.clf()
    plt.plot(recall[0], precision[0], label='Precision-Recall curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title('Precision-Recall example: AUC={0:0.2f}'.format(average_precision[0]))
    plt.legend(loc="lower left")
    plt.show()
    
    # Compute micro-average ROC curve and ROC area
    precision["micro"], recall["micro"], _ = precision_recall_curve(y_test.ravel(),
        y_score.ravel())
    average_precision["micro"] = average_precision_score(y_test, y_score,
                                                         average="micro")

    # Plot Precision-Recall curve for each class
    plt.clf()
    plt.plot(recall["micro"], precision["micro"],
             label='micro-average Precision-recall curve (area = {0:0.2f})'
                   ''.format(average_precision["micro"]))
    for i in range(n_classes):
        plt.plot(recall[i], precision[i],
                 label='Precision-recall curve of class {0} (area = {1:0.2f})'
                       ''.format(i, average_precision[i]))

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Extension of Precision-Recall curve to multi-class')
    plt.legend(loc="lower right")
    plt.show()

    """

def launch_cross_validation(X, y, mla=None):
    n_samples, n_features = X.shape
    # n_classes = y.shape[1]

    # loop = cross_validation.LeaveOneOut(n_samples)
    loop = cross_validation.KFold(n_samples, n_folds=4)

    for train_index, test_index in loop:
        # print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        # print(X_train, X_test, y_train, y_test)
        generate_classifier(X_train, X_test, y_train, y_test)
        break





def generate_classifier(X_train, X_test, y_train, y_test, mla=None):
    # random_state = np.random.RandomState(35)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=random_state)


    if mla == None:
        for mla in MACHINE_LEARNING_ALGORITHMS:
            print 'train ' + mla + ' classifier'
            clf = train(X_train, y_train, mla)
            test(X_test, y_test, mla, clf)
    else:
        clf = train(X_train, y_train, mla)
        test(X_test, y_test, mla, clf)
    # return clf

def train(X_train, y_train, mla=DECISION_TREE):
    # print 'train classifier'

    if mla == DECISION_TREE:
        model = MLDecisionTree(X_train, y_train)
    elif mla == RANDOM_FOREST:
        model = MLRandomForest(X_train, y_train)
    elif mla == K_NEIGHBORS:
        model = MLKNeighbors(X_train, y_train)
    elif mla == SVM_SVC:
        model = MLSVC(X_train, y_train)
    elif mla == AdaBoost:
        model = MLAdaBoost(X_train, y_train)
    elif mla == Gaussian_Naive_Bayes:
        model = MLGaussianNaiveBayes(X_train, y_train)
    # elif mla == Linear_Discriminant_Analysis:
    #     model = MLLinearDiscriminantAnalysis(X_train, y_train)
    # elif mla == Quadratic_Discriminant_Analysis:
    #     model = MLQuadraticDiscriminantAnalysis(X_train, y_train)
    else:
        return None # test
    clf = model.generate()
    save_model(mla, clf)
    return clf # (model, clf) 

def test(X_test, y_test, mla, clf):
    predict_label = list(clf.predict(X_test))
    target_label = y_test

    import os
    from digoie.conf.storage import __ml_datasets_dir__
    from digoie.core.files.file import Xvec2file, yvec2file, features2file
    yvec2file(y_test, os.path.join(__ml_datasets_dir__, 'y_predict'))

    # precision, recall, _ = precision_recall_curve(target_label, predict_label)
    print precision_recall_fscore_support(target_label, predict_label)

    

    # """
    print '+--------------------------------------------------------+'
    print '|                   Classifier Report                    +'
    print '+--------------------------------------------------------+'
    print 'Classifier: ' + mla
    print classification_report(target_label, predict_label)
    print 'accuracy: ' + str(accuracy_score(target_label, predict_label))
    print '\n\n'
    # """








