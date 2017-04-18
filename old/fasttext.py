from __future__ import print_function
import numpy as np

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Embedding
from keras.layers import GlobalAveragePooling1D
from keras.datasets import imdb

class FastText:
    
    '''
    Takes in pandas dataframe with at least two columns where one
    is the dependent variable, and one is text. 
    
    EXAMPLE USE: 
    
        FastText(data,var)
        
    If there is more than one possible depedent variable in df then
    there you can run the moddle for any of it. 
    
    '''
        
    def __init__(self,data,var):
        
        self.data = data
        self.var = var
        
        self.null = self._configuration()
        self.null = self._get_cube()
        self.null = self._padding()
        self.model = self._build_model()
      
    
    def _configuration(self):

        self.max_features = 125000
        self.maxlen = 800
        self.batch_size = 16
        self.embedding_dims = 20
        self.epochs = 2
        
        return "NULL"
    
    
    def _get_cube(self):
        
        o = Cube(self.data,self.var)
        
        self.x_train = o.x_train
        self.y_train = o.y_train
        self.x_test = o.x_test
        self.y_test = o.y_test
        
        return 'NULL'
        

    def create_ngram_set(self,input_list, ngram_value=2):

        return set(zip(*[input_list[i:] for i in range(ngram_value)]))

    
    def add_ngram(self,sequences, token_indice, ngram_range=2):

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

    
    def _padding(self):
    
        self.x_train = sequence.pad_sequences(self.x_train, maxlen=self.maxlen)
        self.x_test = sequence.pad_sequences(self.x_test, maxlen=self.maxlen)
        
        return 'NULL'
    

    def _build_model(self):

        model = Sequential()

        model.add(Embedding(self.max_features,    # efficient embedding layer which maps
                            self.embedding_dims,  # vocab indices into embedding_dims dimensions
                            input_length=self.maxlen))

        model.add(GlobalAveragePooling1D()) # avg the embeddings of all words in the document

        model.add(Dense(1, activation='hard_sigmoid')) # project onto a single unit 
                                                       # output layer, and squash it
        model.compile(loss='binary_crossentropy',
                      optimizer='adagrad',
                      metrics=['accuracy'])

        model.fit(self.x_train, self.y_train,
                  batch_size=self.batch_size,
                  epochs=self.epochs,
                  validation_data=(self.x_test, self.y_test))
        
        return model
