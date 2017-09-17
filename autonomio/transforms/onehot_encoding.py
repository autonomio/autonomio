import pandas as pd
from numpy import array

from keras.utils import to_categorical


def onehot(data):

    '''One Hot Encoding

    WHAT: Transform a feature in to binary columns.

    HOW: onehot(df.col)

    INPUT: An array, series, or list

    OUTPUT: Multiple columns of binary values that
    represent the input values.

    '''

    if type(data) == list:
        data = pd.Series(data)

    data = data.astype(int)

    data = array(data)
    encoded = to_categorical(data)

    encoded = pd.DataFrame(encoded)

    return encoded
