from digoie.core.ml.dataset import feature
from digoie.core.ml.dataset import vector
from sklearn.feature_extraction.text import TfidfVectorizer

def extract(rever_dataset):
    fc_mask = feature.REVERB_OP_MASK_ARG1|feature.REVERB_OP_MASK_REL|feature.REVERB_OP_MASK_ARG2
    featured = feature.extract(rever_dataset, component_mask=fc_mask)
    # print featured[0]
    # vectorized, feature_names = vector.vectorize(featured, my_min_df=0.0005, my_max_df=0.5)

    vectorizer = TfidfVectorizer(min_df=0.00005, max_df=0.5)
    data = vectorizer.fit_transform(featured).toarray()
    feature_names = [x.encode('UTF8') for x in vectorizer.get_feature_names()]
    # dataset, feature_names = vectorizer_filter(dataset, feature_names)
    # feature_names = '\n'.join([name for name in feature_names])
    # print feature_names
    # print feature_names
    
    idf = list(vectorizer.idf_)
    # idf = '\n'.join([name for name in feature_names])
    
    from digoie.conf.storage import __ml_datasets_dir__
    from digoie.core.files.file import Xvec2file, yvec2file, features2file, list2file
    import os

    yvec2file(feature_names, os.path.join(__ml_datasets_dir__, 'fn_test'))
    yvec2file(idf, os.path.join(__ml_datasets_dir__, 'idf_test'))

    # Xvec2file(data, os.path.join(__ml_datasets_dir__, 'sl_test'))


    # print feature.REVERB_OP_MASK_SENTENCE