from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
from keras.layers import SimpleRNN
from keras.layers import Dropout
from keras.layers import Embedding
from keras.layers import GlobalAveragePooling1D
from keras.layers import LSTM


def embeds(x,
           y,
           mode='LSTM',
           pooling=False,
           epochs=10,
           activation='tanh',
           dropout=0,
           recurrent_dropout=0,
           batch_size=15,
           input_dim=None,
           output_dim=100,
           cnn_kernel_size=1,
           hidden_layer=False,
           hidden_dim=32,
           input_length='auto',
           lstm_mode=0):


    '''Embeds Model for Text

    WHAT: An alternative for word2vec based text transformation. Note that
    the data needs to be transformed to the right format first.

    :param mode: Offers modes: 'fasttext', 'CNN', 'SimpleRNN' and 'LSTM'
    :param pooling: Allows turning GlobalAveragePooling on
    :param epochs: Number of epochs
    :param activation: Activation to be used in the model
    :param dropout: Dropout rate as floating point value
    :param recurrent_dropout: For SimpleRNN and LSTM as floating point value
    :param batch_size: Accepts an integer value
    :param input_dim: This is dealth with automatically based on data shape by
    default.
    :param output_dim: An integer value for number output neurons from the
    input layer.
    :param hidden_dim: Number of units / neurons on the layer following the
    Embedding layer
    :param input_length: Automatically handled based on data shape.
    :param lstm_mode: 0, 1 or 2 modes that effect the LSTM model configuration.

    '''

    input_length = x.shape[1]

    if input_dim is None:
        input_dim = x.max()+1

    if input_length is 'auto':
        input_length = x.shape[1]

    model = Sequential()
    model.add(Embedding(input_dim=input_dim,
                        output_dim=output_dim,
                        input_length=input_length))

    elif mode is 'LSTM':
        model.add(LSTM(hidden_dim))

    elif mode is 'SimpleRNN':
        model.add(SimpleRNN(hidden_dim))

    elif mode is 'fasttext':
        pooling = True

    if pooling is True:
        model.add(GlobalAveragePooling1D())

    model.add(Dropout(dropout))
    model.add(Activation(activation))

    if hidden_layer is True:
        model.add(Dense(hidden_dim))
        model.add(Dropout(dropout))
        model.add(Activation(activation))

    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
    model.summary()
    history = model.fit(x, y,
                        epochs=epochs,
                        batch_size=batch_size,
                        validation_split=.33)

    return history
