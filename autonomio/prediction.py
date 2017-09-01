import pandas as pd

from transform.transform_data import transform_data
from plots.plots import prediction_distribution
from load_model import load_model

from IPython.display import display

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

    out = pd.Series({

        'a': len(prediction.Value),
        'b': prediction.Value.median(),
        'c': prediction.Value.mean(),
        'd': prediction.Value.std(),
        'e': prediction.Value.min(),
        'f': prediction.Value.max(),
    })

    out = pd.DataFrame(out).transpose()
    out.columns = ['predictions',
                   'median_prediction',
                   'mean_prediction',
                   'std_prediction',
                   'min_prediction',
                   'max_prediction']

    display(out)
    prediction_distribution(prediction.Value, bins=100)

    return prediction
