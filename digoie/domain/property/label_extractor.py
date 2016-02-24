"""Extract Properties

Two steps to extract properties
1) get features
2) use predefined knowledge
"""
from digoie.core.ml.dataset import feature
from digoie.domain.property import unsupervised


def extract(rever_dataset):
    
    # load featured dataset
    fc_mask = feature.REVERB_OP_MASK_ARG1|feature.REVERB_OP_MASK_ARG2
    featured = feature.extract(rever_dataset, component_mask=fc_mask)

    features = unsupervised.extract(featured)
    # unsupervised.extract(featured)


