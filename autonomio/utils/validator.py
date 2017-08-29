import numpy as np
import pandas as pd
from random import shuffle

from transform_data import transform_data
from prediction import make_prediction, load_model


def validate(X, Y, saved_model):

    model = load_model(saved_model)[0]

    predictions = model.predict(X)
    rounded = np.array([round(x[0]) for x in predictions])

    len_round = len(rounded)

    #transpose Y for comparing
    Y = map(list, zip(*Y))
    l = np.array(Y == rounded)
    l = l.astype(float)

    l_sum = np.sum(l)

    val_acc = l_sum / len_round * 100

    print('validation accuracy: %.2f%%' % (val_acc))

def separate(X, Y, validation):

    if validation is not True:
        n = len(X) * validation
        n = int(n)

    if validation is True:
        n = len(X) * .5
        n = int(n)

    X_validate = X[n:]
    Y_validate = Y[n:]
    X = X[:n]
    Y = Y[:n]

    return X, Y, X_validate, Y_validate