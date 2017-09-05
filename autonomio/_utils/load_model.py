def load_model(saved_model):

    '''Load Model

    WHAT: Loads a saved model and makes it available for
    prediction use by predictor().

    '''
    from keras.models import model_from_json

    json_file = open(saved_model + ".json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(saved_model + '.h5')

    f = open(saved_model + ".x", 'r')
    temp = f.read()
    try:
        X = map(int, temp.split()[:-1])
    except ValueError:
        X = temp.split()[:-1]

    try:
        flatten = float(temp.split()[-1])

    except ValueError:
        flatten = temp.split()[-1]

    f.close()

    if type(X) == list and len(X) == 1:
        X = X[0]

    return loaded_model, X, flatten
