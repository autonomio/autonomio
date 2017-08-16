from keras.models import model_from_json


def load_model(saved_model):

    json_file = open(saved_model + ".json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(saved_model + '.h5')
    print("Loaded model from disk")

    f = open(saved_model+".x", 'r')
    X = f.read()
    try:
        X = map(int, X.split())
    except ValueError:
        X = X.split()

    f.close()

    if type(X) == list and len(X) == 1:
        X = X[0]

    return loaded_model, X
