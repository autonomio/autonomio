import pandas as pd
from numpy import array
from keras.utils import to_categorical


def onehot(data):

    '''One Hot Encoding

    Transform a feature in to binary columns.
    '''

    data = data.astype(int)

    data = array(data)
    encoded = to_categorical(data)

    encoded = pd.DataFrame(encoded)

    return encoded
