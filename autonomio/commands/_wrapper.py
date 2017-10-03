from .prediction import make_prediction
from .train import trainer
from .load_data import load_data
from .wrangler import wrangler_main
from autonomio.models.lstm import lstm


def train(X=None, Y=None, data=None,
          epoch=20,
          flatten='mean',
          validation_split=.33,
          dropout=.2,
          layers=3,
          loss='binary_crossentropy',
          optimizer='adam',
          activation='relu',
          activation_out='sigmoid',
          metrics=['accuracy'],
          save_model=False,
          save_best=False,
          neuron_max='auto',
          batch_size=10,
          verbose=0,
          shape='funnel',
          neurons='auto',
          double_check=False,
          validation=False,
          model='mlp',
          seq_len=50,
          prediction_len='auto',
          dense_neurons=100,
          normalize_window=True,
          reg_mode='linear',
          hyperscan='False',
          w_regularizer='auto',
          w_reg_values=[0, 0],
          learning_rate='auto',
          shape_plot=False,
          randomize=False,
          early_stop=False,
          patience=5,
          monitor='val_loss',
          min_delta=0,
          early_stop_mode='auto',
          reduce_lr=False,
          factor=0.1,
          epsilon=0.0001,
          cooldown=0,
          min_lr=0.001,
          lr_scheduler=False,
          initial_lr='auto',
          drop=0.5,
          drop_each=10):

    '''The command for training a new model.

       NOTE: If you want to see the training / test plots, remember to do:

          %matplotlib inline

    INPUT: the data ingestion is very flexibile. You can
           Input text (also unicode), labels, and things will
           work. No transformation needed outside of Autonomio.

            See more details below.

    PARAMETERS:

    X =     The input can be indicated in several ways:

            'label'   = single column label
            ['a','b'] = multiple column labels
            [1,12]    = a range of columns
            [1,2,12]  = columns by index

            The data can be multiple dtypes:

            'int'     = any integer values
            'float'   = any float value
            'string'  = raw text or category labels*

            * use commands.utils wrangler() to convert in to
            process your data first!

    Y =     This can be in multiple dtype:

            'int'     = any integer values
            'float'   = any float value
            'string'  = category labels

            See more related to prediction variable below
            in 'flatten section'.

    data =  A pandas dataframe where you have at least one
            column for 'x' depedent variable (predictor) and
            one column for 'y' indepedent variable (prediction).

    dims =  this is selected automatically and is not needed.
            NOTE: this needs to be same as x features

    epoch = how many epocs will be run for training. More epochs
            will take more time.

    flatten = For transforming y (outcome) variable. For example if
              the y input is continuous but prediction is binary, then
              a flattening of some sort should be used.

              OPTIONS:  'mean','median','mode', int, float, 'cat_string',
                        'cat_numeric', and 'none'

    dropout = The fraction of learning that will be "forgotten" on each each
              learning event.

    layers = The number of dense layers the model will have. Note that each
             dense layer is followed by a dropout layer.

    model = This is currently not in use. Later we add LSTM and some other
            model options, then it will be activated.

    loss = The loss to be used with the model. All the Keras losses all
           available https://keras.io/losses/

    optimizer = The optimizer to use with the model. All the Keras optimizers
                are all available > https://keras.io/optimizers/

    activation = Activation for the hidden layers (non-output) and all the
                 Keras optimizers are all available >
                 https://keras.io/optimizers/

    activation_out = Same as 'activation' (above), but for the
                     output layer only.

    metrics = list or string with metrics values. Can be used for mlp and
              regression models. All the Keras metrics are available >
              https://keras.io/metrics/

    save_model =  An option to save the model configuration, weights
                  and parameters from last epoch.

                  OPTIONS:  default is 'False', if 'True' model
                            will be saved with default name ('model')
                            and if string, then the model name
                            will be the string value e.g. 'titanic'.

    save_best = When True saves the best model. Works only when 'save_model'
                is activated.

    neuron_max = The maximum number of neurons on any layer.

    neuron_last = How many neurons there are in the last layer.

    batch_size = Changes the number of samples that are propagated
                 through the network at one given point in time.
                 The smaller the batch_size, the longer the training
                 will take.

    verbose = This is set to '0' by default. The other options are
              '1' and '2' and will change the amount of information
              you are getting.


    shape = Used for automatically creating a network shape. Currently
            there are 8 options available.

            'funnel'
            'rhombus'
            'long_funnel'
            'brick'
            'hexagon'
            'diamon'
            'triangle'
            'stairs'

    neurons = list of neurons. By default it is automatically set according to
              a chosen shape. Number of neurons must be the same as number of
              layers.

    double_check = Makes a 'manual' check of the results provided by
                   Keras backend and compares the two. This is good
                   when you have doubt with the results.

    validation = Validates in a more robust way than usual train/test split
                 by initially splitting the dataset in half, where the first
                 half becomes train and test, and then the second half becomes
                 validation data set.

                 OPTIONS: default is 'false', with 'true' 50% of data is
                          separated for validation.

    model = Switch for choosing which kind of model is being used. The options
            are 'mlp' for multi layer perceptor and 'regression' for
            regression.

    hyperscan = Enables a mode where an hyperscan function can be run for
                hyperparameter optimization purpose.

    w_regularizer = Adds a weight regularizer to a model. 'Auto' mode adds
                    regularizer to the last layer. Options are the string with
                    number of layers starting from 0.

    w_reg_value = String with two values for l1 and l2.

    learning_rate = float, which changes the learning rate for an optimizer.

    early_stop = When True turns on the callback EarlyStopping, which stops
                 the training after some number of epochs(patience).

    patience = By default equals to 5. When we use early_stop and reduce_lr at
               the same time, patience is 1.5 times bigger for EarlyStopping.

    monitor = can be 'val_acc' or 'val_loss'(which is set by default), depends
              on which value we want to watch. Used for early_stop and
              reduce_lr.

    min_delta = only change of more than min_delta will count as improvement.
                Used for EarlyStopping callback.

    early_stop_mode = can be 'auto', 'min' and 'max'. 'min' mode will stop
                      the training when monitored value will stop decreasing,
                      max - when increasing. Used for EarlyStopping callback.

    reduce_lr = When True model uses callback ReduceLROnPlateau, which will
                reduce lr when there will be no improvement for some number
                of epochs(patience).

    factor = number by which learning rate will be decreased. By default 0.1.
             new_lr = lr * factor. Used for ReduceLROnPlateau callback.

    epsilon = Treshhold. For concentrating on sufficient changes.
              By default 0.0001. Used for ReduceLROnPlateau callback.

    cooldown = number of epochs to wait before resuming the operation.
               By default 0. Used for ReduceLROnPlateau callback.

    min_lr = minimum value of learning rate that callback can reduce to.

    lr_scheduler = When True, activates LearningRateScheduler callback,
                   which drops learning rate each specified number
                   of epochs.

    initial_lr = the learning rate we start with before droppint.
                 When 'auto' makes learning rate 5 times bigger than
                 the optimizer's default value.

    drop = the factor by which we reduce learning late. 0.5 by default.

    drop_each = number of epoch after which we drop learning rate.
    '''

    parameters = {'epoch': epoch,
                  'batch_size': batch_size,
                  'activation': activation,
                  'validation_split': validation_split,
                  'loss': loss,
                  'optimizer': optimizer,
                  'dropout': dropout,
                  'layers': layers,
                  'activation_out': activation_out,
                  'verbose': verbose,
                  'flatten': flatten,
                  'save_model': save_model,
                  'shape': shape,
                  'neuron_count': neurons,
                  'double_check': double_check,
                  'validation': validation,
                  'neuron_max': neuron_max,
                  'model': model,
                  'reg_mode': reg_mode,
                  'hyperscan': hyperscan,
                  'w_regularizer': w_regularizer,
                  'w_reg_values': w_reg_values,
                  'prediction_len': prediction_len,
                  'seq_len': seq_len,
                  'dense_neurons': dense_neurons,
                  'normalize_window': normalize_window,
                  'shape_plot': shape_plot,
                  'randomize': randomize,
                  'metrics': metrics,
                  'lr': learning_rate,
                  'early_stop': early_stop,
                  'patience': patience,
                  'monitor': monitor,
                  'min_delta': min_delta,
                  'ESmode': early_stop_mode,
                  'reduce_lr': reduce_lr,
                  'factor': factor,
                  'epsilon': epsilon,
                  'cooldown': cooldown,
                  'min_lr': min_lr,
                  'lr_scheduler': lr_scheduler,
                  'initial_lr': initial_lr,
                  'drop': drop,
                  'drop_each': drop_each,
                  'save_best': save_best
                  }

    if model is 'lstm':
        if X is None:
            print('Please input data to use lstm model')
            return
        lstm(X, parameters)
        return

    else:
        if X is None:
            if Y is None:
                if data is None:
                    print('X, Y or data is missing')
                    return

    out = trainer(X, Y, data, parameters)

    return out


