from keras.layers import *
from keras.activations import *
from keras.optimizers import *
from autonomio._utils.shapes import *


def get_method(method_name):

    '''
    Utility function that helps calling methods/functions
    within Keras dynamically using strings.

    method = a string value with the method name

    mode = 'layers', 'activations', and 'optimizers'. Note
           that the method needs to be included within the
           selected mode.
    '''

    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)

    return method
