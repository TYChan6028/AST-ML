import os


def load_ms_data(lab_id, id_fname_dict):
    from pyopenms import MSExperiment, MzMLFile
    tail = id_fname_dict[lab_id].split('-')[0]
    os.chdir(f'/Users/ethanchan/AST-ML/ms-data/MS raw_20{tail}/')
    filename = id_fname_dict[lab_id]
    exp = MSExperiment()
    MzMLFile().load(filename, exp)

    spec = exp[0]
    mz, intensity = spec.get_peaks()

    return mz, intensity


def export_ms_data(lab_id, mz, intensity):
    from numpy import savetxt, vstack
    os.chdir('/Users/ethanchan/AST-ML/cleaned_ms_data/')
    filename = lab_id + '.csv'
    # data = vstack((mz, intensity)).T
    savetxt(filename, vstack((mz, intensity)).T, delimiter=",", fmt='%10.0f')
    # print('export ms data done')


def import_ms_data(lab_id, id_fname_dict):
    from numpy import genfromtxt, shape
    os.chdir('/Users/ethanchan/AST-ML/cleaned_ms_data/')
    ms_data = genfromtxt(f'{lab_id}.csv', delimiter=',')
    print(type(ms_data))
    print(shape(ms_data))
    print(ms_data)
    print('import ms data done')

    return ms_data
