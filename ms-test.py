from pyopenms import *
import os
import csv

# exp = MSExperiment()
# MzMLFile().load("18-01-01_Labo1_0AAADLZ_1_0101DS172207384_L4_1117_1.mzML", exp)

# spec = exp[0]
# mz, intensity = spec.get_peaks()

# print(mz)
# print(len(mz))
# print()
# print(intensity)
# print(len(intensity))

# os.chdir('/Users/ethanchan/AST-ML/ms-data/MS raw_2018/')
# file = '201710-201911generated_id_ast_export.csv'
# filenames = os.listdir()
# filenames.sort()
# print(filenames)
# print("Target file is: ", file)


def countDistinct():
    # Creates an empty hashset
    s = set()
    # Traverse the input array
    res = 0

    os.chdir('/Users/ethanchan/AST-ML/')
    file = 'cleaned_record.csv'
    # os.chdir('/Users/ethanchan/AST-ML/ms-data/REQ ID AST list/')
    # file = '201710-201911generated_id_ast_export.csv'
    print("Target file is: ", file)
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        for line in csv_reader:
            # If not present, then put it in
            # hashtable and increment result
            if (line['Lab ID'] not in s):
                s.add(line['Lab ID'])
                res += 1
    return res


print(countDistinct())
