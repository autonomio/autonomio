import re
import string
from autonomio.text.stopwords import stopword


def _strip_punctuation(data):

    pattern = re.compile('[\W_]+')
    out = pattern.sub('', data)

    return out


def remove_punctuation(data):

    data = map(_strip_punctuation, data)

    return data


def remove_stopwords(data, lowercase=True):

    if lowercase is True:
        data = map(string.lower, data)

    data = list(data)
    stopwords = stopword()
    data = set(data) - set(stopwords)
    data = list(data)

    return data
