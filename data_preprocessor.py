import ast_functions as ast

# load data from raw ast record
data = ast.load_ast_record(head_only=False, lineNum=50000)
print("length of raw data:", len(data))
# find repeated lab IDs (which means repeated pathogen samples) in the raw data
repeated_id = ast.find_repeated_id(data)
# get the position of these repeated entries in the raw data dict list
rep_id_pos_dict = ast.get_repeated_id_pos(data, repeated_id)
# remove the repeated entries and only keep entries whose lab ID has appeared once in the ast record
dis_data = ast.filter_bad_entries(data, rep_id_pos_dict)
print("length of distinct data:", len(dis_data))
# keep only the entries whose ast record and mass spectrometry profile are both valid
id_fname_dict, final_data = ast.match_id_w_filename(dis_data)
print("length of id-filename dict:", len(id_fname_dict))
print("length of final_data:", len(final_data))
# get the number and ratio of med-sensitive samples to med-resistant samples
s, r, s_per, r_per = ast.get_s_r_ratio(final_data)
print(f'S = {s} ({s_per}%)')
print(f'R = {r} ({r_per}%)')
# export the cleaned ast record to a new csv file
ast.export_ast_record(final_data, head_only=False)
# export the labID-filename dict to a new json file
ast.export_id_fname_dict(id_fname_dict)
