import pandas as pd
import numpy as np
import datetime

from vectorize_text import vectorize_text
from nan_handler import nan_dropper, nan_filler


def wrangler_main(data,
                  y,
                  max_categories,
                  starts_with_col,
                  treshold,
                  first_fill_cols,
                  fill_with,
                  to_string,
                  vectorize):

    '''Wrangler Utility

    WHAT: The main function for data transformation.

    '''

    if max_categories == 'auto':
        max_categories = len(data) / 50
    elif max_categories == 'max':
        max_categories = len(data) + 1
    elif type(max_categories) == int:
        max_categories = max_categories

    # skipping columns with datetime type
    for col in data.columns:
        temp = isinstance(data[col][0], datetime.date)

        if temp is True:
            data = data.drop(col, axis=1)

    cols_before = data.shape[1]
    rows_before = len(data)

    temp_string = pd.DataFrame()

    if to_string is not None:

        if type(to_string) is str:
            to_string = [to_string]
        for col in to_string:
            if col in data.columns:
                temp_string[col] = data[col]
                temp_string[col] = temp_string[col].astype('str')

        data = data.drop(to_string, axis=1)

    if vectorize is not None:

        temp_vect = pd.DataFrame()

        if type(vectorize) is str:
            vectorize = [vectorize]

        if type(vectorize) is list:
            vect_len = len(vectorize)

            for i in range(vect_len):
                temp_list = []
                temp_list = vectorize_text(data[vectorize[i]])

                # transpose list of the vectors
                temp_list = list(np.transpose(temp_list))

                for j in range(len(temp_list)):
                    col = 'v'+str(i+1)+"_"+str(j+1)
                    temp_vect[col] = temp_list[j]

        data = data.drop(vectorize, axis=1)

        # temp_vect.columns = vectorize

    if first_fill_cols is not None:

        data[first_fill_cols] = nan_filler(data, first_fill_cols, fill_with)

    if treshold is not 0:

        data = nan_dropper(data, treshold)

    for col in data.columns:
        try:
            data[col].astype('float')

        except ValueError:

            if len(data[col].unique()) < max_categories:
                data[col] = pd.Categorical(data[col]).codes

            # initiates conversion to labels based on first character
            elif starts_with_col is not 'none' and starts_with_col == col:
                data[col] = _starts_with_output(data, col)

            else:
                data = data.drop(col, axis=1)

    if y is not 'none':
        temp_y = data[y]
        data = data.drop(y, axis=1)
        data.insert(0, y, temp_y)

    if vectorize is not None:
        data = data.merge(temp_vect, left_index=True, right_index=True)
    if to_string is not None:
        data = data.merge(temp_string, left_index=True, right_index=True)

    rows_after = len(data)
    cols_after = data.shape[1]

    if vectorize is not None:
        cols_after = data.shape[1] - 300 * vect_len

    print(str(rows_before - rows_after) + " out of " + str(rows_before) + " rows dropped")
    print(str(cols_before - cols_after) + " out of " + str(cols_before) + " columns dropped")

    return data


def _category_starts_with(data, col):

    '''
    This is called from starts_with_output.

    '''
    # filters out columns with long string values

    if data[col].str.len().mean() < 10:

        out = []
        c = len(data)

        for i in range(c):
            val = str(data[col][i])
            temp = []
            temp += val
            out += temp[0]

        return pd.DataFrame(pd.Series(out).unique()).reset_index()


def _starts_with_output(data, col):

    '''

    Helper function for to_integers in cases where
    the feature is categorized based on a common
    first character of a string.

    '''

    data[col] = data[col].fillna('0')
    temp_df = _category_starts_with(data, col)
    temp_df['start_char'] = temp_df[0]
    temp_df = temp_df.drop(0, axis=1)
    reference_df = temp_df.set_index('start_char').transpose()
    temp_list = []
    for i in range(len(data[col])):
        for c in temp_df['start_char']:
            if data[col][i].startswith(c) == True:
                temp_list.append(reference_df[c][0])
    if len(data[col]) != len(temp_list):
        print "AUTONOMIO ERROR: length of input and output do not match"
    else:
        return pd.Series(temp_list)
