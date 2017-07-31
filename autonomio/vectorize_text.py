import spacy as sp
from ascify import Ascify

nlp = sp.load('en')

def vectorize_text(data):
    
    '''
    OUTPUT:       a list of lists with the word vectors in lists
    
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

        print "from command line try: python -m spacy download en"
        return 'ERROR: spacy parser did not load'