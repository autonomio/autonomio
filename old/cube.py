import numpy as np
import pandas as pd
import keras
import pandas as pd
import keras.preprocessing.text
import somecode as some

class Cube:
    
    '''
    
    INTENDED USE > to be called through FastText() class. 
    
    Takes in pandas dataframe with at least two columns where one
    is the dependent variable, and one is text. 
    
    EXAMPLE USE: 
    
        Cube(data,var)
        
    If there is more than one possible depedent variable in df then
    there you can run the moddle for any of it. 
    
    
    '''
    
    
    def __init__(self,data,var):
        
        self.data = data
        self.var = var
        self.x,self.y = self._data_sets()
        self.x_train, self.y_train, self.x_test, self.y_test = self._split_data()
        
    def _word_index(self):

        out = []
        i = 0
        n = len(self.data)

        for item in self.data.text:

            temp = keras.preprocessing.text.one_hot(item, n, lower=True, split=" ")
            out.insert(i,temp)
            i += 1

        return out
    

    def _data_sets(self):

        data = self.data.sample(frac=1)

        x = self._word_index()
        y = data[self.var]

        return x,y


    def _split_data(self):

        length = len(self.x)
        i = length - (length / 3)

        self.x_test = self.x[:i]
        self.x_test = np.array(self.x_test)

        self.x_train = self.x[i+1:]
        self.x_train = np.array(self.x_train)

        self.y_test = self.y[:i]
        self.y_test = np.array(self.y_test)
        self.y_train = self.y[i+1:]
        self.y_train = np.array(self.y_train)

        return self.x_train, self.y_train, self.x_test, self.y_test
