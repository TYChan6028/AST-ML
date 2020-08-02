import ast_functions as ast
import ms_functions as ms

# run this to load the cleaned ast dataset
# content = ast.load_cleaned_record()
# print("length of content:", len(content))
# a, b, c, d = ast.get_s_r_ratio(content)
# print('s', a, c)
# print('r', b, d)

# id_fname_dict = ast.import_id_fname_dict()
# mz, intensity = ms.load_ms_data('3514457', id_fname_dict)
# print(mz)
# print(len(mz))
# print()
# print(intensity)
# print(len(intensity))

# ms.export_ms_data('3514457', mz, intensity)

s_id, r_id = ast.get_s_r_id()
for lab_id in s_id:
    sparse_peak = ms.get_sparsed_peak(lab_id)
