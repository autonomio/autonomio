import pandas as pd
import numpy as np

from IPython.display import display

from keras import backend as K

from transform.transform_data import transform_data
from plots.plots import accuracy
from utils.shapes import shapes
from utils.double_check import check
from utils.validator import validate, separate
from save_model_as import save_model_as
from models.mlp import mlp
from models.regression import regression
from plots.trainplot import trainplot
from autonomio.plots.plots import prediction_distribution
from autonomio.plots.shapeplot import shapeplot


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
    X_num = X

    if para['randomize'] is True:
        data = data.sample(frac=1)

    X, Y = transform_data(data, para['flatten'], X, Y)

    if para['validation'] is not False:
        X, Y, X_val, Y_val = separate(X, Y, para['validation'])

    try:
        dims = X.shape[1]
    except IndexError:
        dims = X_num

    unique = np.unique(Y)

    if len(unique) == 2:
        para['neuron_last'] = 1
    else:
        para['neuron_last'] = len(unique)

    para['dims'] = dims

    if para['layers'] == 1:
        para['shape'] = 'funnel'

    if para['neuron_max'] == 'auto' and dims >= 4:
        para['neuron_max'] = int(dims + (dims * 0.2))

    elif para['neuron_max'] == 'auto':
        para['neuron_max'] = 4

    if para['neuron_count'] is 'auto':
        para['neuron_count'] = shapes(para)

    if len(para['neuron_count']) is not para['layers']:
        print("NB! Number of neurons should be equal to the number of layers")

    if type(para['metrics']) is not list:
        para['metrics'] = [para['metrics']]

    if para['model'] is 'mlp':
        model, history = mlp(X, Y, para)
    if para['model'] is 'regression':
        model, history = regression(X, Y,
                                    para['epoch'],
                                    para['reg_mode'],
                                    para['metrics'])

    network_scale = len(X)*para['epoch']*para['layers']*para['neuron_max']

    for key, val in history.history.iteritems():
        if 'acc' in key:
            if 'val' in key:
                val_acc = key
            else:
                acc = key

        if 'loss' in key:
            if 'val' in key:
                val_loss = key
            else:
                loss = key

    # train / test results
    ex2 = pd.DataFrame({
                    'train_acc': history.history[acc],
                    'train_loss': history.history[loss],
                    'test_acc': history.history[val_acc],
                    'test_loss': history.history[val_loss]})

    scores = model.evaluate(X, Y, verbose=para['verbose'])

    if para['double_check'] is False or para['validation'] is False:
        if para['hyperscan'] is False:
            print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    # calculate and round predictions
    predictions = model.predict(X)
    rounded = [round(x[0]) for x in predictions]

    if para['double_check'] is True:
            check(Y, rounded, scores)

    if para['save_model'] is False and para['validation'] is not False:
        para['save_model'] = 'saved_model'

    if para['save_model'] is not False:
        save_model_as(X_num,
                      data.columns,
                      model, para['save_model'])

    # shuffling and separating the data
    if para['validation'] is not False:
        validate(X_val, Y_val, para['save_model'])

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

    ex3 = pd.Series({
                    'optimizer': para['optimizer'],
                    'activation': para['activation'],
                    'activation_out': para['activation_out'],
                    'loss': para['loss'],
                    })

    train_stats = [ex2['train_acc'].max(),
                   ex2['train_acc'].min(),
                   ex2[-10:]['train_acc'].median(),
                   ex2[-10:]['train_acc'].mean(),
                   ex2[-para['epoch']:]['train_acc'].values[0],
                   ex2[-1:]['train_acc'].values[0]]

    test_stats = [ex2['test_acc'].max(),
                  ex2['test_acc'].min(),
                  ex2[-10:]['test_acc'].median(),
                  ex2[-10:]['test_acc'].mean(),
                  ex2[-para['epoch']:]['test_acc'].values[0],
                  ex2[-1:]['test_acc'].values[0]]

    # prevent Tensorflow memory leakage
    K.clear_session()

    if para['hyperscan'] is True:
        return ex1, ex2, ex3

    else:
        display(pd.DataFrame(ex1).transpose())

        if para['shape_plot'] is True:
            shapeplot(para['neuron_count'], para['model'])

        trainplot(train_stats, test_stats)
        accuracy(ex2)
        prediction_distribution(predictions, bins=100)
        return
