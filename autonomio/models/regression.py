import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l1_l2


def regression(X, Y, epochs, reg_mode):

    '''Regression Models

    WHAT: linear, logistic, and regularized regression models
    for the train() function.

    '''

    x, y = np.array(X), np.array(Y)

    model = Sequential()

    if reg_mode == 'linear':
        model.add(Dense(1, input_dim=x.shape[1]))
        model.compile(optimizer='rmsprop', metrics=['accuracy'], loss='mse')

    elif reg_mode == 'logistic':
        model.add(Dense(1, activation='sigmoid', input_dim=x.shape[1]))
        model.compile(optimizer='rmsprop',
                      metrics=['accuracy'],
                      loss='binary_crossentropy')

    elif reg_mode == 'regularized':
        reg = l1_l2(l1=0.01, l2=0.01)
        model.add(Dense(1,
                        activation='sigmoid',
                        W_regularizer=reg,
                        input_dim=x.shape[1]))

        model.compile(optimizer='rmsprop',
                      metrics=['accuracy'],
                      loss='binary_crossentropy')

    out = model.fit(x, y, nb_epoch=epochs, verbose=0, validation_split=.33)

    return model, out
