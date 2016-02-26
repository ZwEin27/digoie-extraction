
# from __future__ import print_function
from time import time
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
import re
# from digoie.core.ml.dataset import vector


def extract(featured):
    print 'extract properties...'
    
    # print featured[0]
    # vectorized, feature_names = vector.vectorize(featured, my_min_df=0.0005, my_max_df=0.5)
    # features = load_freq_features(featured)
    # test(featured)
    
    extract_top_words(featured)

def extract_top_words(featured, n_topics=10):
    topics = []
    n_topics = 75
    n_top_words = 10
    topics.extend(lauch_nmf(featured, n_topics=n_topics, n_top_words=n_top_words))
    # topics.extend(lauch_lda(featured, n_topics=n_topics))
    return combine_top_words(topics)

def combine_top_words(topics):
    words = {}
    for topic in topics:
        for word in topic:
            words.setdefault(str(word), 0)
            words[str(word)] += 1 # not used
    return words.keys()

def lauch_nmf(featured, n_topics=10, n_top_words=20):
    """ Non-Negative Matrix Factorization (NMF)
    """
    # Use tf-idf features for NMF.
    print "extracting tf-idf features for NMF..."
    tfidf_vectorizer = TfidfVectorizer(preprocessor=custom_preprocessor, max_df=0.95, min_df=2) # max_features=n_features, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(featured)

    # Fit the NMF model
    nmf = NMF(n_components=n_topics, random_state=1, alpha=.1, l1_ratio=.5, max_iter=200).fit(tfidf)

    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    print_top_words(nmf, tfidf_feature_names)
    return load_top_words(nmf, tfidf_feature_names, n_top_words)

def lauch_lda(featured, n_topics=10, n_top_words=20):
    """ Latent Dirichlet Allocation with online variational Bayes algorithm
    """
    # Use tf (raw term count) features for LDA.
    print "extracting tf features for LDA..."
    tf_vectorizer = CountVectorizer(preprocessor=custom_preprocessor, max_df=0.95, min_df=2) # max_features=n_features, stop_words='english')
    tf = tf_vectorizer.fit_transform(featured)
    lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=5,
                                    learning_method='online', learning_offset=50.,
                                    random_state=0)
    lda.fit(tf)

    tf_feature_names = tf_vectorizer.get_feature_names()
    print_top_words(lda, tf_feature_names)
    return load_top_words(lda, tf_feature_names, n_top_words)


def load_top_words(model, feature_names, n_top_words=5):
    result = []
    for topic_idx, topic in enumerate(model.components_):
        topic = [feature_names[i]
                for i in topic.argsort()[:-n_top_words - 1:-1]]
        result.append(topic)
    return result


def print_top_words(model, feature_names, n_top_words=5):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic #" + str(topic_idx) + ':'
        print " ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]])
    print ''

def custom_preprocessor(raw):
    raw_list = raw.split()
    reg = re.compile("\d+")
    result = [word for word in raw_list if not re.match(reg, word)]
    return ' '.join(result) 

"""
def load_freq_features(featured):

    vectorizer = TfidfVectorizer(preprocessor=custom_preprocessor, min_df=0.00005, max_df=0.5)
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
"""


"""
def custom_tokenizer(raw):
    raw_list = raw.split()
    result = []
    reg_tag = re.compile("^[oOpPsS]4(\w*|\w2\w*)$")
    tags = [word for word in raw_list if re.match(reg_tag, word)]
    reg_name = re.compile("^[a-zA-Z]+$")
    words = [word for word in raw_list if re.match(reg_name, word)]
    reg_others = re.compile("^([#]+|conf[0-9])$")
    others = [word for word in raw_list if re.match(reg_others, word)]
    result.extend(words)
    result.extend(tags)
    result.extend(others)
    return result
"""