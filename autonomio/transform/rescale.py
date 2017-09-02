import math
import numpy as np


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
