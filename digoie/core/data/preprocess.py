

import os
import re
from digoie.conf.storage import __ml_datasets_dir__

def preproc_data():

    """
    path = os.path.join(__ml_datasets_dir__, 'input')
    fh_input = open(path, 'rU')

    path = os.path.join(__ml_datasets_dir__, 'input_refined')
    fh_output = open(path, 'wb')
    
    for line in fh_input:
        # reg = re.compile("")
        # if reg.search(line):
        #     print link
        # line.replace('.', '')
        # line = re.sub('[\n]{2,}', '\n', line)
        
        # line = re.sub('[ ]{2,}', '\n', line)
        # line = re.sub(r'\t', '.', line)
        # line = line.replace('\n', '.')
        if line.strip():
            line = re.sub('[\t ]{2,}', '\t', line)
            line = re.sub('(^[\t ]+|^ *$)', '', line)
            line = re.sub('^ *$', '', line)            
            fh_output.write(line)

    fh_input.close()
    fh_output.close()
    # """
    # """
    import nltk
    path = os.path.join(__ml_datasets_dir__, 'input_refined')
    with open(path, 'r') as f:
        sample = f.read()
         
    sentences = nltk.sent_tokenize(sample)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    if nltk.__version__[0:2] == "2.":
        chunkedSentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)
    else:
        chunkedSentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

    # print list(sample)[10]
    print sentences[10]
    print tokenized_sentences[10]
    print tagged_sentences[10]
    path = os.path.join(__ml_datasets_dir__, 'nltk_output')
    fh_output = open(path, 'wb')
    fh_output.writelines(sentences)
    
    # print chunkedSentences[10]

    # """

def train_test_split(path=None, train_point=.2, random_seed=24):
    if not path:
        path = os.path.join(__ml_datasets_dir__, 'input')

    dataset = []
    with open(path, 'rU') as fp:
        for line in iter(fp.readline, ''):
            dataset.append(line)
    
    datasize = len(dataset)

    import random
    random.seed(random_seed)
    random.shuffle(dataset)
    split_point = int(datasize*train_point)

    path = os.path.join(__ml_datasets_dir__, 'train_data')
    train_data_fp = open(path, 'wb')
    train_data_fp.writelines(dataset[:split_point])

    path = os.path.join(__ml_datasets_dir__, 'test_data')
    test_data_fp = open(path, 'wb')
    test_data_fp.writelines(dataset[split_point:])





        

        





