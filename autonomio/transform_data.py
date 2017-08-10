import warnings
import pandas as pd
import numpy as np
from vectorize_text import vectorize_text
from x_transform import x_transform
from y_transform import y_transform

warnings.filterwarnings("ignore")

def transform_data( data,
                    flatten,
                    dims=False,
                    X=False,
                    Y=False):

    '''
    (to be used through model functions)

    INPUT:  A feature label, list of labels, or range of numbers. 
            If you input a single feature with text, it will be 
            automatically vectrozed. 

    OUTOUT: 

    '''  

    if dims == False:
        if type(X) != list:
            temp = []
            temp.append(X)

        dims = len(temp)

    if Y == False:
        if X == False:
            print("Not input nor output data was inserted")
        else:
            X = X_transform(X, data, dims)
            return X
    else:
        if X == False:
            Y = Y_transform(Y, data, flatten)
            return Y
        else:
            X = X_transform(X, data, dims)
            Y = Y_transform(Y, data, flatten)
            return X, Y

def X_transform(X, data, dims):

    x = x_transform(X,data)
    df_x = pd.DataFrame(x)

    X = df_x.astype('float32')
    X = np.array(X)
    X = X[:,0:dims]

    return X

def Y_transform(Y, data, flatten):

    y = y_transform(Y,data,flatten)
    df_y = pd.DataFrame(y)

    Y = df_y.astype('float32')
    Y = np.array(Y)

    return Y