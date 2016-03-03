

import os
import re
from digoie.conf.storage import __elastic_search_dir__, __reverb_input_dir__, __ml_datasets_dir__, REVERB_INPUT_EXT
from digoie.core.files.names import load_names



PROPERTY_DES = 100
PROPERTY_REL = 200
PROPERTY_ACT = 300


def labeling(reverb_data):
    print 'generate labels...'
    # return label_name(reverb_data)
    # return label_phone_number(reverb_data)
    # cache_svo(reverb_data)
    # label_test(reverb_data)
    return label_test(reverb_data)

def test():
    path = os.path.join(__ml_datasets_dir__, 'svo_label')
    fdp = open(path, 'rU')
    label_list = []
    for f in fdp:
        label_list.append(int(f))
    # print label_list
    return label_list

    
def label_test(reverb_data):
    # path = os.path.join(__ml_datasets_dir__, 'train_label')     # two and young
    # fdp = open(path, 'wb')

    two = ['friend', 'two']
    young = ['young', 'cute', 'kid']
    description = ['hair', 'nose', 'beautiful', 'eye', 'face', 'ear', 'body']
    filters = description

    label_list = []

    for line in reverb_data:
        line = line[:-1]
        line = line.split('\t')
        
        rvd_arg1_val = str(line[15]).replace('.', '')
        # rvd_arg1_val = rvd_arg1_val.split(' ')

        rvd_rel_val = str(line[16]).replace('.', '')
        # rvd_rel_val = rvd_arg2_val.split(' ')

        rvd_arg2_val = str(line[17]).replace('.', '')
        # rvd_arg2_val = rvd_arg2_val.split(' ')
        
        """
        for item in filters: 
            if item in rvd_arg1_val or item in rvd_rel_val or item in rvd_arg2_val:
                tmp = line[15] + ' | ' + line[16] + ' | ' + line[17] + ' | ' + line[12]
                fdp.writelines(tmp + '\n')
        """
        label = 0
        for item in two: 
            if item in rvd_arg1_val or item in rvd_rel_val or item in rvd_arg2_val:
                tmp = line[12]
                # fdp.writelines(tmp + '\n')
                label = 1
                break

        for item in young: 
            if item in rvd_arg1_val or item in rvd_rel_val or item in rvd_arg2_val:
                tmp = line[12]
                # fdp.writelines(tmp + '\n')
                label = 2
                break

        for item in description: 
            if item in rvd_arg1_val or item in rvd_rel_val or item in rvd_arg2_val:
                tmp = line[12]
                # fdp.writelines(tmp + '\n')
                label = 3
                break
        label_list.append(label)

    return label_list



    

def cache_svo(raw):
    path = os.path.join(__ml_datasets_dir__, 'svo')
    fdp = open(path, 'wb')
    for line in raw:
        line = line[:-1]
        line = line.split('\t')
        tmp = line[15] + ' | ' + line[16] + ' | ' + line[17] + ' | ' + line[12]
        fdp.writelines(tmp + '\n')


def label_name(reverb_data):
    names = load_names()
    label_list = []

    for line in reverb_data:
        line = line[:-1]
        line = line.split('\t')
        rvd_arg1_val = str(line[15]).replace('.', '')
        rvd_arg1_val = rvd_arg1_val.split(' ')

        rvd_arg2_val = str(line[17]).replace('.', '')
        rvd_arg2_val = rvd_arg2_val.split(' ')
        label = 0
        for name in names:
            name = name.lower()
            if name in rvd_arg1_val or name in rvd_arg2_val:                
                label = 1
                break;
        label_list.append(label)
    return label_list

# def label_phone_number(reverb_data):
    



def has_phone_number(string):
    reg = re.compile("\d{3}[+-._=:,\s]*\d{3}[+-._=:,\s]*\d{4}")
    # reg = re.compile('(zero|one|two|three|four|five|six|seven|eight|nine|\d|.){9}')
    return 1 if re.search(reg, string) else 0




"""
def label_phone_number(reverb_data):
    path = __reverb_input_dir__
    filename_list = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.split('.')[-1] == REVERB_INPUT_EXT[1:]]
    for file_path in filename_list:
        tmp_file = open(file_path, 'rU')
        for line in tmp_file:
            
            reg = re.compile("[0-9]{9pattern, string}")
            if re.match(reg, line):
                print line
"""

# test = 'Daniela please call 818.430.2219 P.S. i dont check.'
# test = 'If you like Please ? ? ? ? two.one.three.s'

# test = '8.1.8.6.9.4.six.zero.four.eight.'

# print 1 if has_phone_number(test) else 0






