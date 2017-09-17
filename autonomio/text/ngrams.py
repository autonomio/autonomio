from keras.preprocessing import sequence
import numpy as np

from autonomio.text.words_to_ints import words_to_ints


def text_to_ngram(data, ngram_value=2):

    return set(zip(*[data[i:] for i in range(ngram_value)]))


def _add_ngram(sequences, token_indice, ngram_range=2):

    '''Helper Function for Creating Ngram Index.

    Not intended to be used with any other purpose
    than through embeds_ngrams()

    '''

    new_sequences = []
    for input_list in sequences:
        new_list = input_list[:]
        for i in range(len(new_list) - ngram_range + 1):
            for ngram_value in range(2, ngram_range + 1):
                ngram = tuple(new_list[i:i + ngram_value])
                if ngram in token_indice:
                    new_list.append(token_indice[ngram])
        new_sequences.append(new_list)

    return new_sequences


def embeds_ngrams(x, ngrams=2, strings=True, max_len=True):

    '''Embedding Ngram Pipeline

    Creates a word embedding index out of text that is first
    treated as ngrams and then converted in to a an index.
    Behaves same as words_to_ints, but with the difference
    of creating ngrams as opposed to single word occurance.


    '''

    if strings is True:
        x = words_to_ints(x)

    if max_len is True:
        temp = [len(x[i]) for i in range(len(x))]
        max_len = max(temp)
    else:
        max_len == max_len

    ngram_set = set()
    for input_list in x:
        for i in range(2, ngrams + 1):
            set_of_ngram = text_to_ngram(input_list, ngram_value=i)
            ngram_set.update(set_of_ngram)

    start_index = np.array(np.array(x).max()).max()
    token_indice = {v: k + start_index for k, v in enumerate(ngram_set)}

    x = _add_ngram(x, token_indice, ngrams)

    x = sequence.pad_sequences(x, maxlen=max_len)

    return x
