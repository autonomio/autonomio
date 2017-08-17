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
from mlp_model import mlp


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
            validation,
            parameters):

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

    parameters['X'] = X
    parameters['Y'] = Y

    try:
        dims = X.shape[1]
    except IndexError:
        dims = X_num

    parameters['dims'] = dims

    if layers == 1:
        shape = 'funnel'

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

    parameters['neuron_count'] = neuron_count

    model, history = mlp(parameters)

    network_scale = len(X) * epoch * layers * neuron_max

    # train / test results
    ex2 = pd.DataFrame({
                    'train_acc': history.history['acc'],
                    'train_loss': history.history['loss'],
                    'test_acc': history.history['val_acc'],
                    'test_loss': history.history['val_loss']})

    accuracy(ex2)

    scores = model.evaluate(X, Y, verbose=verbose)

    if double_check is False or validation is False:
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    # calculate and round predictions
    predictions = model.predict(X)
    rounded = [round(x[0]) for x in predictions]

    if double_check is True:
            check(Y, rounded, scores)

    if save_model is False and validation is not False:
        save_model = 'saved_model'

    if save_model is not False:
        save_model_as(X_num, data.columns, model, save_model)

    # shuffling and separating the data
    if validation is not False:
        X, Y, save_model = validate(Y_num,
                                    data,
                                    validation,
                                    loss,
                                    optimizer,
                                    verbose,
                                    save_model,
                                    flatten)

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

    

    display(pd.DataFrame(ex1).transpose())

    # printing result for double check

    return
