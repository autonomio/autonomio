import spacy as sp
from ascify import *

nlp = sp.load('en')

def vectorize_text(data):
    
    '''
    OUTPUT:       a list of lists with the word vectors in lists
    
    USE EXAMPLE:  vectors = vectorize_text(list_with_strings)

    ''' 
    
    c = len(data)
    
    l = []

    for i in range(c):

        asc_string = Ascify(str(data[i:i+1])).ascify()
        uni_string = unicode(asc_string)
        vec_obj = nlp(uni_string)
        vector = vec_obj.vector
        l.append(vector)
        
    return l
