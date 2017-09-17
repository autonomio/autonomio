def accept_string_as_iterable(data):

    '''Input Checker

    WHAT: Checks input and makes it in to a list if its
    a string or unicode.

    INPUT: Any data object

    OUTPUT: the same data object if not string or unicode,
    or else a list with the string or unicode value.

    '''

    data_type = type(data)

    if data_type is str or data_type is unicode:
        data = [data]

    return data
