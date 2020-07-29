import ast_functions as ast

# preprocess raw data
data = ast.load_ast_record(head_only=False, lineNum=50000)
print("length of raw data:", len(data))
repeated_id = ast.find_repeated_id(data)
rep_id_pos_dict = ast.get_repeated_id_pos(data, repeated_id)
dis_data = ast.filter_bad_entries(data, rep_id_pos_dict)
print("length of distinct data:", len(dis_data))
id_name_dict, final_data = ast.match_id_w_filename(dis_data)
print("length of id-filename dict:", len(id_name_dict))
print("length of final_data:", len(final_data))
s, r, s_per, r_per = ast.get_s_r_ratio(final_data)
print(f'S = {s} ({s_per}%)')
print(f'R = {r} ({r_per}%)')
ast.export_ast_record(final_data, head_only=False)
