import numpy as np
import random

# filling the missing age values


def nan_imputer(data, impute_mode='mean_by_std'):

    '''NaN Imputer

    Provides five different options for imputing nan
    values within a a series / array of data.

    USE: nan_imputer(titanic.Age,'mean')

    OPTIONS: The default is 'mean_by_std', with other
    options 'mean', 'median', 'mode', and 'common'.

    '''

    l = []

    if impute_mode == 'mean':
        val = data.mean()

    if impute_mode == 'median':
        val = data.median()

    if impute_mode == 'mode':
        val = data.mode()

    if impute_mode == 'common':
        val = data.value_counts().index[0]

    if impute_mode == 'mean_by_std':
        val = data.mean()
        std = data.std()
        lo = val - std
        hi = val + std

    else:
        # create dummmy values for random pick
        lo = val
        hi = val

    c = len(data)

    for i in range(c):

        if np.isnan(data[i]) == True:

            l.append(random.randint(int(lo), int(hi)))

        else:
            l.append(data[i])

    return l
