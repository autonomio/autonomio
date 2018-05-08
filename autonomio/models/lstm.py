import pandas as pd
import numpy as np

from IPython.display import display

from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.optimizers import RMSprop

from autonomio.transforms.lstm_transform_data import _lstm_load_data
from autonomio.plots.lstm_plots import histplot, lstm_plot


def lstm(data, param):

    '''LSTM Model

    WHAT: An LSTM model function to be used through train().

    HOW: lstm(x)

    INPUT: 1-dimensional data in array, list or Series

    OUTOUT: Trained model and plots for reviewing the accuracy.

    '''

    if param['prediction_len'] is 'auto':
        param['prediction_len'] = param['seq_len']

    if param['lr'] is not 'auto':
        optimizer = RMSprop(lr=param['lr'])
    else:
        optimizer = 'rmsprop'

    print(param['seq_len'])

    X_train, y_train, X_test, y_test = _lstm_load_data(
                                                    data,
                                                    param['seq_len'],
                                                    param['normalize_window']
                                                    )

    dimensions = [1, param['seq_len'], param['dense_neurons'], 1]

    model = Sequential()

    model.add(LSTM(
        input_shape=(dimensions[1], dimensions[0]),
        output_dim=dimensions[1],
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        dimensions[2],
        return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(
        output_dim=dimensions[3]))
    model.add(Activation("linear"))

    model.compile(loss="mse", optimizer=optimizer)

    history = model.fit(X_train,
                        y_train,
                        batch_size=param['batch_size'],
                        nb_epoch=param['epoch'],
                        validation_split=0.05,
                        verbose=param['verbose'])

    predicted = model.predict(X_test)
    predicted = np.reshape(predicted, (predicted.size,))

    temp = pd.DataFrame({'predicted': predicted, 'actual': y_test})

    out = pd.Series({
         'pred_std': temp.predicted.std(),
         'actual_std': temp.actual.std(),
         'diff_std': round(temp.actual.std() / temp.predicted.std(), 3) - 1,
         'pred_max': temp.predicted.max(),
         'actual_max': temp.actual.max(),
         'diff_max': round(temp.actual.max() / temp.predicted.max(), 3) - 1,
         'pred_min': temp.predicted.min(),
         'actual_min': temp.actual.min(),
         'diff_min': round(temp.actual.min() / temp.predicted.min(), 3) - 1})

    display(pd.DataFrame(out).transpose())

    lstm_plot(predicted, y_test)
    histplot(predicted, y_test, 50)
