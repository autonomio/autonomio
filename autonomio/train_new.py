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
from regression import regression


def trainer(X, Y, data, para):

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

    X, Y = transform_data(data, para['flatten'], X, Y)

    try:
        dims = X.shape[1]
    except IndexError:
        dims = X_num

    para['dims'] = dims

    if para['layers'] == 1:
        para['shape'] = 'funnel'

    if para['neuron_max'] == 'auto' and dims >= 4:
        para['neuron_max'] = int(dims + (dims * 0.2))

    elif para['neuron_max'] == 'auto':
        para['neuron_max'] = 4

    para['neuron_count'] = shapes(para)

    if para['model'] is 'mlp':
        model, history = mlp(X, Y, para)
    if para['model'] is 'regression':
        model, history = regression(X, Y, para['epoch'], para['reg_mode'])

    network_scale = len(X)*para['epoch']*para['layers']*para['neuron_max']

    # train / test results
    ex2 = pd.DataFrame({
                    'train_acc': history.history['acc'],
                    'train_loss': history.history['loss'],
                    'test_acc': history.history['val_acc'],
                    'test_loss': history.history['val_loss']})

    accuracy(ex2)

    scores = model.evaluate(X, Y, verbose=para['verbose'])

    validation = para['validation']
    save_model = para['save_model']

    if para['double_check'] is False or para['validation'] is False:
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    # calculate and round predictions
    predictions = model.predict(X)
    rounded = [round(x[0]) for x in predictions]

    if para['double_check'] is True:
            check(Y, rounded, scores)

    if para['save_model'] is False and para['validation'] is not False:
        para['save_model'] = 'saved_model'

    if para['save_model'] is not False:
        save_model_as(X_num, data.columns, model, para['save_model'])

    # shuffling and separating the data
    if para['validation'] is not False:
        X, Y = validate(Y_num, data, para)

    # model parameters
    ex1 = pd.Series({
                     'ind_var': ind_var,
                     'y_transform': para['flatten'],
                     'n=': len(X),
                     'features': para['dims'],
                     'epochs': para['epoch'],
                     'layers': para['layers'],
                     'dropout': para['dropout'],
                     'batch_size': para['batch_size'],
                     'shape': para['shape'],
                     'max_neurons': para['neuron_max'],
                     'network_scale': network_scale})

    

    display(pd.DataFrame(ex1).transpose())

    # printing result for double check

    return
