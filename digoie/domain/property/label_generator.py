
import os
from digoie.domain.property.human_trafficking import HT_LABELS
from digoie.conf.storage import __ml_datasets_dir__
import numpy as np


def ganerate_singlelabel(path=None):
    if not path:
        path = os.path.join(__ml_datasets_dir__, 'train_label')
    labels = []
    with open(path, 'r') as fp:
        for line in fp.readlines():
            line = line.strip('\n')
            line = line.split(',')
            idx = HT_LABELS.index(line[0])
            labels.append(idx)
    return np.array(labels)

def ganerate_multilabel(path=None):
    if not path:
        path = os.path.join(__ml_datasets_dir__, 'train_label')

    multilabel_size = len(HT_LABELS)
    multilabel = []

    with open(path, 'r') as fp:
        for line in fp.readlines():
            labels = [0]*multilabel_size
            line = line.strip('\n')
            line = line.split(',')
            for label in line:
                idx_found = HT_LABELS.index(label)
                labels[idx_found] = 1
            multilabel.append(labels)
    multilabel = np.array(multilabel)
    # with open(path, 'wb') as fp:
    #     path = os.path.join(__ml_datasets_dir__, 'train_label_binary')
    #     fp.writelines(multilabel)
    return multilabel



# print generate_multilabel()