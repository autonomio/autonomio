def nan_finder(data):

    '''
    Finds nans and provides a dataframe
    with the column names and fraction of
    nans in the column.

    '''

    temp = data.transpose().isnull()
    temp = temp.transpose().describe()
    temp = temp.transpose().drop('count', axis=1)
    temp.unique = temp.unique == 1
    temp.freq = temp.freq / len(data)
    temp.freq = temp.freq - temp.top
    temp = temp.drop('top', axis=1)
    temp.columns = ['no_nans', 'quality']

    return temp


def nan_dropper(data, treshold=.9):

    '''
    Drops nans in a specific column or a range of
    columns, using np.isnull() through pandas.

    The treshold sets the % at which the whole column
    is droped (nan % of all values in the column).

    '''

    temp = nan_finder(data)
    temp = temp.transpose()

    for col in temp:
        if temp[col][1] < treshold:
            data = data.drop(col, axis=1)

    data.dropna(inplace=True)
    #data = data.reset_index().drop('index', axis=1)

    return data


def nan_filler(data, cols, fill_with):

    '''
    Fills nans in a specific column or a range of
    columns, using np.isnull() through pandas.

    This is for the cases where some nans are dropped,
    but some nans are converted in to zero (or other)
    first.

    '''

    if data[cols].dtype == 'O':
        fill_with = str(fill_with)

    if type(cols) != list:
        cols = [cols]
    for col in cols:
        cols = [cols]
        data = data[col].fillna(fill_with)

    return data
