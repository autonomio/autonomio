import pandas as pd

import sys
sys.path.insert(0, '/Users/mikko/Documents/GitHub/core-module')

from autonomio.transform.col_name_generator import col_name_generator
from autonomio.transform.nan_imputer import nan_imputer
from autonomio.transform.onehot_encoding import onehot
from autonomio.transform.nan_handler import nan_filler

def all_is_binary(data,y):

    '''Sohot DataFrame One Hot Encoding

    DANGER ZONE!!! this is where things get strange...

    WHAT: A way to one hot encode an entire dataframe
    minus the outcome variable of course. Handles automatically
    nans, categorical labeling, etc. Yes, everything.

    HOW: sohot(titanic,'Survived')

    INPUT: A pandas dataframe.

    OUTPUT: A one hot encoded transformation of the dataframe.
    That's right, pure binary goodness...gonna make your machine so hot!

    '''

    ind_var = data[y]

    temp = pd.DataFrame()

    for col in data.columns:
        if col != y:
            # handle columns with no nans
            if data[col].isnull().sum() == 0:
                if data[col].dtype != 'O':
                    temp = _concat_df(data[col], temp)

            # handle columns with nans
            else:
                if data[col].dtype != 'O':
                    imputed = nan_imputer(data[col])
                    temp = _concat_df(imputed, temp)
                else:
                    filled = nan_filler(data,col,0)
                    labeled = pd.Categorical(filled).codes
                    temp = _concat_df(labeled, temp)

    temp = col_name_generator(temp)
    temp = temp.astype(int)
    temp = pd.concat([ind_var, temp],axis=1)

    return temp


def _concat_df(data, temp):

    oh = onehot(data)
    temp = pd.concat([temp, oh], axis=1)

    return temp
