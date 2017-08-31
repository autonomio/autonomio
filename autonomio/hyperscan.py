import datetime as dt
import pandas as pd

from hyperparameters import load_parameters
from commands import train


def hyperscan(x,
              y,
              data,
              epochs,
              flatten,
              dropout,
              batch_sizes,
              batch_sizes_step,
              layers,
              layers_step,
              activation_out,
              neuron_max,
              scan_mode,
              losses,
              optimizers,
              activations,
              shapes):

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

    temp_list = []

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
            layers = range(2, 15, layers_step)
        elif type(layers) is int:
            layers = [layers]
        elif type(layers) is list:
            layers = range(layers[0], layers[1], layers_step)

        if batch_sizes is 'auto':
            batch_sizes = range(2, 15, batch_sizes_step)
        elif type(batch_sizes) is int:
            batch_sizes = [batch_sizes]
        elif type(batch_sizes) is list:
            batch_sizes = range(batch_sizes[0], batch_sizes[1], batch_sizes_step)

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

    column_list = ['train_acc', 'train_acc_mean', 'train_acc_min',
                   'train_acc_max', 'train_acc_std', 'train_loss',
                   'train_loss_mean', 'train_loss_min', 'train_loss_max',
                   'train_loss_std', 'test_acc', 'test_acc_mean',
                   'test_acc_min', 'test_acc_max', 'test_acc_std', 'test_loss',
                   'test_loss_mean', 'test_loss_min', 'test_loss_max',
                   'test_loss_std', 'shape', 'activation', 'activation_out',
                   'loss', 'optimizer', 'epochs', 'layers', 'features',
                   'dropout', 'batch_size', 'max_neurons', 'network_scale']

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

                            temp_list.append(out)

                            if counter == 1:

                                try_time = dt.datetime.now()
                                temp = (try_time - start_time) * no_of_tries
                                finish_est = temp + start_time
                                finish_est = finish_est.strftime('%H:%M')
                                print("Estimated finish: %s" % finish_est)

                            # creating a backup to a file every 50 tries
                            if counter % 50 == 0:
                                backup_to_csv = _to_df(temp_list, column_list)
                                backup_to_csv.to_csv('hyperscan.csv')

                                print('tries left: %d' % no_of_tries - counter)


    df = _to_df(temp_list, column_list)

    return df


def _to_df(data, cols):

    '''Dataframe maker

    Takes the input of the scan and puts it in to
    a dataframe. This is to avoid having to use
    the same code twice.

    '''

    df = pd.DataFrame(data)
    df.columns = cols

    return df


def _data_prep(data):

    '''
    Prepares the data for appending to dataframe round by round.

    '''

    a = data[1][-10:]['train_acc'].median()
    b = data[1][-10:]['train_acc'].mean()
    c = data[1]['train_acc'].min()
    d = data[1]['train_acc'].max()
    e = data[1][-10:]['train_acc'].std()

    f = data[1][-10:]['train_loss'].median()
    g = data[1][-10:]['train_loss'].mean()
    h = data[1]['train_loss'].min()
    i = data[1]['train_loss'].max()
    j = data[1][-10:]['train_loss'].std()

    k = data[1][-10:]['test_acc'].median()
    l = data[1][-10:]['test_acc'].mean()
    m = data[1]['test_acc'].min()
    n = data[1]['test_acc'].max()
    o = data[1][-10:]['test_acc'].std()

    p = data[1][-10:]['test_loss'].median()
    q = data[1][-10:]['test_loss'].mean()
    r = data[1]['test_loss'].min()
    s = data[1]['test_loss'].max()
    t = data[1][-10:]['test_loss'].std()

    u = data[0]['shape']
    v = data[2]['activation']
    w = data[2]['activation_out']
    x = data[2]['loss']
    y = data[2]['optimizer']
    z = data[0]['epochs']
    aa = data[0]['layers']
    ab = data[0]['features']
    ac = data[0]['dropout']
    ad = data[0]['batch_size']
    ae = data[0]['max_neurons']
    af = data[0]['network_scale']

    out = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af]

    return out
