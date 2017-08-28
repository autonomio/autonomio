from prediction import make_prediction
from train_new import trainer
from load_data import load_data
from wrangler import labels_to_ints
from plots import scatterz


def train(X, Y, data,
          epoch=5,
          flatten='mean',
          validation_split=.33,
          dropout=.2,
          layers=3,
          loss='binary_crossentropy',
          optimizer='adam',
          activation='relu',
          activation_out='sigmoid',
          save_model=False,
          neuron_max='auto',
          neuron_last=1,
          batch_size=10,
          verbose=0,
          shape='funnel',
          double_check=False,
          validation=False,
          model='mlp',
          reg_mode='linear',
          hyperscan='False',
          w_regularizer='auto',
          w_reg_values=[0,0]):

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

    save_model =  An option to save the model configuration, weights
                  and parameters.

                  OPTIONS:  default is 'False', if 'True' model
                            will be saved with default name ('model')
                            and if string, then the model name
                            will be the string value e.g. 'titanic'.

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
            are 'mlp' for multi layer perceptor and 'regression' for regression.

    hyperscan = Enables a mode where an hyperscan function can be run for
                hyperparameter optimization purpose.

    w_regularizer = Adds a weight regularizer to a model. 'Auto' mode adds 
                    regularizer to the last layer. Options are the string with
                    number of layers starting from 0.

    w_reg_value = String with two values for l1 and l2.
    '''

    parameters = {'epoch': epoch,
                  'batch_size': batch_size,
                  'activation': activation,
                  'validation_split': validation_split,
                  'loss': loss,
                  'optimizer': optimizer,
                  'dropout': dropout,
                  'layers': layers,
                  'neuron_last': neuron_last,
                  'activation_out': activation_out,
                  'verbose': verbose,
                  'flatten': flatten,
                  'save_model': save_model,
                  'shape': shape,
                  'double_check': double_check,
                  'validation': validation,
                  'neuron_max': neuron_max,
                  'model': model,
                  'reg_mode': reg_mode,
                  'hyperscan': hyperscan,
                  'w_regularizer': w_regularizer,
                  'w_reg_values': w_reg_values
                  }

    out = trainer(X, Y, data, parameters)

    return out


def predictor(data,
              saved_model,
              labels=False,
              x_plot=False,
              y_plot=False):

    ''' Function for making predictions on a saved model.

    NOTE:  1) remember to use the same 'x' as with training

           2) call the model by its name
    '''

    pred = make_prediction(data, saved_model, label=labels)

    if x_plot is not False and y_plot is not False and labels is not False:
        scatterz(x_plot, y_plot, data, labels)

    if x_plot is not False or y_plot is not False:
        print("Please, define both x and y for plots for rendering")

    return pred


def wrangler(df,
             y='none',
             max_categories='auto',
             starts_with_col='none',
             treshold=.9,
             first_fill_cols=None,
             fill_with=0,
             to_string=None,
             vectorize=None):

    out = labels_to_ints(df, y, max_categories, starts_with_col,
                         treshold, first_fill_cols, fill_with, to_string, vectorize)

    return out


def data(name, mode='default', sep=',', delimiter=None, header='infer'):

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

    out = load_data(name, mode, sep, delimiter, header)

    return out
