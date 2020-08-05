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


def export_all_ms_data(id_fname_dict):
    # i = 1
    for lab_id in id_fname_dict:
        mz, intensity = load_ms_data(lab_id, id_fname_dict)
        export_ms_data(lab_id, mz, intensity)
        # print(i)
        # i += 1
    print("Successfully exported all ms data!")


def import_ms_data(lab_id):
    from numpy import genfromtxt
    os.chdir('/Users/ethanchan/AST-ML/cleaned_ms_data/')
    ms_data = genfromtxt(f'{lab_id}.csv', delimiter=',', dtype=int)
    # print(type(ms_data))
    # print(shape(ms_data))
    # print(ms_data)
    # print(f'Successfully imported ms data from {lab_id}.csv!')

    return ms_data


def get_sparsed_peak(lab_id, bin=1, mz_min=2000, mz_max=20000):
    from numpy import zeros, array
    # from numpy import set_printoptions, inf
    # set_printoptions(threshold=inf)
    peaks = import_ms_data(lab_id)
    mz = set(peaks[:, 0])
    intensity = dict(zip(peaks[:, 0], peaks[:, 1]))
    new_mz = zeros((mz_max - mz_min + 1, 2), dtype=int)

    for i in range(mz_max - mz_min + 1):
        if i + mz_min in mz:
            new_mz[i, :] = array([i + mz_min, intensity[i + mz_min]])

    if bin != 1:
        new_mz = bin_sparsed_peaks(new_mz, bin=bin)

    return new_mz


def bin_sparsed_peaks(new_mz, bin=100, mz_min=2000):
    from numpy import zeros, array
    new_len = (len(new_mz) - 1) // bin
    binned_new_mz = zeros((new_len, 2), dtype=int)

    for i in range(new_len):
        binned_new_mz[i, :] = array([mz_min + i * bin, sum(new_mz[i * bin:i * bin + bin, 1])])

    return binned_new_mz
