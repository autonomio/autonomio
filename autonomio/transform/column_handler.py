import pandas as pd

def column_mover(data, cols, position='first'):

    '''Column Mover

    WHAT: Moves a column/s first or last column location in a dataframe

    OPTIONS: Either 'first' or 'last', first is on by default.

    '''

    if type(cols) is str:
        cols = [cols]
    for col in cols:

        temp_col = data[col]
        temp_col = pd.DataFrame(temp_col)
        data = data.drop(col, axis=1)

        if position is 'first':
            data = pd.merge(temp_col, data, left_index=True, right_index=True)
        else:
            data = pd.merge(data, temp_col, left_index=True, right_index=True)

    return data
