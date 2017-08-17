from vectorize_text import vectorize_text


def x_transform(X, data):

    # for a range of columns (two ints)
    if type(X) == list:
        if len(X) == 2:
            if type(X[0]) == int:
                x = data.ix[:, X[0]:X[1]]
                status = 'ok'

    # for multiple column index
    if type(X) == list:
        if len(X) > 2:
            if type(X[0]) == int:
                x = data.ix[:, X]
                status = 'ok'

    # for multiple column labels
    if type(X) == list:
        if type(X[0]) == str:
            x = data.loc[0:, X]
            status = 'ok'

    # for an integer as column name (int)
    if type(X) == int:
        x = data.iloc[:, X]
        status = 'ok'

    # for a single column label which contains string values
    if type(X) == str:
        if type(data[X][0]) == str:
            x = vectorize_text(data[X])
            status = 'ok'
        else:
            x = data[X]
            status = 'ok'

    # validate the result
    try:
        status == 'ok'
        return x

    except:
        print("ERROR: please check your X input if it's int, list of ints,")
        print("list of labels or label.")
        return False
