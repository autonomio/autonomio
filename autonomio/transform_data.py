import warnings
import pandas as pd
import numpy as np
from vectorize_text import vectorize_text
from x_transform import x_transform
from y_transform import y_transform

warnings.filterwarnings("ignore")

def transform_data(X,Y,data,flatten,dims):

    '''
    (to be used through model functions)

    INPUT:  A feature label, list of labels, or range of numbers. 
            If you input a single feature with text, it will be 
            automatically vectrozed. 

    OUTOUT: 

    ''' 

    ## Vectorize text if X is text. 

    x = x_transform(X,data)
    df_x = pd.DataFrame(x)

    ## Prepare Y 

    y = y_transform(Y,data,flatten)
    df_y = pd.DataFrame(y)

    ## final formatting for the neural net

    X = df_x.astype('float32')
    Y = df_y.astype('float32')
    X = np.array(X)
    Y = np.array(Y)
    X = X[:,0:dims]
        
    return X, Y