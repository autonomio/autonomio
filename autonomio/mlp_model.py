import time

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout


def mlp(X, Y, para):

    model = Sequential()
    model.add(Dense(para['neuron_count'][0],
                    input_dim=para['dims'],
                    activation=para['activation']))
    model.add(Dropout(para['dropout']))

    for i in range(para['layers'] - 1):
        model.add(Dense(para['neuron_count'][i+1], activation=para['activation']))
        model.add(Dropout(para['dropout']))

    model.add(Dense(para['neuron_last'], activation=para['activation_out']))
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
