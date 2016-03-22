import numpy as np
import os
from digoie.core.http.stream.base import stream
from digoie.core.extractor import reverb
from digoie.core.ml.dataset import feature
from digoie.core.ml.dataset.labeling import labeling
from digoie.domain.property import property_extractor
from digoie.core.extractor.reverb import load_data
from digoie.core.ml.dataset import feature
from digoie.core.ml.dataset import vector
from digoie.conf.storage import __ml_datasets_dir__
from digoie.core.files.file import load_file2list
from digoie.domain.property import label_generator
from sklearn.multiclass import OneVsRestClassifier
from digoie.core.data import preprocess
from digoie.core.files.file import Xvec2file, yvec2file, features2file, list2file


def ooc():
    from sklearn import svm
    from digoie.core.ml.classifier import predict

    # training
    path = os.path.join(__ml_datasets_dir__, 'group')
    reverb_data = load_file2list(path)
    # print reverb_data
    
    featured = feature.extract(reverb_data)
    vectorized, feature_names = vector.vectorize(featured, my_min_df=0, my_max_df=1)

    train_size_rate = int(.5*(len(vectorized)))

    X_train = vectorized[:train_size_rate]
    X_train_size = len(X_train)
    X_test = vectorized[train_size_rate:]
    X_test_size = len(X_test)
    
    # testing
    path = os.path.join(__ml_datasets_dir__, 'outlier')
    outlier = load_file2list(path)

    featured = feature.extract(outlier)
    vectorized, predict_feature_names = vector.vectorize(featured, my_min_df=0, my_max_df=1)

    X_outliers = predict.transfer_pre_vector(feature_names, predict_feature_names, vectorized) 
    X_outliers_size = len(X_outliers)


    clf = svm.OneClassSVM(nu=0.1, kernel="rbf")
    clf.fit(X_train)
    y_pred_train = clf.predict(X_train)
    y_pred_test = clf.predict(X_test)
    y_pred_outliers = clf.predict(X_outliers)
    n_error_train = y_pred_train[y_pred_train == -1].size
    n_error_test = y_pred_test[y_pred_test == -1].size
    n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size

    print "error train: %d/%d ; errors novel regular: %d/%d ; errors novel abnormal: %d/%d" % (n_error_train, X_train_size, n_error_test, X_test_size, n_error_outliers, X_outliers_size)



def demo():
    # reverb_data = reverb.extract()
    # reverb_data = load_data()
    
    

    
    # filename = 'train_data'
    # path = os.path.join(__ml_datasets_dir__, filename)
    # reverb_file = open(path)
    # reverb_data = []
    # for line in reverb_file:
    #     reverb_data.append(line)

    labeled_point = 1000

    path = os.path.join(__ml_datasets_dir__, 'train_data')
    reverb_data = load_file2list(path)
    reverb_data = reverb_data[:labeled_point]
    # preprocess.train_test_split(path=path, train_point=.8, random_seed=2, train_file_name='train_data_training', test_file_name='train_data_testing')

    path = os.path.join(__ml_datasets_dir__, 'train_label')
    # preprocess.train_test_split(path=path, train_point=.8, random_seed=2, train_file_name='train_label_training', test_file_name='train_label_testing')
    # labels = label_generator.ganerate_multilabel(path)
    labels = label_generator.ganerate_singlelabel(path)
    labels = labels[:labeled_point]
    # labels = [label[0] for label in labels]
    # print labels


    # classes test
    



    # train classifier
    split_seed = 59
    split_test_rate = .2

    X_train, X_test, y_train, y_test = preprocess.train_test_split_data(reverb_data, labels, test_size=split_test_rate, random_seed=split_seed)

    list2file(X_test, os.path.join(__ml_datasets_dir__, 'X_test'))
    yvec2file(y_test, os.path.join(__ml_datasets_dir__, 'y_test'))

    # """
    min_df = 0.0
    max_df = 1.0
    
    
    # labels = labeling(reverb_data)
    featured = feature.extract(reverb_data)
    vectorized, feature_names = vector.vectorize(featured, my_min_df=min_df, my_max_df=max_df)
    
    X = vectorized
    # print X
    y = labels
    # print y
    
    X_train, X_test, y_train, y_test = preprocess.train_test_split_data(X, y, test_size=split_test_rate, random_seed=split_seed)

    




    from digoie.core.ml.classifier.base import generate_classifier, generate_multilabel_classifier, launch_cross_validation
    
    """
    launch_cross_validation(X, y)
    """
    # X_train, X_test, y_train, y_test = X, 0, y, 0
    # """
    # from sklearn.cross_validation import train_test_split
    # random_state = np.random.RandomState(13)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.01, random_state=random_state)
    clf = generate_classifier(X_train, X_test, y_train, y_test)
    


    # """
    # clf = generate_classifier(X, y)
    # clf = generate_multilabel_classifier(X, y)
    # """

def extract_label():
    dataset = reverb.load_data()
    property_extractor.extract(dataset)

def extract():
    """ extract useful information
    
    based on the data from elastic search, extract useful information like person's
    description, behavior and relationship
    """

    # load data   
    # """ 
    # stream()
    data = reverb.extract()
    # """

    # dataset = reverb.load_data()
    # featured = feature.extract(dataset)
    # labels = labeling(dataset)
    # print labels

def test():
    # from digoie.core.ml.dataset.base import generate_dataset
    # from digoie.core.ml.classifier.base import generate_classifier

    # min_df = 0.0
    # max_df = 1.0
    # feature_names, X_train, X_test, y_train, y_test = generate_dataset(min_df, max_df)
    # clf = generate_classifier(X_train, X_test, y_train, y_test)
     
    from digoie.core.ml.classifier import predict
    # predict.predict4dir()
    predict.test()


    

def get_data():
    from digoie.conf.storage import __ml_datasets_dir__
    from digoie.core.files.file import Xvec2file, yvec2file, features2file, list2file
    import  random
    import os

    size_rd = len(reverb_data)
    random.seed(2)
    random.shuffle(reverb_data)
    gap = int(.0235*size_rd)

    train_data = reverb_data[:gap]
    test_data = reverb_data[gap:]
    print len(train_data)

    list2file(train_data, os.path.join(__ml_datasets_dir__, 'train_origin'))
    list2file(test_data, os.path.join(__ml_datasets_dir__, 'test_origin'))



