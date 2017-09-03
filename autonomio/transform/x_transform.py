from vectorize_text import vectorize_text


def x_transform(X, data):

    '''Transformation for X

    WHAT: Automatically interprets flexible input methods
    for the x variable, and vectorize if the values are string.

    HOW: x_transform('text', df)

    INPUT: A pandas dataframe and list with two ints, list of ints,
    list of string values (column labels), single integer, a single string
    value.

    OUTPUT: a dataframe with the selected columns. In the case of string
    values and a single string label as x input, vectorized text.

    '''

    # for a range of columns (two ints)
    if type(X) == list:
        if len(X) == 2:
            if type(X[0]) == int:
                x = data.ix[:, X[0]:X[1]]

    # for multiple column index
    if type(X) == list:
        if len(X) > 2:
            if type(X[0]) == int:
                x = data.iloc[:, X]

    # for multiple column labels
    if type(X) == list:
        if type(X[0]) == str:
            x = data.loc[:, X]

    # for an integer as column name (int)
    if type(X) == int:
        x = data.iloc[:, X]

    # for a single column label which contains string values
    if type(X) == str:

        first_index = data.index.values[0]
        if type(data[X][first_index]) == str or type(data[X][first_index]) == unicode:
            x = vectorize_text(data[X])

        else:
            x = data[X]

    return x
