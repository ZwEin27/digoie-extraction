



def load_multilabels(path=None):
    if not path:
        path = os.path.join(__ml_datasets_dir__, 'train_label')

    labels = []
    with open(path, 'rU') as fp:
        for line in iter(fp.readline, ''):
            label = line.split(',')
            labels.append(label)
    return labels

print load_multilabels()

