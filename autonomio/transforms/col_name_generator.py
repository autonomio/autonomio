def col_name_generator(data, prefix='C'):

    '''Column Name Generator

    WHAT: A helper function that generates alphabetic
    column names automatically.

    HOW: col_name_generator(df)

    INPUT: A pandas dataframe

    OUTPUT: The input dataframe with alphabetical sequence
    column names.

    '''

    no_of_cols = data.shape[1]
    l = []

    for i in range(no_of_cols):

        l.append(prefix + str(i))

    data.columns = l

    return data
