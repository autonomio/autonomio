import pandas as pd
import numpy as np

from IPython.display import display

from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential

from lstm_transform_data import _lstm_load_data
from lstm_plots import histplot, lstm_plot

def lstm(data,
         epochs=1,
         seq_len=50,
         prediction_len='auto',
         normalize_window=True,
         batch_size=512,
         dense_neurons=100,
         verbose=1):

    if prediction_len is 'auto':
        prediction_len = seq_len

    X_train, y_train, X_test, y_test = _lstm_load_data(data, seq_len, normalize_window)

    dimensions = [1, seq_len, dense_neurons, 1]

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

    model.compile(loss="mse", optimizer="rmsprop")

    model.fit(
        X_train,
        y_train,
        batch_size=batch_size,
        nb_epoch=epochs,
        validation_split=0.05,
        verbose=verbose)

    predicted = model.predict(X_test)
    predicted = np.reshape(predicted, (predicted.size,))

    temp = pd.DataFrame({'predicted': predicted, 'actual': y_test})

    out = pd.Series({'pred_std': temp.predicted.std(),
                     'actual_std': temp.actual.std(),
                     'diff_std': round(temp.actual.std() / temp.predicted.std(), 3) -1,
                     'pred_max': temp.predicted.max(),
                     'actual_max': temp.actual.max(),
                     'diff_max': round(temp.actual.max() / temp.predicted.max(), 3) -1,
                     'pred_min': temp.predicted.min(),
                     'actual_min': temp.actual.min(),
                     'diff_min': round(temp.actual.min() / temp.predicted.min(), 3) -1})

    #print("Median prediction error: %.2f%%" % ((temp.predicted / temp.actual * 100).median() - 100))

    display(pd.DataFrame(out).transpose())

    lstm_plot(predicted, y_test)
    histplot(predicted, y_test, 50)
