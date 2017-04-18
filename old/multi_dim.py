import pandas as pd
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model, Sequential
from keras.layers import LSTM, Dense
import load_data

#df = pd.read_csv("sample1.csv")

class MultiDim:
    
    '''
    Takes in multi-dimensional data and runs a model based on it. 
    
    '''

    def __init__(self,data):
        
        self.data = data
        
        self.null = self._prepare_data()
        self.null = self._prepare_shape()
        self.null = self._prepare_dimensions()
        self.null = self._build_model()
        
    def _prepare_data(self):
        
        if self.data.shape[1] != 4:
            
            print "shape of the data is wrong > you need 4 variable columns"
        
        else:
            self.data['single_input_vector'] = self.data.apply(tuple, axis=1).apply(list)
            self.data['single_input_vector'] = self.data.single_input_vector.apply(lambda x: [list(x)])
            self.data['cumulative_input_vectors'] = self.data.single_input_vector.cumsum()
            self.data['output_vector'] = self.data[[1]].apply(tuple, axis=1).apply(list)

            self.max_sequence_length = self.data['cumulative_input_vectors'].apply(len).max()
            self.padded_sequences = pad_sequences(self.data['cumulative_input_vectors'].tolist(), self.max_sequence_length).tolist()
            self.data['padded_input_vectors'] = pd.Series(self.padded_sequences).apply(np.asarray)

        return 'NULL'

    def _prepare_shape(self):
        
        self.X_train_init = np.asarray(self.data.padded_input_vectors)
        self.X_train = np.hstack(self.X_train_init).reshape(len(self.data),self.max_sequence_length,4)
        self.y_train = np.hstack(np.asarray(self.data.output_vector)).reshape(len(self.data),1)
        
        return 'NULL'
    
    def _prepare_dimensions(self):

        self.input_length = self.X_train.shape[1]
        self.input_dim = self.X_train.shape[2]
        self.output_dim = len(self.y_train[0])
        
        return 'NULL'
    
    def _build_model(self):

        model = Sequential()
        model.add(LSTM(4,input_dim=self.input_dim,input_length=self.input_length))
        model.add(Dense(self.output_dim,activation='relu'))
        model.compile(loss='mean_squared_error',optimizer='sgd',metrics=['accuracy'])
        history = model.fit(self.X_train,self.y_train,batch_size=7,nb_epoch=3,verbose=1)
                
        return 'NULL'
