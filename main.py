import ast_functions as ast
import ms_functions as ms

# run this to load the cleaned ast dataset
content = ast.load_cleaned_record()
a, b, c, d = ast.get_s_r_ratio(content)
print('s', a, c)
print('r', b, d)
# print("length of content:", len(content))
id_fname_dict = ast.import_id_fname_dict()
# mz, intensity = ms.load_ms_data('3514457', id_fname_dict)
# print(mz)
# print(len(mz))
# print()
# print(intensity)
# print(len(intensity))

# mz1, intensity1 = ms.load_ms_data('3514457')
# mz2, intensity2 = ms.load_ms_data('3536784')
# print(mz2)
# print(len(mz2))
# print()
# print(intensity2)
# print(len(intensity2))
# print(type(mz))
# print(type(intensity))

# ms.export_ms_data('3514457', mz, intensity)
ms.import_ms_data('3514457', id_fname_dict)

# # DANGER!!!
# i = 1
# for lab_id in id_fname_dict:
#     mz, intensity = ms.load_ms_data(lab_id, id_fname_dict)
#     ms.export_ms_data(lab_id, mz, intensity)
#     print(i)
#     i += 1
