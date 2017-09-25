import numpy as np

from autonomio._utils.load_model import load_model


def validate(X, Y, saved_model):

    '''Validation

    WHAT: function that makes predictions for the separated
    data and compares them with the actual output.
    '''

    model = load_model(saved_model)[0]

    predictions = model.predict(X)
    rounded = np.array([round(x[0]) for x in predictions])

    len_round = len(rounded)

    # transpose Y for comparing
    Y = map(list, zip(*Y))
    l = np.array(Y == rounded)
    l = l.astype(float)

    l_sum = np.sum(l)

    val_acc = l_sum / len_round * 100

    print('validation accuracy: %.2f%%' % (val_acc))


def separate(X, Y, validation):

    '''Separation

    WHAT: separating data for validation.

    OUTPUT: returns X and Y data for training the model and
    validation.
    '''

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
