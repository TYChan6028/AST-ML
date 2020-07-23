from pyopenms import *
import os

# exp = MSExperiment()
# MzMLFile().load("18-01-01_Labo1_0AAADLZ_1_0101DS172207384_L4_1117_1.mzML", exp)

# spec = exp[0]
# mz, intensity = spec.get_peaks()

# print(mz)
# print(len(mz))
# print()
# print(intensity)
# print(len(intensity))

os.chdir('/Users/ethanchan/AST-ML/ms-data/MS raw_2018/')
# file = '201710-201911generated_id_ast_export.csv'
filenames = os.listdir()
filenames.sort()
print(filenames)
# print("Target file is: ", file)
