import pandas as pd


def y_transform(Y, data, flatten):

    '''Outcome Variable Transformer

    WHAT: Transforms the outcome variable to a format that
    is according with the prediction target

    OPTIONS: 'mean','median','mode',int (ge), string for
    interquartile range for binary conversion. 'cat_string'
    for converting strings in to categorical labels, and
    'cat_int' for doing the same with integer values.

    '''

    df_y = data[Y]

    # if user input 'int' then function will be "greater than value"
    # if user input 'float' then function will be IQR range

    # below is for case where prediction is true or false
    # but the y-feature is in different format (e.g continuous)

    if flatten == 'mean':
        df_y = pd.DataFrame(df_y >= df_y.mean())
    elif flatten == 'median':
        df_y = pd.DataFrame(df_y >= df_y.median())
    elif flatten == 'mode':
        df_y = pd.DataFrame(df_y >= df_y.mode()[0])
    elif type(flatten) == int:
        df_y = pd.DataFrame(df_y >= flatten)
    elif type(flatten) == float:
        df_y = pd.DataFrame(df_y >= df_y.quantile(flatten))

    # below is for case where the y-feature is converted in
    # to a categorical, either if it's a number or string.

    elif flatten == 'cat_string':
        df_y = pd.Categorical(df_y)
        df_y = pd.DataFrame(pd.Series(df_y).cat.codes)

    elif flatten == 'cat_numeric':
        df_y = pd.qcut(df_y, 5, duplicates='drop')
        df_y = pd.DataFrame(pd.Series(df_y).cat.codes)

    # for cases when y-feature is already in the format
    # where the prediction output will be.

    elif flatten == 'none':
        df_y = pd.DataFrame(df_y)

    return df_y
