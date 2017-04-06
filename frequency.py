from __future__ import print_function

import plac
import io

import spacy
from spacy.attrs import ORTH
from spacy import en
import somecode as some
import pandas as pd
import ascify as asc

class Frequency:

    '''
    USE EXAMPLE: 

        freq = f.Frequency(out)
        print freq.noun_token()

    '''
    
    def __init__(self,data):
        
        self.en = en
        self.nlp = spacy.load('en')
        self.stopwords = self._stop_words()
        self.data = self._get_data(data)

    def _get_data(self,data):

        if type(data) != 'pandas.core.series.Series':
            
            data = pd.Series(data)

        text = [str(line).strip() for line in data]

        out = ''

        for tweet in text:

             out += tweet

        text = unicode(out.lower())
        doc = self.nlp(text)

        return doc
    
    
    def _stop_words(self):
        
        stopwords = some.stopword()
        stopwords = stopwords[0]

        for word in self.en.STOP_WORDS:
            
            stopwords.append(word)
            
        return stopwords

    
    def single_word(self):

        l=[]
        counts = self.data.count_by(ORTH)
        self.stopwords += ['...','.....','......','n\'t']

        for word_id, count in sorted(counts.items(), reverse=True, key=lambda item: item[1]):

            if self.nlp.vocab.strings[word_id] not in en.STOP_WORDS:
                if self.nlp.vocab.strings[word_id] not in self.stopwords:
                    if len(self.nlp.vocab.strings[word_id]) > 2:
                        l.append([count, self.nlp.vocab.strings[word_id]])

        df = pd.DataFrame(l)
        df.columns = ['frequency','word']
        
        return df
        
        
    def noun_token(self):
        
        l = []
        
        for np in self.data.noun_chunks:

            string = str(np)
            
            if string not in self.stopwords:
                if len(string) >2:

                    l.append(string)

            else: 
                l.append("None")

        out = pd.DataFrame(l)
        out.columns = ['token']

        out = out.token.value_counts()
            
        return out
    
    def _entities(self):
        
        l=[]
        
        for ent in self.data.ents:
            
            l.append([str(ent), str(ent.label), str(ent.label_)])
            
        out = pd.DataFrame(l)
        out.columns = ['entity','a','class']
        out['count'] = 1
        
        return out
    
            
    def entities(self):
        
        entities = self._entities()

        entity = pd.DataFrame(entities).groupby(['entity','class']).sum()
        entity = entity.reset_index()
        entity = entity.sort_values('count',ascending=False)

        cleaned = entity[~entity['entity'].isin(self.stopwords)]
        cleaned = cleaned[cleaned['class'] != 'CARDINAL']
        cleaned = cleaned[cleaned['class'] != 'PERCENT']
        cleaned = cleaned[cleaned['class'] != 'TIME']
        cleaned = cleaned[cleaned['class'] != 'MONEY']
        cleaned = cleaned[cleaned['class'] != 'DATE']
        cleaned = cleaned[cleaned['class'] != 'ORDINAL']
        cleaned = cleaned[cleaned['entity'].str.len() > 2]
        
        return cleaned
