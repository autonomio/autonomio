from keras.preprocessing.text import one_hot
from keras.preprocessing import sequence


def words_to_ints(data, pad_sequences=False):

    '''Word Embeddings

    WHAT: Creates the data format required for word
    embeddings.

    HOW: word_to_ints(df.text, 50)

    OPTIONS: pad_sequencies is either False or an integeer
    value which limits the number of columns / words
    per sample.

    INPUT: a single column with string values.

    OUTPUT: a 2-dimensional array where each column represent
    a single word from the original input.

    '''

    out = []
    i = 0
    n = len(data)

    for item in data:

        temp = one_hot(item, n, lower=True, split=" ")
        out.insert(i, temp)
        i += 1

    if pad_sequences is not False:

        out = sequence_padding(out, pad_sequences)

    return out


def sequence_padding(data, maxlen):

    '''Sequence Padding

    WHAT: Pads a list of lists where lists are varying length.

    '''

    data = sequence.pad_sequences(data, maxlen=maxlen)

    return data
