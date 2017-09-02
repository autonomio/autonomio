import pandas as pd
from autonomio.transform.wrangler_utils import max_category
from autonomio.transform.wrangler_utils import datetime_detector
from autonomio.transform.wrangler_utils import vectorize_string_cols
from autonomio.transform.wrangler_utils import filling_nans
from autonomio.transform.wrangler_utils import imputing_nans
from autonomio.transform.wrangler_utils import to_category_labels

from autonomio.transform.nan_handler import nan_dropper


def wrangler_main(data,
                  y,
                  max_categories,
                  datetime_mode,
                  to_string,
                  vectorize,
                  fill_columns,
                  fill_with,
                  impute_columns,
                  impute_mode,
                  nan_treshold,
                  starts_with_col,
                  col_that_contains,
                  col_contains_strings):

    '''Wrangler Utility

    WHAT: The main function for data transformation.

    '''

    # store the values for original shape
    rows_before = data.shape[0]
    cols_before = data.shape[1]

    # set the value for maximum category label per feature
    max_categories = max_category(data, max_categories)

    # keep 'y' for later
    if y is not None:
        temp_y_col = data[y]
        data = data.drop(y, axis=1)

    # deal with possible datetime columns
    data = datetime_detector(data, datetime_mode)

    # in case retain, keep the column for later and drop it
    if datetime_mode is 'retain':

        temp_datetime_col = data[data.datetime_col_name]
        temp_datetime_col = pd.DataFrame(temp_datetime_col)
        data = data.drop(data.datetime_col_name, axis=1)

    # in case of string label, keep the column for later
    if to_string is not None:
        temp_string_col = pd.DataFrame(data[to_string].astype('str'))

    if vectorize is not None:
        data, temp_vectorized_cols = vectorize_string_cols(data, vectorize)

    # taking care of nan filling and imputing
    if fill_columns is not None:
        data = filling_nans(data, fill_columns, fill_with)

    if impute_columns is not None:
        data = imputing_nans(data, impute_columns, impute_mode)

    # dropping columns with nans above the treshold
    if nan_treshold is not 0:
        data = nan_dropper(data, nan_treshold)

    # doing to categorical conversions
    if starts_with_col is not None or col_that_contains is not None:
        data = to_category_labels(data,
                                  max_categories,
                                  starts_with_col,
                                  col_that_contains,
                                  col_contains_strings)

    # inserting / merging the missing columns back
    if datetime_mode is 'retain':
        data = pd.merge(temp_datetime_col,
                        data,
                        left_index=True,
                        right_index=True)

    if vectorize is not None:
        data = pd.merge(data,
                        temp_vectorized_cols,
                        left_index=True,
                        right_index=True)

    if to_string is not None:
        data = pd.merge(temp_string_col,
                        data,
                        left_index=True,
                        right_index=True)

    # inserting y-feature as the first column
    if y is not None:
        data = pd.concat([temp_y_col, data], axis=1)

    # printing the report for col / row dropping
    rows_after = len(data)
    cols_after = data.shape[1]

    if vectorize is not None:
        if type(vectorize) is str:
            vectorize = [vectorize]

        cols_after = data.shape[1] - 300 * len(vectorize)

    rows_total = rows_before - rows_after
    cols_total = cols_before - cols_after

    print("%d out of %d rows dropped" % (rows_total, rows_before))
    print("%d out of %d cols dropped" % (cols_total, cols_before))

    return data
