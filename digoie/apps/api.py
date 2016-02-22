

from digoie.core.http.stream.base import stream
from digoie.core.extractor import reverb
from digoie.core.ml.dataset import feature
from digoie.core.ml.dataset.labeling import labeling


def extract():
    """ extract useful information
    
    based on the data from elastic search, extract useful information like person's
    description, behavior and relationship
    """

    # load data   
    """ 
    stream()
    data = reverb.extract()
    """

    dataset = reverb.load_data()
    # featured = feature.extract(dataset)
    labels = labeling(dataset)







    





