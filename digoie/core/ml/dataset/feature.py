
import os
import re
import math
from digoie.conf.storage import __elastic_search_dir__, __reverb_input_dir__, __ml_datasets_dir__, REVERB_INPUT_EXT

from digoie.core.files.names import load_names
from digoie.conf.global_settings import TARGET_PERSON_NAME, TARGET_PHONE_NUMBER
from digoie.core.files.file import *



REVERB_OP_MASK_FILENAME = 1 << 1
REVERB_OP_MASK_SENTNO = 1 << 2
REVERB_OP_MASK_SENTENCE = 1 << 3
REVERB_OP_MASK_ARG1 = 1 << 4
REVERB_OP_MASK_REL = 1 << 5
REVERB_OP_MASK_ARG2 = 1 << 6
REVERB_OP_MASK_CONF = 1 << 7
REVERB_OP_MASK_POST = 1 << 8
REVERB_OP_MASK_CT = 1 << 9
REVERB_OP_MASK_DEFAULT = REVERB_OP_MASK_CONF|REVERB_OP_MASK_ARG1|REVERB_OP_MASK_REL|REVERB_OP_MASK_ARG2|REVERB_OP_MASK_POST|REVERB_OP_MASK_CT


def extract_spo(raw):
    print 'extract features...'


def extract(raw, target=TARGET_PERSON_NAME, component_mask=REVERB_OP_MASK_DEFAULT):
    print 'extract features...'
    featured = []
    for line in raw:
        line = preprocess_line(line)
        var_list = []

        # load basic info for reverb output line
        # print line
        if component_mask&REVERB_OP_MASK_CONF:
            confidence = load_confidence_symbol(line[11])
            var_list.append(confidence)

        if (component_mask&REVERB_OP_MASK_ARG1) or (component_mask&REVERB_OP_MASK_REL) or (component_mask&REVERB_OP_MASK_ARG2):
            rvd_arg1_val, rvd_rel_val, rvd_arg2_val = load_ar_vals(line, target=target)
            if component_mask&REVERB_OP_MASK_ARG1:
                var_list.append(rvd_arg1_val)
            if component_mask&REVERB_OP_MASK_REL:
                var_list.append(rvd_rel_val)
            if component_mask&REVERB_OP_MASK_ARG2:
                var_list.append(rvd_arg2_val)

        if (component_mask&REVERB_OP_MASK_POST) or (component_mask&REVERB_OP_MASK_CT):
            rvd_arg1_post_tags, rvd_arg1_ct_tags, rvd_rel_post_tags, rvd_rel_ct_tags, rvd_arg2_post_tags, rvd_arg2_ct_tags = preprocess_tags(line)
            if component_mask&REVERB_OP_MASK_POST:
                var_list.append(rvd_arg1_post_tags)
                var_list.append(rvd_rel_post_tags)
                var_list.append(rvd_arg2_post_tags)
            if component_mask&REVERB_OP_MASK_CT:
                var_list.append(rvd_arg1_ct_tags)
                var_list.append(rvd_rel_ct_tags)
                var_list.append(rvd_arg2_ct_tags)




        """
        var_list = [
                        confidence,
                        rvd_arg1_val,
                        rvd_rel_val,  
                        rvd_arg2_val, 
                        rvd_arg1_post_tags, 
                        rvd_arg1_ct_tags,
                        rvd_rel_post_tags, 
                        rvd_rel_ct_tags,
                        rvd_arg2_post_tags, 
                        rvd_arg2_ct_tags
                    ]
        """

        rv4fe_data = ' '.join(var_list)
        featured.append(rv4fe_data)


    # path = os.path.join(__ml_datasets_dir__, 'featured')
    # list2file(featured, path)

    return featured



def preprocess_line(line):
    line = line[:-1]
    line = line.split('\t')
    return line


def load_ar_vals(line, target=TARGET_PERSON_NAME):
    if target == TARGET_PERSON_NAME:
        return load_av4name(line)
    elif target == TARGET_PHONE_NUMBER:
        return load_av4phoneno(line)
    else:
        return load_av4default(line)

def load_av4default(line):
    rvd_arg1_val = str(line[15]).replace('.', '')
    rvd_rel_val  = str(line[16]).replace('.', '')
    rvd_arg2_val = str(line[17]).replace('.', '')
    return rvd_arg1_val, rvd_rel_val, rvd_arg2_val

def load_av4name(line):
    rvd_arg1_val = str(line[15]).replace('.', '')
    rvd_rel_val  = str(line[16]).replace('.', '')
    rvd_arg2_val = str(line[17]).replace('.', '')

    # filter features
    names = load_names()
    filter = FeatureFilter(names=names)
    rvd_arg1_val = filter.filtering(rvd_arg1_val)
    rvd_rel_val = filter.filtering(rvd_rel_val)
    rvd_arg2_val = filter.filtering(rvd_arg2_val)

    return rvd_arg1_val, rvd_rel_val, rvd_arg2_val

