import string

from autonomio._utils.iterables import accept_string_as_iterable
from autonomio.text.recognition import entity_recognition
from autonomio.text.recognition import part_of_speech


def text_to_words(data, decoder='utf-8'):

    data = accept_string_as_iterable(data)
    blob = u''
    for text in data:
        blob += text.decode(decoder)

    blob = blob.split()

    return blob


def text_to_blob(data, decoder='utf-8'):

    data = accept_string_as_iterable(data)
    blob = u''
    for text in data:
        blob += text.decode(decoder)

    return blob


def text_to_chars(data, decoder='utf-8'):

    data = accept_string_as_iterable(data)
    chars = u''
    for text in data:
        words = text.split()
        for word in words:
            for char in word:
                chars += char.decode(decoder)

    return chars


def word_filtering(data,
                   output=list,
                   min_len=3,
                   max_len=10,
                   pos=None,
                   entity=None):

    '''Word Filtering

    WHAT: a utility for extracting meaningful words out of text

    HOW: word_filtering('some string comes in here')

    INPUT: a string value

    OUTPUT: a list with the words

    output = by default 'list' or can be 'string' as well.

    mix_len = min length allowed for a word to not be dropped

    max_len = max length allowed for a word to be not filtered

    pos = part of speech tagging. See full reference for codes:
    https://spacy.io/docs/usage/pos-tagging#pos-tagging-english

    entity = if true, will turn on entity recognition. In order to
    just identify entities, 'pos' needs to be None.

    '''

    if type(data) is str or unicode:

        data = data.split()

    temp = []

    for word in data:

        temp_word = ''

        # length based filtering
        length = len(word)
        if length > min_len and length < max_len:
            temp_word = word

            # entity recognition based filtering
            if entity is True:
                if entity_recognition(word) is not u'':
                    temp_word = word
                else:
                    temp_word = ''

            # part-of-speech based filtering
            if pos is not None:
                if part_of_speech(word) in pos:
                    temp_word = word
                else:
                    temp_word = ''

        elif length > min_len and length < max_len:
            temp_word = word

        temp.append(temp_word)

        for i in range(len(temp)):
            try:
                temp.remove('')
            except ValueError:
                pass

    if output is str:
        temp_str = ''
        for word in temp:
            temp_str += word

        temp = temp_str

    return temp
