import pandas as pd


def df_merge(data1, data2, on_index=True, on_column=False):

    '''Dataframe Merger

    WHAT: Performs a pandas dataframe merge.

    HOW: df_merge(data1, data2)

    INPUT: two pandas dataframes

    OUTPUT: a single pandas datafame

    '''

    if on_index is True and on_column is False:
        data = pd.merge(data1, data2, left_index=True, right_index=True)

    else:
        data = pd.merge(data1, data2, left_on=on_column, right_on=on_column)

    return data
