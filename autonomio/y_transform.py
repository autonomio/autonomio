import pandas as pd
from keras.utils import np_utils

def y_transform(Y,data,flatten):

    y = [data[Y]]

    if len(y) == 1:

        y = map(list, zip(*y))
    
    df_y = pd.DataFrame(y)

        # if user input 'int' then function will be "greater than value"
        # if user input 'float' then function will be IQR range 

    
    # deals with 'y' inputs for non-categorical model 
    if flatten == 'mean':
        df_y = pd.DataFrame(df_y[0] >= df_y[0].mean()).astype(int)
    elif flatten == 'median':    
        df_y = pd.DataFrame(df_y[0] >= df_y[0].median()).astype(int)
    elif type(flatten) == int:    
        df_y = pd.DataFrame(df_y[0] >= quantile).astype(int)
    elif type(flatten) == float:
        df_y = pd.DataFrame(df_y[0] >= df_y[0].quantile(flatten)).astype(int)
    
    # deals with 'y' input for categorical variable
    elif flatten == 'categorical':

        if type((y[1][0])) == unicode or type((y[1][0])) == str:

            df_y = pd.Categorical(pd.DataFrame(df_y)[0])
            df_y = pd.DataFrame(pd.Series(df_y).cat.codes)

        df_y = np_utils.to_categorical(df_y)
        df_y = pd.DataFrame(df_y)

    elif flatten == 'none':
        df_y = pd.DataFrame(df_y).astype(int)

    return df_y