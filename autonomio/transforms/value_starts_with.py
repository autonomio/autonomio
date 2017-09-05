import pandas as pd


def value_starts_with(data, col):

    '''

    Helper function for to_integers in cases where
    the feature is categorized based on a common
    first character of a string.

    '''
    data[col] = data[col].astype(str)
    data[col] = data[col].fillna('0')
    temp_df = _category_starts_with(data, col)
    temp_df['start_char'] = temp_df[0]
    temp_df = temp_df.transpose().drop(0)
    temp_df.columns = temp_df.ix[0].values
    temp_df = temp_df

    temp_list = []

    for index_id in data.index.values:
        for c in temp_df:
            if data[col][index_id].startswith(c) is True:
                temp_list.append(temp_df[c][0])

    return temp_list


def _category_starts_with(data, col):

    '''First Letter Producer

    WHAT: Produces a list of first characters from a set of values.
    This is called from starts_with_output.

    '''
    out = []

    for i in data.index.values:
        val = str(data[col][i])
        temp = []
        temp += val
        out += temp[0]

    return pd.DataFrame(pd.Series(out).unique())
