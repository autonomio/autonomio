import pandas as pd

from autonomio.transforms.datetime_handler import datetime_detector
from autonomio.transforms.wrangler_utils import string_contains_to_binary
from autonomio.transforms.value_starts_with import value_starts_with


def to_category_labels(data,
                       max_categories,
                       starts_with_col,
                       col_that_contains,
                       col_contains_strings):

    '''Categorical Labeling

    Typically called through the wrangler() function.

    WHAT: takes in a dataframe and automatically and based on user input
    transforms data ready for training or testing. Note that both train
    and test data should be transformed with the same settings.

    '''

    datetime_cols = datetime_detector(data)

    for col in data.columns:
        if col not in datetime_cols:

            # test if the column is already float or int
            try:
                data[col] = data[col].astype('float')

            # if not, covert in to categorical labels or drop
            except ValueError:
                # contains a value
                if col_that_contains == col:
                    temp_contains = string_contains_to_binary(data,
                                                              col_that_contains,
                                                              col_contains_strings)

                    data = data.drop(col_that_contains, axis=1)
                    data = pd.concat([data, temp_contains], axis=1)
                    print("TO CATEGORY (col_that_contains): %s" % col)

                # initiates conversion to labels based on first character
                elif starts_with_col == col:
                    data[col] = value_starts_with(data, col)
                    data[col] = pd.Categorical(data[col]).codes
                    print("TO CATEGORY (starts_with_col): %s" % col)

                # checks if the column meets the conversion treshold
                else:
                    if len(data[col].unique()) <= max_categories:
                        data[col] = pd.Categorical(data[col]).codes
                        print("TO CATEGORY (automatic): %s" % col)
                    else:
                        data = data.drop(col, axis=1)
                        print("DROPPED (string values): %s" % col)

        else:
            print("Treated as datetime: %s" % col)
    return data
