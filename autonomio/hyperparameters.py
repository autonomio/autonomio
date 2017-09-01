def load_parameters(parameters):

    '''Load hyperparameters

    WHAT: a helper function for storing and accessing
    all available hyperparameters.

    '''

    # losses
    if parameters is 'losses':
        losses = ['msle',
                  'mape',
                  'mae',
                  'poisson',
                  'hinge',
                  'squared_hinge',
                  'cosine',
                  'mse',
                  'logcosh',
                  'binary_crossentropy']
        return losses

    if parameters is 'categorical_losses':
        categorical_losses = ['categorical_hinge',
                              'categorical_crossentropy',
                              'sparce_categorical_crossentropy']
        return categorical_losses

    # activations
    if parameters is 'activations':
        activations = ['softmax',
                       'elu',
                       'selu',
                       'softplus',
                       'softsign',
                       'relu',
                       'tanh',
                       'sigmoid',
                       'hard_sigmoid',
                       'linear']
        return activations

    # optimizers
    if parameters is 'optimizers':
        optimizers = ['SGD',
                      'RMSprop',
                      'Adagrad',
                      'Adadelta',
                      'Adamax',
                      'Adam',
                      'Nadam']
        return optimizers

    # shapes
    if parameters is 'shapes':
        shapes = ['funnel',
                  'long_funnel',
                  'rhombus',
                  'diamond',
                  'brick',
                  'hexagon',
                  'triangle',
                  'stairs']

        return shapes
