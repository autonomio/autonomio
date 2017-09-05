import pandas as pd

from autonomio.text.processing import text_to_blob
from autonomio.text.processing import word_filtering


def index_builder(data,
                  word_limit=1000,
                  min_len=3,
                  max_len=10,
                  pos=None,
                  entity=None):

    '''Word Index Builder

    WHAT: Creates an index based on words in a given set of text.

    HOW: index_builder(df.text)

    INPUT: a series / dataframe column of text values

    OUTPUT: an index table in a dictionary format

    '''

    data = text_to_blob(data)
    data = word_filtering(data,
                          min_len=min_len,
                          max_len=max_len,
                          pos=pos,
                          entity=entity)

    data = pd.Series(data).value_counts()
    data = data.head(word_limit).index.values
    data = pd.DataFrame(data)
    data = data.reset_index()
    data = data.set_index(0)
    data = data.to_dict()

    return data
