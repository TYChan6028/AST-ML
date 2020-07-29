import ast_functions as ast
# import ms_test as test


# run this to load the cleaned ast dataset
content = ast.load_cleaned_record()
print("length of content:", len(content))
id_name_dict, content = ast.match_id_w_filename(content)
ast.load_ms_data('3585071', id_name_dict)
