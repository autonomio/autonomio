import pandas as pd

from autonomio.transform.transform_data import transform_data
from autonomio.plots.plots import prediction_distribution
from autonomio.plots.scatterz import scatterz
from autonomio.load_model import load_model

from IPython.display import display

def make_prediction(data,
                    saved_model,
                    label,
                    interactive,
                    interactive_x):

    loaded_model, X, flatten = load_model(saved_model)
    signals = transform_data(data, flatten, X)
    prediction = loaded_model.predict(signals)

    if label is False:
        prediction = pd.DataFrame(prediction)
        prediction.columns = ['Prediction']

    else:
        prediction = pd.DataFrame(prediction)
        prediction[label] = data[label]
        prediction.columns = ['Prediction', label]

    prediction = prediction.sort_values('Prediction', ascending=False)

    out = pd.Series({

        'a': len(prediction.Prediction),
        'b': prediction.Prediction.median(),
        'c': prediction.Prediction.mean(),
        'd': prediction.Prediction.std(),
        'e': prediction.Prediction.min(),
        'f': prediction.Prediction.max(),
    })

    out = pd.DataFrame(out).transpose()
    out.columns = ['predictions',
                   'median_prediction',
                   'mean_prediction',
                   'std_prediction',
                   'min_prediction',
                   'max_prediction']

    display(out)
    prediction_distribution(prediction.Prediction, bins=100)

    if interactive is True:

        temp = pd.merge(prediction,
                        data,
                        left_on=label,
                        right_on=label)
        return temp

    else:

        return prediction
