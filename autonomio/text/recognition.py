import spacy as sp


def entity_recognition(word):

    '''Entity Recognition

    WHAT: recognize if a word is an entity.

    HOW: entity_recognition('word')

    INPUT: a string

    OUTPUT: the entity class or emtpy

    '''
    try:
        nlp.lang
    except NameError:
        nlp = sp.load('en')

    word = unicode(word)
    doc = nlp(word)
    out = doc[0].ent_type_

    return out


def part_of_speech(word):

    '''Part-of-Speech Recognition

    WHAT: recognize the part of speech of a word (e.g. noun)

    HOW: part_of_speech('word')

    INPUT: a string

    OUTPUT: the pos classification for the word

    '''
    try:
        nlp.lang
    except NameError:
        nlp = sp.load('en')

    word = unicode(word)
    doc = nlp(word)
    out = doc[0].pos_

    return out
