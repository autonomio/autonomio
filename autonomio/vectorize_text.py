import spacy as sp
from ascify import Ascify


def vectorize_text(data, language='en'):
    
    nlp = sp.load(language)

    '''

    INPUT: a SERIES with string values

    OUTPUT: a list of lists with the word vectors in lists
    
    USE EXAMPLE:  vectors = vectorize_text(list_with_strings)

    
    ''' 

    try:
        
        nlp.parser.model  # to confirm that the parser loaded ok

        c = len(data)
        
        l = []

        for i in range(c):

            asc_string = Ascify(str(data[i:i+1])).ascify()
            uni_string = unicode(asc_string)
            vec_obj = nlp(uni_string)
            vector = vec_obj.vector
            l.append(vector)
            
        return l

    except:

        print "ERROR: from command line try: python -m spacy download en"

## Returns a list with 300 columns when succesful

