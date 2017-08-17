import numpy as np
import pandas as pd
from random import shuffle

from transform_data import transform_data
from prediction import make_prediction, load_model


def validate(Y, data, para):

    model, X = load_model(para['save_model'])

    X, Y = transform_data(data, para['flatten'], X, Y)

    shuffle(X)

    X_val, Y_val, X, Y = val_separation(para['validation'], X, Y)
    X_train, Y_train, X_test, Y_test = separation(X, Y, X_val)

    model.compile(loss=para['loss'], 
                  optimizer=para['optimizer'], 
                  metrics=['accuracy'])

    # getting scores and predictions
    train_scores = model.evaluate(X_train, Y_train, verbose=verbose)
    test_scores = model.evaluate(X_test, Y_test, verbose=verbose)

    predictions = make_prediction(data, para['save_model'],	flatten=para['flatten'],
                                  validation=para['validation'])
    rounded = [round(x[0]) for x in predictions]

    df1 = pd.DataFrame(rounded)
    df2 = pd.DataFrame(Y_val)

    printing(df1, df2, X_val, rounded, test_scores, train_scores)

    return X, Y

def val_separation(validation, X, Y):

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

    return X_validate, Y_validate, X, Y

def separation(X, Y, X_val):

    a = len(X)

    # separating data for train 67% and test 33%
    s = int(round(.67 * a))

    X_train = X[:s]
    Y_train = Y[:s]

    X_test = X[s:]
    Y_test = Y[s:]

    return X_train, Y_train, X_test, Y_test

def printing(df1, df2, X_val, rounded, test_scores, train_scores):

    b = len(X_val)

    # 0 or 1 if the prediction mathes with output
    l = np.array(df1 == df2)
    l = l.astype(int)

    x = 0

    for i in range(b):
        if l[i] == 1:
            x += 1.0

    val_acc = x / len(rounded)

    print("\ntrain accuracy: %.2f%%" % (train_scores[1]*100))
    print("loss: %.2f%%" % (train_scores[0]*100))
    print("test accuracy: %.2f%%" % (test_scores[1]*100))
    print("loss: %.2f%%" % (test_scores[0]*100))
    print("validation accuracy: %.2f%%" % (val_acc*100))