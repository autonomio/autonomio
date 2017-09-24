from keras.callbacks import EarlyStopping
from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import LearningRateScheduler


def callbacks(early_stop):

    '''
    WHAT: function which creates the list of the callbacks for the
          model.
    '''

    l = []

    if early_stop is not False:
        l.append(_earlystop(early_stop))

    return l


def _earlystop(early_stop):

    '''
    WHAT: helping function that creates the EarlyStopping callback.
    '''

    patience = 5
    monitor = 'val_loss'

    if early_stop is not True:
        if early_stop is not list:
            early_stop = [early_stop]

    if early_stop is list:
        for i in range(len(early_stop)):
            if early_stop[i] is str:
                monitor = early_stop[i]
            if early_stop[i] is int:
                patience = early_stop[i]

    early_stopping = EarlyStopping(patience=patience, monitor=monitor)

    return early_stopping
