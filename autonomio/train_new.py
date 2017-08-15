import time
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

from IPython.display import display

from transform_data import transform_data
from plots import accuracy
from shapes import shapes
from double_check import check
from validator import validate
from save_model_as import save_model_as


def trainer(X, Y, data,
            dims,
            epoch,
            flatten,
            dropout,
            layers,
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

    X, Y = transform_data(data, flatten, X, Y)

    try:
        dims = X.shape[1]
    except IndexError:
        dims = X_num

    # shuffling and separating the data
    if validation is not False:

        if validation is not True:
            n = len(X) * validation
            n = int(n)

        if validation is True:
            n = len(X) * .5
            n = int(n)

        X = X[:n]
        Y = Y[:n]

        if save_model is False:
            save_model = 'saved_model'

    if layers == 1:
        shape = 'funnel'

    else:

        if neuron_max == 'auto' and dims >= 4:
            neuron_max = int(dims + (dims * 0.2))

        elif neuron_max == 'auto':
            neuron_max = 4

        neuron_count = []
        neuron_count = shapes(layers,
                              shape,
                              neuron_max,
                              neuron_last,
                              dropout)

        model = Sequential()
        model.add(Dense(neuron_count[0],
                        input_dim=dims,
                        activation=activation))
        model.add(Dropout(dropout))

        for i in range(layers - 1):
            model.add(Dense(neuron_count[i+1], activation=activation))
            model.add(Dropout(dropout))

        model.add(Dense(neuron_last, activation=activation_out))
        model.compile(loss=loss,
                      optimizer=optimizer,
                      metrics=['accuracy'])

        network_scale = len(X) * epoch * layers * neuron_max

        time.sleep(0.2)
        history = model.fit(X, Y, validation_split=0.33,
                            epochs=epoch,
                            verbose=verbose,
                            batch_size=batch_size)

        scores = model.evaluate(X, Y, verbose=verbose)

        if double_check is False or validation is False:
            print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

        # model parameters
        ex1 = pd.Series({
                         'ind_var': ind_var,
                         'y_transform': flatten,
                         'n=': len(X),
                         'features': dims,
                         'epochs': epoch,
                         'layers': layers,
                         'dropout': dropout,
                         'batch_size': batch_size,
                         'shape': shape,
                         'max_neurons': neuron_max,
                         'network_scale': network_scale})

        # train / test results
        ex2 = pd.DataFrame({
                        'train_acc': history.history['acc'],
                        'train_loss': history.history['loss'],
                        'test_acc': history.history['val_acc'],
                        'test_loss': history.history['val_loss']})

        display(pd.DataFrame(ex1).transpose())

        accuracy(history)

        if save_model is not False:

            save_model_as(X_num, model, save_model)

        # calculate and round predictions
        predictions = model.predict(X)
        rounded = [round(x[0]) for x in predictions]

        # printing result for double check
        if double_check is True:

            p = check(Y, rounded)

            print ("keras accuracy: %.2f%%" % (scores[1]*100))
            print ("double check: %.2f%%" % (p*100))

        # printing result for validation
        if validation is not False:

            train_scores, test_scores, val_acc = validate(Y_num,
                                                          data,
                                                          validation,
                                                          loss,
                                                          optimizer,
                                                          verbose,
                                                          save_model,
                                                          flatten)

            print("\n train accuracy: %.2f%%" % (train_scores[1]*100))
            print("loss: %.2f%%" % (train_scores[0]*100))
            print("test accuracy: %.2f%%" % (test_scores[1]*100))
            print("loss: %.2f%%" % (test_scores[0]*100))
            print("validation accuracy: %.2f%%" % (val_acc*100))

    return

# Returns output on the screen
