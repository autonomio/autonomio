import pandas as pd

from transform_data import transform_data
from load_model import load_model
from plots import scatterz


def make_prediction(data,
                    saved_model,
                    label=False):

    loaded_model, X, flatten = load_model(saved_model)

    signals = transform_data(data, flatten, X)

    prediction = loaded_model.predict(signals)

    if label is not False:
        label = data[label]

        l = []
        i = 0

        for x in prediction:
            l.append([x[0], label[i:i+1].values[0]])
            i += 1

        prediction = pd.DataFrame(l)
        prediction.columns = ['Value', 'Name']

    else:
        prediction = pd.DataFrame(prediction)
        prediction.columns = ['Value']
        
    prediction = prediction.sort_values('Value', ascending=False)

    print(prediction.head(10))
    print('--------------')
    print(prediction.tail(10))
        
    return prediction