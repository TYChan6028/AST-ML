import ast_functions as ast
# import ms_test as test


# run this to load the cleaned ast dataset
content = ast.load_cleaned_record()
print("length of content:", len(content))
id_fname_dict, content = ast.match_id_w_filename(content)
print("length of id_fname_dict:", len(id_fname_dict))
ast.load_ms_data('4228289', id_fname_dict)
# import json
# import os
# os.chdir('/Users/ethanchan/AST-ML/')
# with open('id_fname_dict.json', 'w') as f:
#     json.dump(id_fname_dict, f, indent=2)

# with open('id_fname_dict.json') as f:
#     new_dict = json.load(f)

# print(type(new_dict))
# print(len(new_dict))
