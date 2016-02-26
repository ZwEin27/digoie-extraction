"""Extract Properties

Two steps to extract properties
1) get properties
2) use predefined knowledge to filter properties
"""
from digoie.core.ml.dataset import feature
from digoie.domain.property import unsupervised
from digoie.domain.property import property_filter

# test only
properties = ['cute', 'beauties', 'youthfull', 'cowgirl', 'money', 'half', 'encounter', 'mish', 'fingers', 'course', 'session', 'asian', 'bedroom', 'phone', 'nipples', 'perfect', 'style', 'apartment', 'adrienne', 'la', 'disappointed', 'dick', 'young', 'lot', 'better', 'lube', 'black', 'attractive', 'pretty', 'wet', 'adn', 'smile', 'cum', 'friendly', 'lacey', 'real', 'good', 'appointment', 'big', 'couple', 'kitty', 'early', 'balls', 'pop', 'kiss', 'hands', 'bit', 'password', 'lady', 'day', 'missionary', 'heaven', 'towel', 'like', 'skills', 'frustrated', 'chest', 'naked', 'miami', 'lingerie', 'thighs', 'positions', 'quick', 'soft', 'round', 'clothes', 'upper', 'right', 'roxy', 'appearance', 'energy', 'hard', 'lfk', 'sex', 'second', 'sure', 'girl', 'sexual', 'best', 'really', 'living', 'mood', 'clock', 'pictures', 'sadie', 'shaved', 'hayden', 'provider', 'anne', 'doggy', 'sweet', 'red', 'pants', 'ass', 'blow', 'omg', 'business', 'thong', 'attention', 'boobs', 'little', 'bj', 'standard', 'small', 'job', 'lips', 'sexy', 'super', 'boy', 'great', 'instant', 'visit', 'cock', 'favorite', 'experience', 'times', 'thing', 'gfe', 'doggie', 'sweat', 'smoke', 'menu', 'mouth', 'tongue', 'condom', 'massage', 'gena', 'load', 'control', 'ladies', 'extra', 'pussy', 'cg', 'number', 'private', 'bath', 'raquel', 'date', 'vip', 'erect', 'table', 'ring', 'total', 'bra', 'bathroom', 'service', 'area', 'decent', 'night', 'girls', 'long', 'start', 'wonderful', 'escort', 'scant', 'white', 'legs', 'amazing', 'climax', 'friend', 'location', 'shower', 'head', 'door', 'way', 'aubrey', 'hotel', 'body', 'fore', 'hj', 'photos', 'finished', 'butt', 'russian', 'ok', 'town', 'rcg', 'bbbj', 'room', 'hour', 'type', 'smooth', 'flip', 'bed', 'air', 'reviews', 'evening', 'hottie', 'fun', 'kissing', 'minutes', 'called', 'beautiful', 'veronica', 'clit', 'taylor', 'pleasure', 'ad', 'cbj', 'knees', 'awesome', 'dfk', 'eyes', 'gianna', 'throat', 'woman', 'mya', 'stomach', 'pics', 'dress', 'ivy', 'sensual', 'different', 'end', 'relaxing', 'turn', 'things', 'agency', 'tip', 'couch', 'tight', 'hot', 'contact', 'tits', 'holly', 'panties', 'nice', 'picture', 'play', 'oil', 'daty', 'petite', 'ella', 'bald', 'breasts', 'hand', 'donation', 'fruit', 'lax', 'kim', 'position', 'crysta', 'friends', 'break', 'short', 'natural', 'johnson', 'boys', 'light', 'floor', 'cover', 'face', 'person', 'edge', 'clean', 'time', 'fresh', 'oral', 'karina', 'wine']

def extract(rever_dataset):
    
    # """
    fc_mask = feature.REVERB_OP_MASK_ARG1|feature.REVERB_OP_MASK_ARG2
    featured = feature.extract(rever_dataset, component_mask=fc_mask)
    properties = unsupervised.extract(featured)
    # """
    # property_filter.filter(properties)