def load_av4phoneno(line):
    rvd_arg1_val = str(line[15]).replace('.', '')
    rvd_rel_val  = str(line[16]).replace('.', '')
    rvd_arg2_val = str(line[17]).replace('.', '')
    return rvd_arg1_val, rvd_rel_val, rvd_arg2_val
    

def preprocess_tags(line):
    rvd_post = str(line[13]).split(' ')
    rvd_ct = str(line[14]).split(' ')

    rvd_arg1_start_idx = int(line[5])
    rvd_arg1_end_idx = int(line[6])
    rvd_rel_start_idx = int(line[7])
    rvd_rel_end_idx = int(line[8])
    rvd_arg2_start_idx = int(line[9])
    rvd_arg2_end_idx = int(line[10])

    # load post and chunk tags
    rvd_arg1_post_tags = rvd_post[rvd_arg1_start_idx:rvd_arg1_end_idx]
    rvd_arg1_ct_tags = rvd_ct[rvd_arg1_start_idx:rvd_arg1_end_idx]

    rvd_rel_post_tags = rvd_post[rvd_rel_start_idx:rvd_rel_end_idx]
    rvd_rel_ct_tags = rvd_ct[rvd_rel_start_idx:rvd_rel_end_idx]

    rvd_arg2_post_tags = rvd_post[rvd_arg2_start_idx:rvd_arg2_end_idx]
    rvd_arg2_ct_tags = rvd_ct[rvd_arg2_start_idx:rvd_arg2_end_idx]

    # format chunk tags
    rvd_arg1_ct_tags = [tag.replace('-','2') for tag in rvd_arg1_ct_tags]
    rvd_rel_ct_tags = [tag.replace('-','2') for tag in rvd_rel_ct_tags]
    rvd_arg2_ct_tags = [tag.replace('-','2') for tag in rvd_arg2_ct_tags]


    # add prefix for tags
    prefix = 'S4'
    rvd_arg1_post_tags = [prefix + elt for elt in rvd_arg1_post_tags]
    rvd_arg1_ct_tags = [prefix + elt for elt in rvd_arg1_ct_tags]

    prefix = 'P4'
    rvd_rel_post_tags = [prefix + elt for elt in rvd_rel_post_tags]
    rvd_rel_ct_tags = [prefix + elt for elt in rvd_rel_ct_tags]

    prefix = 'O4'
    rvd_arg2_post_tags = [prefix + elt for elt in rvd_arg2_post_tags]
    rvd_arg2_ct_tags = [prefix + elt for elt in rvd_arg2_ct_tags]


    # transfer list into string
    rvd_arg1_post_tags = ' '.join(rvd_arg1_post_tags)
    rvd_arg1_ct_tags = ' '.join(rvd_arg1_ct_tags)

    rvd_rel_post_tags = ' '.join(rvd_rel_post_tags)
    rvd_rel_ct_tags = ' '.join(rvd_rel_ct_tags)

    rvd_arg2_post_tags = ' '.join(rvd_arg2_post_tags)
    rvd_arg2_ct_tags = ' '.join(rvd_arg2_ct_tags)

    return rvd_arg1_post_tags, rvd_arg1_ct_tags, rvd_rel_post_tags, rvd_rel_ct_tags, rvd_arg2_post_tags, rvd_arg2_ct_tags

    # remove names from feature
    # rvd_arg1_val = remove_names(rvd_arg1_val)
    # rvd_rel_val = remove_names(rvd_rel_val)
    # rvd_arg2_val = remove_names(rvd_arg2_val)

        
def load_confidence_symbol(conf):
    return 'conf' + str(conf)[2]
    # return 'conf' + str(math.floor(float(conf*10)))


class FeatureFilter():
    def __init__(self, names=None):
        self.names = names

    def filtering(self, sentence):
        result = []
        word_list = sentence.split(' ')
        for word in word_list:
            word = self.refine_word(word)
            if self.is_valid_word(word):
                result.append(word)
        return ' '.join(result)


    def refine_word(self, word):
        word = word.lower()
        return word

    def is_valid_word(self, word):
        
        # if self.is_contain_name(word):
        #     return False

        if len(word) < 2:
            return False

        reg = re.compile("^[a_zA_Z]{2,}$")
        if re.match(reg, word):
            return False
        return True


    def is_contain_name(self, word):
        if word in self.names:
            return True
        else:
            return False








"""
def remove_names(vals):
    result = []
    # load name
    path = os.path.join(__elastic_search_dir__, 'names')
    names_file = open(path, 'rU')
    names = list([name[:-1] for name in names_file])
    names_file.close()

    val_list = vals.split(' ')
    for val in val_list:
        if val.lower() not in names:
            result.append(val.lower())
    return ' '.join(result)
"""








