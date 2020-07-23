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
    print("Target file is: ", file)

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        iRow = 0

        for line in csv_reader:
            line = line_formatter(line)  # clean and reformat output
            # head_only parameter
            if head_only:
                if iRow > lineNum - 1:
                    break
                else:
                    iRow += 1
            ###
            print(line)


def export_ast_record(head_only=False, lineNum=100):
    # move to correct directory
    os.chdir('/Users/ethanchan/AST-ML/ms-data/REQ ID AST list/')
    file = '201710-201911generated_id_ast_export.csv'
    print("Target file is: ", file)

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
                if line['Organism Code'] == 'MAU' and line['Drug Code'] == 'OX1':
                    line = line_formatter(line)  # clean and reformat output
                    csv_writer.writerow(line)
                # head_only parameter
                if head_only:
                    if iRow > lineNum - 1:
                        break
                    else:
                        iRow += 1
                ###
