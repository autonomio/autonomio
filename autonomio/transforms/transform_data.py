import warnings
import pandas as pd
import numpy as np

from .x_transform import x_transform
from .y_transform import y_transform

warnings.filterwarnings("ignore")


def transform_data(data,
                   flatten=False,
                   X=False,
                   Y=False):

    '''
    (to be used through model functions)

    INPUT:  A feature label, list of labels, or range of numbers.
            If you input a single feature with text, it will be
            automatically vectrozed.

    OUTOUT:

    '''
    if Y is False:
        if X is False:
            print("Not input nor output data was inserted")
        else:
            X = X_data(X, data)
            return X
    else:
        if X is False:
            Y = Y_data(Y, data, flatten)
            return Y
        else:
            X = X_data(X, data)
            Y = Y_data(Y, data, flatten)
            return X, Y


def X_data(X, data):

    x = x_transform(X, data)
    x = pd.DataFrame(x)

    X = x.astype('float32')
    X = np.array(X)

    return X


def Y_data(Y, data, flatten):

    y = y_transform(Y, data, flatten)
    df_y = pd.DataFrame(y)

    Y = df_y.astype('float32')
    Y = np.array(Y)

    return Y
