from keras.callbacks import EarlyStopping
from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import LearningRateScheduler

from autonomio._utils.get_method import get_method

import math


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

    if para['lr_scheduler'] is True:

        if para['initial_lr'] is 'auto':
            optim = get_method(para['optimizer'], 'optimizers')
            para['initial_lr'] = optim.__init__.__defaults__[0] * 5

        def step_decay(epoch):
            temp = math.floor(epoch / para['drop_each'])
            lr = para['initial_lr'] * math.pow(para['drop'], temp)
            return lr

        l.append(LearningRateScheduler(step_decay))

    return l
