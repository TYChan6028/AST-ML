# from pyopenms import *
import os
import csv
import ast_functions as ast

# exp = MSExperiment()
# filename = '18-01-01_Labo1_0AAADLZ_1_0101DS172207384_L4_1117_1.mzML'
# MzMLFile().load(filename, exp)

# spec = exp[0]
# mz, intensity = spec.get_peaks()

# print(mz)
# print(len(mz))
# print()
# print(intensity)
# print(len(intensity))

# os.chdir('/Users/ethanchan/AST-ML/ms-data/MS raw_2018/')
# filenames = os.listdir()
# filenames.sort()
# print(filenames[999].split('_'))
# print(len(filenames))


def get_filename_dict(distinct_s):
    os.chdir('/Users/ethanchan/AST-ML/ms-data/MS raw_2018/')
    filenames = os.listdir()
    filenames.sort()
    id_name_dict = {}
    for file in filenames:
        lab_id = file.split('_')[2]
        if lab_id in distinct_s:
            id_name_dict[lab_id] = [file]

    os.chdir('/Users/ethanchan/AST-ML/ms-data/MS raw_2019/')
    filenames = os.listdir()
    filenames.sort()
    for file in filenames:
        lab_id = file.split('_')[2]
        if lab_id in distinct_s:
            id_name_dict[lab_id] = [file]

    return id_name_dict


def count_distinct(dict_list):
    # Creates an empty hashset
    distinct_s = set()
    repeated_s = set()
    # Traverse the input array
    ct = 0

    for line in dict_list:
        # If not present, then put it in hashtable and increment result
        if (line['Lab ID'] not in distinct_s):
            distinct_s.add(line['Lab ID'])
            ct += 1
        else:
            repeated_s.add(line['Lab ID'])

    # print(len(repeated_s))
    return distinct_s


def get_repeated_id_pos(data, rep_data):
    new_dict = {}
    for lab_id in rep_data:
        rep_pos = []
        for i, line in enumerate(data):
            if line['Lab ID'] == lab_id:
                rep_pos.append(i)
        new_dict[lab_id] = rep_pos

    return new_dict


# data = ast.load_ast_record(head_only=False, lineNum=10000)
# dis_data = count_distinct(data)
# print(rep_data)
# print(get_repeated_id_pos(data, rep_data))
# print(len(new_dict))
# print(data[5359], data[5387])  # very strange case
# print(data[3202], data[3229])
# id_name_dict = get_filename_dict(dis_data)
# print(id_name_dict)
# print(len(id_name_dict))

# final_id = set()
# for lab_id in id_name_dict:
#     final_id.add(lab_id)

# R = 0
# S = 0
# for line in data:
#     if line['Lab ID'] in final_id:
#         if line['Result'] == 'S':
#             S += 1
#         else:
#             R += 1
# print("Num of S = ", S)
# print("Num of R = ", R)
