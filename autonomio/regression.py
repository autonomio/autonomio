import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l1_l2
from hyperas.distributions import uniform

def regression(epochs, mode='linear'):

    x, y = np.array(df.iloc[:,2:]),np.array(df.Survived)
    
    model = Sequential()
    
    if mode == 'linear':
        model.add(Dense(1, input_dim=x.shape[1]))
        model.compile(optimizer='rmsprop', metrics=['accuracy'], loss='mse')
    
    elif mode == 'logistic':
        model.add(Dense(1, activation='sigmoid', input_dim=x.shape[1]))
        model.compile(optimizer='rmsprop', metrics=['accuracy'], loss='binary_crossentropy')
    
    elif mode == 'regularized':
        reg = l1_l2(l1=0.01, l2=0.01)
        model.add(Dense(1, activation='sigmoid', W_regularizer=reg, input_dim=x.shape[1]))
        model.compile(optimizer='rmsprop', metrics=['accuracy'], loss='binary_crossentropy')

    history = model.fit(x, y, nb_epoch=epochs, verbose=0, validation_split=.33)
    
    out = pd.DataFrame({
                    'train_acc': history.history['acc'],
                    'train_loss': history.history['loss'],
                    'test_acc': history.history['val_acc'],
                    'test_loss': history.history['val_loss']
    })
    
    return model, out