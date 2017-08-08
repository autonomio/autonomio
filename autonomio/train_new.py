import time
import numpy as np
import spacy as sp
import ascify as asc
import pandas as pd
import math

from transform_data import transform_data
from plots import accuracy
from prediction import load_model
from shapes import shapes
from double_check import check
from validator import validate

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
            neuron_max,
            neuron_last,
            batch_size,
            verbose,
            shape,
            double_check,
            validation):

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
    X_num, Y_num = X, Y

    X,Y = transform_data(data,flatten,dims,X,Y)

    #shuffling and separating the data
    if validation != False:

        if validation != True:
            n = len(X) * validation
            n = int(n)

        if validation == True:
            n = len(X) * .5
            n = int(n)

        X = X[:n]
        Y = Y[:n]

        if save_model == False:
            save_model = 'saved_model'
    
    np.random.seed()

    #Y = Y[:,8]

    if layers == 1:
        shape = 'funnel'

    if model != 'kuubio':
        model = load_model(model)
        history = ''  # this is no good and have to be dealt with in another way

    else:

        if neuron_max == 'auto' and dims >= 4:
            neuron_max = int(dims + (dims * 0.2))

        elif neuron_max == 'auto':
            neuron_max = 4

        #print neuron_max

        neuron_count = []
        neuron_count = shapes(  layers, 
                                shape, 
                                neuron_max,
                                neuron_last, 
                                dropout)

        model = Sequential()
        model.add(Dense(neuron_count[0], input_dim=dims, activation=activation))
        model.add(Dropout(dropout))

        for i in range(layers - 1):
            model.add(Dense(neuron_count[i+1], activation=activation))
            model.add(Dropout(dropout))

        model.add(Dense(neuron_last, activation=activation_out))
        model.compile(loss=loss, 
                      optimizer=optimizer, 
                      metrics=['accuracy'])

        print(model.summary())
        print ""
        network_scale = len(X) * epoch * layers * neuron_max
        print "network scale index : " + str(network_scale)

        if verbose == 0:
            if network_scale > 3000000000:
                print "This could take a while. Why not check back in a moment?"

        time.sleep(0.2)
        history = model.fit(X, Y,   validation_split=0.33, 
                                    epochs=epoch, 
                                    verbose=verbose, 
                                    batch_size=batch_size)

        scores = model.evaluate(X, Y, verbose=verbose)

        #print(history.history.keys())

        print ""

        if double_check == False or validation == False:
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
        print "1st layer neurons : " + str(neuron_max)
        print "flatten : " + str(flatten)
        print "batch_size : " + str(batch_size) 

        accuracy(history)

        if save_model != False:

            model_json = model.to_json()
            with open(save_model+".json", "w") as json_file:
                json_file.write(model_json)

            model.save_weights(save_model+".h5")
            print("Model" + " " + save_model + " " + "have been saved.")

            k = ""
            
            f = open(save_model+".x", "w+")
            
            if type(X_num) == list:
                for x in X_num:
                    k = k+str(x)+" "
            elif type(X_num) == int:
                k = str(X_num)
            else:
                k = X_num

            f.write(k)
            f.close()

        # calculate predictions
        predictions = model.predict(X)
        # round predictions
        rounded = [round(x[0]) for x in predictions]

        #printing result for double check
        if double_check == True:

            p = check(Y, rounded)

            print ""

            print ("keras accuracy: %.2f%%" % (scores[1]*100))
            print ("double check: %.2f%%" % (p*100))

        #printing result for validation
        if validation != False:

            train_scores, test_scores, val_acc = validate(  Y_num, 
                                                            data,
                                                            validation,
                                                            loss,
                                                            optimizer,
                                                            verbose,
                                                            save_model,
                                                            flatten,
                                                            dims)

            print ""
            print   ("train accuracy: %.2f%%" % (train_scores[1]*100))
            print   ("      loss: %.2f%%" % (train_scores[0]*100))
            print   ("test accuracy: %.2f%%" % (test_scores[1]*100)) 
            print   ("     loss: %.2f%%" % (test_scores[0]*100))
            print   ("validation accuracy: %.2f%%" % (val_acc*100))
    
    return 
