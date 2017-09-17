import pandas as pd
import numpy as np

from autonomio.transforms.nan_handler import nan_filler
from autonomio.transforms.nan_imputer import nan_imputer
from autonomio.text.vectorize_text import vectorize_text


def max_category(data, max_categories):

    '''Max Category Configuration

    WHAT: helper function for setting the max_categories
    parameter for wrangler()

    OPTIONS: integer value for max number of categories
             'max' for allowing any number of categories
             'auto' for allowing 1/50 of total values as
                    max number of categories

    INPUT: a dataframe or an array/series/list and the option

    OUTPUT: an integer representing the maximum allowed number
    of categories.


    '''

    # takes

    if max_categories == 'auto':
        max_categories = len(data) / 50

    elif max_categories == 'max':
        max_categories = len(data) + 1

    elif type(max_categories) == int:
        max_categories = max_categories

    elif max_categories is None:
        max_categories = len(data) + 1

    return max_categories


def vectorize_string_cols(data, vectorize):

    temp_vectorized_cols = pd.DataFrame()

    if type(vectorize) is str:
        vectorize = [vectorize]

    no_of_cols = len(vectorize)

    for i in range(no_of_cols):

        temp_list = []
        temp_list = vectorize_text(data[vectorize[i]])

        # transpose list of the vectors
        temp_list = list(np.transpose(temp_list))

        for j in range(len(temp_list)):
            col = 'v'+str(i+1)+"_"+str(j+1)
            temp_vectorized_cols[col] = temp_list[j]

    return data, temp_vectorized_cols


def filling_nans(data, fill_columns, fill_with):

    if type(fill_columns) is str:
        fill_columns = [fill_columns]

    for col in fill_columns:
        data[col] = nan_filler(data, col, fill_with)

    return data


def imputing_nans(data, impute_columns, impute_mode):

    if type(impute_columns) is str:
        impute_columns = [impute_columns]

    for col in impute_columns:
        data[col] = nan_imputer(data[col], impute_mode)

    return data


def _category_starts_with(data, col):

    '''
    This is called from starts_with_output.

    '''
    # filters out columns with long string values

    if data[col].str.len().mean() < 10:

        out = []

        for i in data.index.values:
            val = str(data[col][i])
            temp = []
            temp += val
            out += temp[0]

    return pd.DataFrame(pd.Series(out).unique())


def starts_with_output(data, col):

    '''

    Helper function for to_integers in cases where
    the feature is categorized based on a common
    first character of a string.

    '''
    data[col] = data[col].fillna('0')
    temp_df = _category_starts_with(data, 'Cabin')
    temp_df['start_char'] = temp_df[0]
    temp_df = temp_df.transpose().drop(0)
    temp_df.columns = temp_df.ix[0].values
    temp_df = temp_df

    temp_list = []

    for index_id in data.index.values:
        for c in temp_df:
            if data[col][index_id].startswith(c) == True:
                temp_list.append(temp_df[c][0])

    return temp_list


def string_contains_to_binary(data, col_that_contains, col_contains_strings):

    '''Convert String to Binary

    WHAT: Deals with cases where string values are converted in to Binary based
    on a value contained in the string.

    '''

    temp_contains = pd.DataFrame()

    if type(col_that_contains) is str:
        col_that_contains = [col_that_contains]

    for col in col_that_contains:
        count = 0
        for string in col_contains_strings:
            temp_contains = pd.concat([temp_contains, data[col].str.contains(string)], axis=1)
            count += 1

        temp_contains.columns = col_contains_strings
        temp_contains = temp_contains.astype(float)

    return temp_contains
