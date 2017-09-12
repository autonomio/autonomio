import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l1_l2
from keras.optimizers import RMSprop


def regression(X, Y, param):

    '''Regression Models

    WHAT: linear, logistic, and regularized regression models
    for the train() function.

    '''

    x, y = np.array(X), np.array(Y)

    if param['lr'] is not 'auto':
        optim = RMSprop(lr=param['lr'])
    else:
        optim = 'rmsprop'

    reg = l1_l2(l1=param['w_reg_values'][0], l2=param['w_reg_values'][1])

    model = Sequential()

    if param['reg_mode'] == 'linear':
        model.add(Dense(1, input_dim=x.shape[1]))
        model.compile(optimizer=optim, metrics=param['metrics'], loss='mse')

    elif param['reg_mode'] == 'logistic':
        model.add(Dense(1, activation='sigmoid', input_dim=x.shape[1]))
        model.compile(optimizer=optim,
                      metrics=param['metrics'],
                      loss='binary_crossentropy')

    elif param['reg_mode'] == 'regularized':
        reg = l1_l2(l1=0.01, l2=0.01)
        model.add(Dense(1,
                        activation='sigmoid',
                        W_regularizer=reg,
                        input_dim=x.shape[1]))

        model.compile(optimizer=optim,
                      metrics=param['metrics'],
                      loss='binary_crossentropy')

    out = model.fit(x, y,
                    nb_epoch=param['epoch'],
                    verbose=0,
                    validation_split=param['validation_split'])

    return model, out