def predictor(data,
              saved_model,
              labels=False,
              interactive=False,
              interactive_x='none'):

    ''' Function for making predictions on a saved model.

    NOTE:  1) remember to use the same 'x' as with training

           2) call the model by its name
    '''

    pred = make_prediction(data,
                           saved_model,
                           labels=labels,
                           interactive=interactive,
                           interactive_x=interactive_x)

    return pred


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
              losses='auto',
              optimizers='auto',
              activations='auto',
              shapes='auto',
              early_stop=False,
              patience=5,
              monitor='val_loss',
              min_delta=0,
              early_stop_mode='auto'):

    from hyperscan import hyperscan

    df = hyperscan(x, y, data, epochs, flatten, dropout, batch_sizes,
                   batch_sizes_step, layers, layers_step, activation_out,
                   neuron_max, losses, optimizers,
                   activations, shapes, early_stop, patience, monitor,
                   min_delta, early_stop_mode)

    return df


def wrangler(data,
             y=None,
             max_categories=None,
             datetime_mode='retain',
             to_string=None,
             vectorize=None,
             fill_columns=None,
             fill_with=None,
             impute_columns=None,
             impute_mode='mean_by_std',
             nan_treshold=.9,
             starts_with_col=None,
             col_that_contains=None,
             col_contains_strings=None):

    out = wrangler_main(data,
                        y,
                        max_categories,
                        datetime_mode,
                        to_string,
                        vectorize,
                        fill_columns,
                        fill_with,
                        impute_columns,
                        impute_mode,
                        nan_treshold,
                        starts_with_col,
                        col_that_contains,
                        col_contains_strings)

    return out


def data(name,
         mode='default',
         sep=',',
         delimiter=None,
         header='infer',
         error_bad_lines=False,
         nrows=None):

    '''Function for loading one of the Autonomio dataset.

    OPTIONS: Either set mode to 'file' or use name without mode parameter.

    FILENAMES:

    'election_in_twitter'
     Dataset consisting of 10 minute samples of 80 million tweets.

     'tweet_sentiment'
     Dataset with tweet text classified for sentiment using NLTK Vader.

    'sites_category_and_vec'
     4,000 sites with word vectors and 5 categories.

    'programmatic_ad_fraud'
     Data from both buy and sell side and over 10 other sources.

    'parties_and_employment'
     9 years of monthly poll and unemployment numbers.

    'random_tweets'
     20,000 tweets main intended for.

    '''

    out = load_data(name, mode, sep, delimiter, header, error_bad_lines, nrows)

    return out
