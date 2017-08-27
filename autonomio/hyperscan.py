import datetime as dt
import pandas as pd

from hyperparameters import load_parameters
from commands import train


def hyperscan(x,
              y,
              data,
              epochs=10,
              flatten='none',
              dropout=0,
              batch_sizes=15,
              batch_sizes_step=1,
              layers=5,
              layers_step=1,
              activation_out='sigmoid',
              neuron_max='auto',
              scan_mode='auto',
              losses='auto',
              optimizers='auto',
              activations='auto',
              shapes='auto',
              check=False):

    '''
    mode = 'auto' will scan through all
           'selective' will scan through selected

           When you have selective mode on, then just
           set the parameters you don't want to scan
           and leave the rest to 'auto'. Those that are
           on 'auto' will be scanned.

           Input can be either string for a single parameter,
           or a list for multiple parameters.
    '''

    df = pd.DataFrame()

    if scan_mode is not 'selective':

        shapes = load_parameters('shapes')
        optimizers = load_parameters('optimizers')
        activations = load_parameters('activations')
        losses = load_parameters('binary_losses')

    else:
        if losses is 'auto':
            losses = load_parameters('binary_losses')
        elif type(losses) is str:
            losses = [losses]

        if activations is 'auto':
            activations = load_parameters('activations')
        elif type(activations) is str:
            activations = [activations]

        if optimizers is 'auto':
            optimizers = load_parameters('optimizers')
        elif type(optimizers) is str:
            optimizers = [optimizers]

        if shapes is 'auto':
            shapes = load_parameters('shapes')
        elif type(shapes) is str:
            shapes = [shapes]

        if layers is 'auto':
            layers = range([2, 15], layers_step)
        elif type(layers) is int:
            layers = [layers]
        elif type(layers) is list:
            layers = range(layers[0], layers[1], layers_step)

        if batch_sizes is 'auto':
            batch_sizes = range([2, 15], batch_sizes_step)
        elif type(batch_sizes) is int:
            batch_sizes = [batch_sizes]
        elif type(batch_sizes) is list:
            batch_sizes = range(batch_sizes[0], batch_sizes[1], batch_sizes_step)

    if check == True:
      return

    a = len(losses)
    b = len(shapes)
    c = len(activations)
    d = len(optimizers)
    e = len(batch_sizes)
    f = len(layers)

    no_of_tries = a * b * c * d * e * f

    start_time = dt.datetime.now()
    print("Total tries in this scan: %d" % no_of_tries)
    print("Scan started on: %s" % start_time.strftime('%H:%M'))

    counter = 0
    for loss in losses:
        for activation in activations:
            for optimizer in optimizers:
                for shape in shapes:
                    for layer in layers:
                        for batch_size in batch_sizes:

                            counter += 1
                            temp = train(x,
                                         y,
                                         data,
                                         epoch=epochs,
                                         flatten=flatten,
                                         dropout=dropout,
                                         layers=layer,
                                         batch_size=batch_size,
                                         activation_out=activation_out,
                                         neuron_max=neuron_max,
                                         hyperscan=True,
                                         loss=loss,
                                         activation=activation,
                                         optimizer=optimizer,
                                         shape=shape)

                            out = _data_prep(temp)

                            df = df.append(out)

                            if counter == 1:

                                try_time = dt.datetime.now()
                                temp = (try_time - start_time) * no_of_tries
                                finish_estimate = temp + start_time
                                finish_estimate = finish_estimate.strftime('%H:%M')
                                print("Estimated finish: %s" % finish_estimate)

    return df


def _data_prep(x):

    '''
    Prepares the data for appending to dataframe round by round.

    '''

    temp = x[0]

    temp['train_acc'] = x[1][-10:]['train_acc'].median()
    temp['train_acc_std'] = x[1][-10:]['train_acc'].std()
    temp['train_loss'] = x[1][-10:]['train_loss'].median()
    temp['train_loss_std'] = x[1][-10:]['train_loss'].std()
    temp['test_acc'] = x[1][-10:]['test_acc'].median()
    temp['test_acc_std'] = x[1][-10:]['test_acc'].std()
    temp['test_loss'] = x[1][-10:]['test_loss'].median()
    temp['test_loss_std'] = x[1][-10:]['test_loss'].std()
    temp['activation'] = x[2]['activation']
    temp['activation_out'] = x[2]['activation_out']
    temp['loss'] = x[2]['loss']
    temp['optimizer'] = x[2]['optimizer']
    temp = pd.DataFrame(temp).transpose()
    temp = temp.drop(['ind_var', 'y_transform'], axis=1)

    return temp
