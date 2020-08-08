import os
import pdb
import pandas as pd
import numpy as np
import ast_functions as ast

# sensitivity: accuracy for R-type samples
# specificity: accuracy for S-type samples
# accuracy: accuracy for the above combined


def naive_classifier(sorted_peak, s_ct, r_ct):
    sample_ct = s_ct + r_ct
    # best_sens = 0
    # best_spec = 0
    # best_acc = 0
    # alpha_idx = 0
    best = {'sensitivity': 0, 'specificity': 0, 'accuracy': 0, 'alpha': 0, 'orientation': 0}
    for sep_idx in range(1, sample_ct):
        # cand_list = []
        local_best = {'sensitivity': [0, 0], 'specificity': [0, 0], 'accuracy': [0, 0]}
        # S below alpha, R above alpha
        s_real = sum(sorted_peak['result'][0:sep_idx])
        s_pred = sep_idx
        r_real = r_ct - (s_pred - s_real)
        r_pred = sample_ct - sep_idx
        # sensitivity = round(r_real / r_pred * 100, 2)
        # specificity = round(s_real / s_pred * 100, 2)
        # accuracy = round((r_real + s_real) / sample_ct * 100, 2)
        # cand_list.append((sensitivity, specificity, accuracy))
        local_best['sensitivity'][0] = round(r_real / r_pred * 100, 2)
        local_best['specificity'][0] = round(s_real / s_pred * 100, 2)
        local_best['accuracy'][0] = round((r_real + s_real) / sample_ct * 100, 2)

        # R below alpha, S above alpha
        r_real = sep_idx - sum(sorted_peak['result'][0:sep_idx])
        r_pred = sep_idx
        s_real = s_ct - (r_pred - r_real)
        s_pred = sample_ct - sep_idx
        # sensitivity = round(r_real / r_pred * 100, 2)
        # specificity = round(s_real / s_pred * 100, 2)
        # accuracy = round((r_real + s_real) / sample_ct * 100, 2)
        # cand_list.append((sensitivity, specificity, accuracy))
        local_best['sensitivity'][1] = round(r_real / r_pred * 100, 2)
        local_best['specificity'][1] = round(s_real / s_pred * 100, 2)
        local_best['accuracy'][1] = round((r_real + s_real) / sample_ct * 100, 2)

        # decide if R bottom S top or vice versa
        # False: intensity below alpha = S; intensity above alpha = R
        # True: intensity below alpha = R; intensity above alpha = S
        o = (bool)(local_best['accuracy'][1] // local_best['accuracy'][0])

        # alpha_idx = alpha_idx * (bool)(best_acc // accuracy) + sep_idx * (bool)(accuracy // best_acc)
        # best_acc = best_acc * (bool)(best_acc // accuracy) + accuracy * (bool)(accuracy // best_acc)
        # if accuracy > best_acc:
        #     best_sens = sensitivity
        #     best_spec = specificity
        #     best_acc = accuracy
        #     alpha_idx = sep_idx
        if local_best['accuracy'][o] > best['accuracy']:
            best['sensitivity'] = local_best['sensitivity'][o]
            best['specificity'] = local_best['specificity'][o]
            best['accuracy'] = local_best['accuracy'][o]
            best['alpha'] = (sorted_peak['intensity'][sep_idx] - sorted_peak['intensity'][sep_idx - 1]) / 2
            best['orientation'] = o

        # print(sep_idx)
        # print(sensitivity, specificity, accuracy)
        # print(best_acc, alpha_idx)
        # print(best)

    return best


# set bin width
bin = 1

# read ms data from pandas dataframe
os.chdir('/Users/ethanchan/AST-ML/exported_data/')
df = pd.read_csv(f'pd_df_bin={bin}.csv')
# print(df.head())

s_id, r_id = ast.get_s_r_id()
s_ct = len(s_id)
r_ct = len(r_id)
# all_ct = s_ct + r_ct
all_ct = len(s_id) + len(r_id)
dtype = [('intensity', int), ('result', int)]
peaks = ['pk-' + f'{2000+i}' for i in range(0, 18001)]
result_df = pd.DataFrame(columns=['accuracy', 'sensitivity', 'specificity', 'alpha', 'orientation'], index=peaks)

# for each mz, convert pandas df to ndarray with intensity and ast result
for mz in range(2000, 20001):
    # dtype = [('intensity', int), ('result', int)]
    # sorted_peak = np.zeros((all_ct,), dtype=dtype)
    # sorted_peak['intensity'] = df.loc[f'pk-{mz}', :].to_numpy()
    # sorted_peak['result'] = np.concatenate((np.ones((s_ct,), dtype=int), np.zeros((r_ct,), dtype=int)), axis=None)
    # sorted_peak = np.sort(sorted_peak, order='intensity')

    sorted_peak = np.zeros((all_ct,), dtype=dtype)
    sorted_peak['intensity'] = df.loc[f'pk-{mz}', :].to_numpy()
    sorted_peak['result'] = np.concatenate((np.ones((len(s_id),), dtype=int), np.zeros((len(r_id),), dtype=int)), axis=None)
    new_sorted_peak = sorted_peak[np.nonzero(sorted_peak['intensity'])]
    new_sorted_peak = np.sort(new_sorted_peak, order='intensity')
    s_ct = np.count_nonzero(new_sorted_peak['result'])
    r_ct = new_sorted_peak.shape[0] - s_ct

# s_ct = 5
# r_ct = 5
# dtype = [('intensity', int), ('result', int)]
# values = [(0, 1), (0, 0), (2, 0), (3, 1), (5, 1), (7, 0), (10, 1), (12, 1), (15, 0), (20, 0)]
# sorted_peak = np.array(values, dtype=dtype)
# sorted_peak = np.sort(sorted_peak, order='intensity')
# print(sorted_peak)

# for mz in range(2000, 2011):
    # best = naive_classifier(sorted_peak, s_ct, r_ct)
    best = naive_classifier(new_sorted_peak, s_ct, r_ct)
    result_df.loc[f'pk-{mz}', :] = (best['accuracy'], best['sensitivity'], best['specificity'], best['alpha'], best['orientation'])
    # pdb.set_trace()
    # print(mz)

print('Exporting to csv...')
os.chdir('/Users/ethanchan/AST-ML/exported_data/')
# result_df.to_csv(f'best_acc_&_alphas.csv')
result_df.to_csv(f'best_acc_&_alphas_no_0.csv')
print('Done!')
