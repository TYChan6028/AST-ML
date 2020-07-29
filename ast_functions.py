import os
import csv


def line_formatter(line):
    # delete useless columns
    del line['Isolate Number'], line['Patient Last Name'], line['Patient First Name']
    del line['Sex'], line['Patient Birthday'], line['Patient ID'], line['Patient Location']
    del line['Patient Admission Date'], line['Specimen Type'], line['Specimen Source'], line['Collection Date']
    del line['Claimed'], line['Bio Number'], line['Percent Probability'], line['ID Confidence']
    del line['Method'], line['Coded comments'], line['MIC']
    # reformat the testing date
    month, day, year = line['Testing Date'].split('/')
    month = month.zfill(2)
    day = day.zfill(2)
    year = year.split()[0]
    line['Testing Date'] = f'{year}-{month}-{day}'

    return line


def view_ast_record(head_only=True, lineNum=100):
    os.chdir('/Users/ethanchan/AST-ML/ms-data/REQ ID AST list/')
    file = '201710-201911generated_id_ast_export.csv'
    print("Target file is:", file)

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        iRow = 0

        for line in csv_reader:
            # head_only parameter
            if head_only:
                if iRow > lineNum - 1:
                    break
                else:
                    iRow += 1
            ###
            if line['Organism Code'] == 'MAU' and line['Drug Code'] == 'OX1':
                line = line_formatter(line)  # clean and reformat output
                print(line)


def load_ast_record(head_only=True, lineNum=100):
    # move to correct directory
    os.chdir('/Users/ethanchan/AST-ML/ms-data/REQ ID AST list/')
    file = '201710-201911generated_id_ast_export.csv'
    print("Target file is:", file)

    # read antimicrobial susceptibility test record
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        dict_list = []
        iRow = 0

        for line in csv_reader:
            # head_only parameter
            if head_only:
                if iRow > lineNum - 1:
                    break
                else:
                    iRow += 1
            ###
            if line['Organism Code'] == 'MAU' and line['Drug Code'] == 'OX1':
                line = line_formatter(line)  # clean and reformat output
                dict_list.append(line)

    return dict_list


def export_ast_record(head_only=False, lineNum=100):
    # move to correct directory
    os.chdir('/Users/ethanchan/AST-ML/ms-data/REQ ID AST list/')
    file = '201710-201911generated_id_ast_export.csv'
    print("Target file is:", file)

    # read original antimicrobial susceptibility test record
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        iRow = 0

        # clean original test record and write to new test record
        os.chdir('/Users/ethanchan/AST-ML/')
        with open('cleaned_record.csv', 'w') as new_file:
            fieldnames = ['Lab ID', 'Testing Date', 'Organism Name', 'Organism Code', 'Drug Code', 'Drug Name', 'Result']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
            csv_writer.writeheader()

            for line in csv_reader:
                # head_only parameter
                if head_only:
                    if iRow > lineNum - 1:
                        break
                    else:
                        iRow += 1
                ###
                if line['Organism Code'] == 'MAU' and line['Drug Code'] == 'OX1':
                    line = line_formatter(line)  # clean and reformat output
                    csv_writer.writerow(line)


def find_repeated_id(dict_list):
    # Creates an empty hashset
    distinct_s = set()
    repeated_s = set()
    # Traverse the input array
    ct = 0

    for line in dict_list:
        # If not present, then put it in hashtable and increment result
        if (line['Lab ID'] not in distinct_s):
            distinct_s.add(line['Lab ID'])
            ct += 1
        else:
            repeated_s.add(line['Lab ID'])

    return repeated_s


def get_repeated_id_pos(dict_list, repeated_s):
    rep_id_pos_dict = {}
    for lab_id in repeated_s:
        rep_pos = []
        for i, line in enumerate(dict_list):
            if line['Lab ID'] == lab_id:
                rep_pos.append(i)
        rep_id_pos_dict[lab_id] = rep_pos

    return rep_id_pos_dict


def filter_bad_entries(dict_list, rep_id_pos_dict):
    # check S R result of repeated entries
    remove_list = set()

    for lab_id in rep_id_pos_dict:
        result = set()
        for pos in rep_id_pos_dict[lab_id]:
            result.add(dict_list[pos]['Result'])
            remove_list.add(pos)
            # print("added", pos)
        # print(remove_list)

        # if len(result) == 1:  # results are all S or all R
        #     # keep last entry
        #     remove_list.remove(rep_id_pos_dict[lab_id][-1])
        #     print("removed", rep_id_pos_dict[lab_id][-1])
        #     print(remove_list)
        # else:  # results contain S and R
        #     print("conflicted results")

    for i, line in reversed(list(enumerate(dict_list))):
        if i in remove_list:
            dict_list.pop(i)

    return dict_list


def match_id_w_filename(dict_list):
    valid_id = set()
    for line in dict_list:
        valid_id.add(line['Lab ID'])

    dir_list = [
        '/Users/ethanchan/AST-ML/ms-data/MS raw_2018/',
        '/Users/ethanchan/AST-ML/ms-data/MS raw_2019/'
    ]

    id_name_dict = {}
    for path in dir_list:
        os.chdir(path)
        filenames = os.listdir()
        filenames.sort()
        for file in filenames:
            lab_id = file.split('_')[2]
            if lab_id in valid_id:
                if lab_id not in id_name_dict:
                    id_name_dict[lab_id] = file
                else:
                    del id_name_dict[lab_id]
                    valid_id.remove(lab_id)
                    # print(f'{lab_id} has more than one mzML file')

    for i, line in reversed(list(enumerate(dict_list))):
        if line['Lab ID'] not in id_name_dict:
            dict_list.pop(i)

    return id_name_dict, dict_list
