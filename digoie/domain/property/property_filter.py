

import enchant
import inflect

p = inflect.engine()

def filter(properties):
    result = {}
    for prop in properties:
        # print prop + ' in singular_noun: ' + str(p.singular_noun(prop))
        prop = check_property(prop)
        if prop:
            result.setdefault(prop, 0)
            result[prop] += 1
    print result.keys()


def check_property(prop):
    singular = p.singular_noun(prop)
    if singular: 
        prop = singular
    #     if prop_desc(prop):
    #         return True
    # else:
    #     if prop_desc(prop) or prop_action(prop) or prop_relation(prop):
    #         return True

    tmp = case_filter(prop)
    if tmp:
        return tmp

    # final check
    d = enchant.Dict("en_US")
    if d.check(prop):
        return prop
    return False

"""
def check_inside(prop, csets):
    for cs in csets:
        if not prop in cs:
            return False
    return True
"""

# def check_inside(prop, check_set, common_string):
#     if prop in check_set:
#         return common_string
#     return False




def case_filter(prop):
    look = ['head', 'hair', 'eye', 'nose', 'mouth', 'ear', 'leg', 'foot', 'face']
    young = ['kid', 'young', 'youth', 'teen', 'teenager', 'child', 'youthful', 'cute']
    twonm = ['friend', 'two']

    desc = {}
    desc.setdefault('look', look)
    desc.setdefault('young', young)
    desc.setdefault('twonm', twonm)

    for (k, v) in desc.items():
        # print prop
        # print v
        if prop in v:
            return k
        # for item in v:
        #     if item in prop:
        #         return k
    return False

print filter(['friend'])
