import time
import warnings
import numpy as np
import spacy as sp
import ascify as asc
import pandas as pd

from vectorize_text import *

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
nlp = sp.load('en')

def _transform_data(x_text,y_var,data,flatten): 
    
    if type(x_text) == list:
        if type(x_text[0]) == int:
            x = data.ix[:,x_text[0]:x_text[1]]
        else:
            x = data[x_text]
        
    else: 
        x = vectorize_text(data[x_text])
    
    y = [data[y_var]]
    
    try:
        
        if len(y) == 1:

            y = map(list, zip(*y))

        if len(y) == len(x):

            x1 = x   # we do this to retain the original y and x
            y1 = y

            df_x = pd.DataFrame(x1)
            df_y = pd.DataFrame(y1)
            
            if flatten == 'mean':
                df_y = pd.DataFrame(df_y[0] >= df_y[0].mean()).astype(int)
            elif flatten == 'median':    
                df_y = pd.DataFrame(df_y[0] >= df_y[0].median()).astype(int)
            elif type(flatten) == float:
                df_y = pd.DataFrame(df_y[0] >= df_y[0].quantile(flatten)).astype(int)
            elif flatten == 'none':
                df_y = pd.DataFrame(df_y).astype(int)
    except:
        
        print "ERROR: something went wrong"
        
    return df_x,df_y


def kuubio(X,Y,data,dims=300,epoch=5,flatten='mean',
           dropout=.2,layers=3,
           model='train',loss='binary_crossentropy',
           save_model=False,
           neuron_first='auto',neuron_last=1,
           batch_size=10,verbose=0):
    
    ind_var = Y
    X,Y = _transform_data(X,Y,data,flatten)
    
    '''
    NOTE:  1) the data has to be in float or something that
              goes nicely in to 'float32'
           
           2) the data has to be in pandas dataframe 
              with no column names (other than int)
    '''

    np.random.seed(7)
    
    X = X.astype('float32')
    Y = Y.astype('float32')
    
    X = np.array(X)
    Y = np.array(Y)
    
    X = X[:,0:dims]
    #Y = Y[:,8]
    
    if model != 'train':
        model = _load_model(model)
    else:
        model = Sequential()
        
        if neuron_first == 'auto':
            neuron_first = int(dims + (dims * .5))
            
            
        if layers == 2:

            layer_a = int(neuron_first / 1.5)

            model.add(Dense(neuron_first, input_dim=dims, activation='relu'))
            model.add(Dropout(dropout))
            model.add(Dense(neuron_last, activation='sigmoid'))

        if layers == 3:

            layer_a = int(neuron_first / 1.5)

            model.add(Dense(neuron_first, input_dim=dims, activation='relu'))
            model.add(Dropout(dropout))
            model.add(Dense(layer_a, activation='relu'))
            model.add(Dense(neuron_last, activation='sigmoid'))

        if layers == 4:

            layer_a = int(neuron_first / 1.5)
            layer_b = int(layer_a / 1.5)

            model.add(Dense(neuron_first, input_dim=dims, activation='relu'))
            model.add(Dropout(dropout))
            model.add(Dense(layer_a, activation='relu'))
            model.add(Dropout(dropout))
            model.add(Dense(layer_b, activation='relu'))
            model.add(Dense(neuron_last, activation='sigmoid'))

        if layers == 5:

            layer_a = int(neuron_first / 1.5)
            layer_b = int(layer_a / 1.5)
            layer_c = int(layer_b / 1.5)

            model.add(Dense(neuron_first, input_dim=dims, activation='relu'))
            model.add(Dropout(dropout))
            model.add(Dense(layer_a, activation='relu'))
            model.add(Dropout(dropout))
            model.add(Dense(layer_b, activation='relu'))
            model.add(Dropout(dropout))
            model.add(Dense(layer_c, activation='relu'))
            model.add(Dense(neuron_last, activation='sigmoid'))

        model.compile(loss=loss, 
                      optimizer='adam', 
                      metrics=['accuracy'])

        print(model.summary())
        print ""
        network_scale = len(X) * epoch * layers * neuron_first 
        print "network scale : " + str(network_scale)

        if verbose == 0:
            if network_scale > 100000000:
                print "This could take " + str(network_scale / 1000000) + " minutes. Why not have a break?"

        time.sleep(0.2)
        history = model.fit(X, Y, validation_split=0.33, epochs=epoch, verbose=verbose, batch_size=batch_size)
        scores = model.evaluate(X, Y)

        #print(history.history.keys())

        print ""
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        print ""
        print "TRIAL PARAMETERS"
        print "----------------"
        print "indepedent variable : " + ind_var
        print "n= : " + str(len(X))

        print "features : " + str(dims)
        print "layers : " + str(layers)
        print "dropout : " + str(dropout)
        print "1st layer neurons : " + str(neuron_first)
        print "flatten : " + str(flatten)
        print "batch_size : " + str(batch_size) 

	plt.style.use('bmh')
        fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

        ax1.plot(history.history['acc'])
        ax1.plot(history.history['val_acc'])
        ax2.plot(history.history['loss'])
        ax2.plot(history.history['val_loss'])

        ax1.set_title('accuracy')
        ax1.set_xlabel('epoch')

        #ax1.set_ylabel('accuracy')

        ax2.set_title('loss')
        ax2.set_xlabel('epoch')
        #ax3.set_ylabel('loss')

        fig.set_size_inches(12,3)

        if save_model == True:

            model_json = model.to_json()
            with open("model.json", "w") as json_file:
                json_file.write(model_json)
            model.save_weights("model.h5")
            print("Saved model to disk")

        # calculate predictions
        predictions = model.predict(X)
        # round predictions
        rounded = [round(x[0]) for x in predictions]

        fig.show() 
    
    return rounded
