import time

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.regularizers import l1_l2


def mlp(X, Y, para):

    '''Multi Layer Perceptor Model

    WHAT: A multi-layer perceptor neural network to be called through
    the train() command.

    See more info through train() docstring.

    '''

    if para['w_regularizer'] is 'auto':
        para['w_regularizer'] = [para['layers']]

    l1, l2 = check_w_reg(0, para['w_regularizer'], para['w_reg_values'])

    model = Sequential()
    model.add(Dense(para['neuron_count'][0],
                    input_dim=para['dims'],
                    activation=para['activation'],
                    W_regularizer=l1_l2(l1=l1, l2=l2)))
    model.add(Dropout(para['dropout']))

    j = 1

    for i in range(para['layers'] - 1):

        l1, l2 = check_w_reg(j, para['w_regularizer'], para['w_reg_values'])

        model.add(Dense(para['neuron_count'][i+1],
                        activation=para['activation'],
                        W_regularizer=l1_l2(l1=l1, l2=l2)))
        model.add(Dropout(para['dropout']))

        j += 1

    l1, l2 = check_w_reg(para['layers'],
                         para['w_regularizer'],
                         para['w_reg_values'])

    model.add(Dense(para['neuron_last'],
                    activation=para['activation_out'],
                    W_regularizer=l1_l2(l1=l1, l2=l2)))
    model.compile(loss=para['loss'],
                  optimizer=para['optimizer'],
                  metrics=['accuracy'])

    if para['verbose'] >= 1:
        time.sleep(0.1)

    out = model.fit(X, Y, validation_split=para['validation_split'],
                    epochs=para['epoch'],
                    verbose=para['verbose'],
                    batch_size=para['batch_size'])

    return model, out


def check_w_reg(x, w_reg, values):

    '''Weight Regulizer Parameter Reader

    WHAT: Reads the user input and makes it available for the
    lstm() function.

    '''

    if x in w_reg:
        l1 = values[0]
        l2 = values[1]
    else:
        l1 = 0
        l2 = 0

    return l1, l2
