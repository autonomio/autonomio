import math
import numpy as np
import pandas as pd

from autonomio.transforms.dataframe import df_merge


def max_rescale(values, scale=1, to_int=False):

    '''MinMax Rescaler

    WHAT: rescales a set of values on to a fixed scale.

    HOW: max_rescale([10,6,2],1)

    INPUT: an array, list or Series

    OUTPUT: an array with rescaled values.

    '''

    multiplier = scale / np.array(values).max().astype(float)
    new_shape = np.array(values) * multiplier

    if to_int is True:

        l = []

        for value in new_shape:
            l.append(int(math.ceil(value)))

        return np.array(l)

    else:
        return new_shape


def mean_zero(data, retain=None):

    '''Zero Mean Scalering

    WHAT: normalize data in to scale of 1 where mean is 0
    and standard deviation is 1.

    HOW: mean_zero(df,'y_variable')

    INPUT: dataframe where y is identified with column label.

    OUTPUT: dataframe with normalized value

    '''

    # avoiding transformation of y, labels, etc
    if retain is not None:
        col_temp = pd.DataFrame(data[retain])
        data = data.drop(retain, axis=1)

    # storing the temp values
    data_mean = data.mean(axis=0)
    data_std = data.std(axis=0)

    # transforming the data
    data = data - data_mean
    data = data / data_std

    # putting retained cols as first columns
    if retain is not None:
        data = df_merge(col_temp, data)

    return data
