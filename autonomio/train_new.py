import time
import numpy as np
import spacy as sp
import ascify as asc
import pandas as pd

from transform_data import transform_data
from plots import accuracy
from prediction import load_model

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
import keras.backend as K

import matplotlib.pyplot as plt

def kuubio(X,Y,data,
            dims,
            epoch,
            flatten,
            dropout,
            layers,
            model,
            loss,
            optimizer,
            activation,
            activation_out,
            save_model,
            neuron_first,
            neuron_last,
            batch_size,
            verbose):

    '''
    
    IMPORTANT: to see the plots in jupyter remember to invoke: 

                    %matplotlib inline

    (could be used as stand-alone but we call it through commands)

    INPUT:  X with one or more variables in float32 and Y with a single 
            binary value. These can be easily produced through 
            transform_data if you insist to bybass commands function.  

    OUTOUT: Trains a model and outputs the training results with a plot
            comparing train and test. The predictions are loaded on to 
            a data object. 

    ''' 

    ind_var = Y   # this is used later for output 

    X,Y = transform_data(X,Y,data,flatten,dims)
    
    np.random.seed()

    #Y = Y[:,8]

    if model != 'kuubio':
        model = load_model(model)
        history = ''  # this is no good and have to be dealt with in another way

    else:
        if neuron_first == 'auto':
            neuron_first = int(dims + (dims * .05))
        model = Sequential()
        model.add(Dense(neuron_first, input_dim=dims, activation=activation))
        model.add(Dropout(dropout))

        neuron_previous = neuron_first
        
        for i in range(layers-1):

            neuron_count = (neuron_previous + neuron_last) / 2

            model.add(Dense(neuron_count, activation=activation))
            model.add(Dropout(dropout))

            neuron_previous = neuron_count
        
        model.add(Dense(neuron_last, activation=activation_out))
        model.compile(loss=loss, 
                      optimizer=optimizer, 
                      metrics=['accuracy'])

        print(model.summary())
        print ""
        network_scale = len(X) * epoch * layers * neuron_first 
        print "network scale index : " + str(network_scale)

        if verbose == 0:
            if network_scale > 3000000000:
                print "This could take a while. Why not check back in a moment?"

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

        print "epochs : " + str(epoch)
        print "features : " + str(dims)
        print "layers : " + str(layers)
        print "dropout : " + str(dropout)
        print "1st layer neurons : " + str(neuron_first)
        print "flatten : " + str(flatten)
        print "batch_size : " + str(batch_size) 

        accuracy(history)

        if save_model != False:

            model_json = model.to_json()
            with open(save_model+".json", "w") as json_file:
                json_file.write(model_json)
            model.save_weights(save_model+".h5")
            print("Model" + " " + save_model + " " + "have been saved.")

        # calculate predictions
        predictions = model.predict(X)
        # round predictions
        rounded = [round(x[0]) for x in predictions]
    
    return rounded, history