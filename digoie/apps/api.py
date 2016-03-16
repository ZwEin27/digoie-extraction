

from digoie.core.http.stream.base import stream
from digoie.core.extractor import reverb
from digoie.core.ml.dataset import feature
from digoie.core.ml.dataset.labeling import labeling
from digoie.domain.property import property_extractor
from digoie.core.extractor.reverb import load_data
from digoie.core.ml.dataset import feature
from digoie.core.ml.dataset import vector
import numpy as np



def demo():
    # reverb_data = reverb.extract()
    # reverb_data = load_data()
    import os
    from digoie.conf.storage import __ml_datasets_dir__
    from digoie.core.files.file import load_file2list
    from digoie.domain.property import label_generator
    from sklearn.multiclass import OneVsRestClassifier
    from digoie.core.data import preprocess
    from digoie.conf.storage import __ml_datasets_dir__
    from digoie.core.files.file import Xvec2file, yvec2file, features2file, list2file

    
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
    split_test_rate = .5

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



