import os
import csv

def export_ast_record():
    # move to correct directory
    os.chdir('/Users/ethanchan/AST-ML/ms-data/REQ ID AST list/')
    file = '201710-201911generated_id_ast_export.csv'
    print("Target file is: ", file)

    # open original antimicrobial susceptibility test record
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        i = 0

        # for row in csv_reader:
        #     if i > 1000:
        #         break
        #     else:
        #         print(row['Lab ID'])
        #         i += 1

        # clean original test record and write parsed test record
        os.chdir('/Users/ethanchan/AST-ML/')
        with open('parsed_record.csv', 'w') as new_file:
            fieldnames = ['Lab ID', 'Testing Date', 'Organism Name', 'Organism Code', 'Drug Code', 'Drug Name', 'Result']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
            csv_writer.writeheader()

            for line in csv_reader:
                if line['Organism Code'] == 'MAU' and line['Drug Code'] == 'OX1':
                    # delete useless columns
                    del line['Isolate Number'], line['Patient Last Name'], line['Patient First Name']
                    del line['Sex'], line['Patient Birthday'], line['Patient ID'], line['Patient Location']
                    del line['Patient Admission Date'], line['Specimen Type'], line['Specimen Source'], line['Collection Date']
                    del line['Claimed'], line['Bio Number'], line['Percent Probability'], line['ID Confidence']
                    del line['Method'], line['Coded comments'], line['MIC']
                    # reformat the testing date
                    month, day, year = line['Testing Date'].split('/')
                    year = year.split()[0]
                    line['Testing Date'] = f'{year}-{month}-{day}'
                    csv_writer.writerow(line)
                # if i > 100:
                #     break
                # else:
                #     i += 1
