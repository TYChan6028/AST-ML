import ast_functions as ast

# run this to load the cleaned ast dataset
# content = ast.load_cleaned_record()
# print("length of content:", len(content))
id_fname_dict = ast.import_id_fname_dict()
mz, intensity = ast.load_ms_data('3514457', id_fname_dict)
# mz1, intensity1 = ast.load_ms_data('3514457')
# mz2, intensity2 = ast.load_ms_data('3536784')

# print(mz)
# print(len(mz))
# print()
# print(intensity)
# print(len(intensity))
# print(mz2)
# print(len(mz2))
# print()
# print(intensity2)
# print(len(intensity2))
# print(type(mz))
# print(type(intensity))

# for i, entry in enumerate(content):
#     mz, intensity = ast.load_ms_data(entry['Lab ID'])
#     print(i)
#     print(len(mz))

ast.export_ms_data(mz, intensity)
ast.import_ms_data('3514457', id_fname_dict)
# for i in range(len(mz1)):
#     print(mz1[i], intensity1[i])
# print()
# for i in range(len(mz2)):
#     print(mz2[i], intensity2[i])


def import_ms_data(lab_id, id_fname_dict):
    from numpy import genfromtxt, shape
    os.chdir('/Users/ethanchan/AST-ML/cleaned_ms_data/')
    # with open(id_fname_dict[lab_id], 'r') as csv_file:
    # with open('foo.csv', 'r') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')

    #     for line in csv_reader:
    #         print(type(line))
    #         print(line)
    ms_data = genfromtxt('foo.csv', delimiter=',')
    # print(type(ms_data))
    # print(shape(ms_data))
    # print(ms_data)
    print('import ms data done')
