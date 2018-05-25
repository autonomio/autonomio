import datetime
import pandas as pd

from autonomio.transforms.column_handler import column_mover


def datetime_detector(data, datetime_mode='retain'):

    '''Datetime Handling

    WHAT: Detects a datetime column and sends it to the
    datetime_handler for processing based on the
    datetime_mode setting.

    OPTIONS: 'pass', drop', 'sequence', and 'retain'

    '''

    datetime_cols = []

    for col in data.columns:
        if isinstance(data[col][0], datetime.date) is True:
            datetime_cols.append(col)

    return datetime_cols


def datetime_handler(data, datetime_mode='pass'):

    if datetime_mode == 'pass':
        return data

    datetime_cols = datetime_detector(data, datetime_mode=datetime_mode)
    datetime_cols_len = len(datetime_cols)

    # case where there is no datetime
    if datetime_cols_len is 0:
        return data

    # case where there is a single datetime column
    if datetime_cols_len is 1:

        if datetime_mode is 'drop':
            data = data.drop(datetime_cols, axis=1)
            return data

        elif datetime_mode is 'sequence':
            data = datetime_to_sequence(data, datetime_cols)
            return data

        elif datetime_mode is 'retain':
            data = column_mover(data, datetime_cols)
            return data

    # case where there are more than one datetime column
    if datetime_cols_len > 1:

        if datetime_mode is 'drop':
            data = data.drop(datetime_cols, axis=1)
            return data

        elif datetime_mode is 'sequence':

            for col in datetime_cols:
                data = datetime_to_sequence(data, col)
            return data

        elif datetime_mode is 'retain':
            data = column_mover(data, datetime_cols)
            return data


def datetime_to_sequence(data, col):

    '''
    INPUT: A pandas dataframe and a single column string value

    OUTPUT: A pandas dataframe with the converted timestamp column

    '''

    # sort according to timestamps
    sorted_datetime_col = pd.DataFrame(data[col]).sort_values(col)

    # create a sequence of integers that correlates with the
    # sequence of time linearly
    sorted_datetime_col = sorted_datetime_col.reset_index().reset_index()
    sorted_datetime_col = sorted_datetime_col.set_index('index')

    sorted_datetime_col = sorted_datetime_col.drop(col, axis=1)
    sorted_datetime_col.columns = [col]
    data = data.drop(col, axis=1)
    data = pd.merge(sorted_datetime_col,
                    data,
                    left_index=True,
                    right_index=True)

    return data
