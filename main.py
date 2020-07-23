import ast_functions as ast
import os
import csv

# ast.view_ast_record(lineNum=10)
# ast.export_ast_record()


def countDistinct():
    # Creates an empty hashset
    s = set()
    # Traverse the input array
    res = 0

    # os.chdir('/Users/ethanchan/AST-ML/')
    # file = 'cleaned_record.csv'
    os.chdir('/Users/ethanchan/AST-ML/ms-data/REQ ID AST list/')
    file = '201710-201911generated_id_ast_export.csv'
    print("Target file is: ", file)
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        for line in csv_reader:
            # If not present, then put it in
            # hashtable and increment result
            if (line['Lab ID'] not in s):
                s.add(line['Lab ID'])
                res += 1
    return res


print(countDistinct())
