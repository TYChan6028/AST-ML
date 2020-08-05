import os
import pdb
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
import ast_functions as ast
import ms_functions as ms

# # display settings
# pd.set_option('display.max_columns', 2477)
# pd.set_option('display.max_rows', 18001)


def create_peaks_df(bin, s_id, r_id, peaks, sen, res):
    df = pd.DataFrame(columns=[*sen, *res], index=peaks)
    for i, lab_id in enumerate(s_id, start=1):
        df.loc[:, f'S-{i}'] = ms.get_sparsed_peak(lab_id, bin)[:, 1]
        # if i > 5:
        #     break
    for i, lab_id in enumerate(r_id, start=1):
        df.loc[:, f'R-{i}'] = ms.get_sparsed_peak(lab_id, bin)[:, 1]
        # if i > 5:
        #     break
    os.chdir('/Users/ethanchan/AST-ML/exported_data/')
    df.to_csv(f'pd_df_bin={bin}.csv')
    # after the csv file is created, remember to go into the file and maually delete the first comma


# set bin
bin = 10

# name features and samples
s_id, r_id = ast.get_s_r_id()
peaks = ['pk-' + f'{2000+i*bin}~{2000+i*bin+bin}' for i in range(18000 // bin)]
sen = ['S-' + str(i) for i in range(1, len(s_id) + 1)]
res = ['R-' + str(i) for i in range(1, len(r_id) + 1)]

# # create pandas dataframe to store data
# create_peaks_df(bin, s_id, r_id, peaks, sen, res)
# pdb.set_trace()

# read pre-created dataframe from file
os.chdir('/Users/ethanchan/AST-ML/exported_data/')
df = pd.read_csv(f'pd_df_bin={bin}.csv')
# print(df.head(10))
# print(df.loc[:, 'S-1'])
# print(df.loc['pk-2000~2100', :])

# scale and center data
scaled_df = preprocessing.StandardScaler().fit_transform(df.T)

# do PCA
pca = PCA()
pca.fit(scaled_df)
pca_data = pca.transform(scaled_df)

# draw scree plot
per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]
plt.bar(x=range(1, len(per_var) + 1), height=per_var)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()
# pdb.set_trace()

# draw fancy looking plot using PC1 and PC2
pca_df = pd.DataFrame(pca_data, index=[*sen, *res], columns=labels)
plt.scatter(pca_df.PC1, pca_df.PC2)
plt.title('My PCA Graph')
plt.xlabel('PC1 - {0}%'.format(per_var[0]))
plt.ylabel('PC2 - {0}%'.format(per_var[1]))

for sample in pca_df.index:
    plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))

plt.show()
# pdb.set_trace()

# get the name of the top 10 measurements (peaks) that contribute most to pc1
# get the loading scores
loading_scores = pd.Series(pca.components_[0], index=peaks)
# sort the loading scores based on their magnitude
sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)
# get the names of the top 10 peaks
top_10_genes = sorted_loading_scores[0:10].index.values
# print the peak names and their scores (and +/- sign)
print("Top 10 peaks that comtributed most to PC1:")
print(loading_scores[top_10_genes])
