from keras.callbacks import EarlyStopping
from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import LearningRateScheduler


def callbacks(para):

    '''Callbacks
    WHAT: function which creates the list of the callbacks for the
          model.
    '''

    l = []

    if para['reduce_lr'] is True:
        l.append(ReduceLROnPlateau(patience=para['patience'],
                                   monitor=para['monitor'],
                                   factor=para['factor'],
                                   epsilon=para['epsilon'],
                                   cooldown=para['cooldown'],
                                   min_lr=para['min_lr']))
        if para['early_stop'] is True:
            para['patience'] = para['patience'] * 1.5

    if para['early_stop'] is True:
        l.append(EarlyStopping(patience=para['patience'],
                               monitor=para['monitor'],
                               min_delta=para['min_delta'],
                               mode=para['ESmode']))

    return l
