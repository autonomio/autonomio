import pandas as pd

from autonomio.transform.transform_data import transform_data
from autonomio.plots.plots import prediction_distribution
from autonomio.load_model import load_model
from autonomio.transform.dataframe import df_merge

from IPython.display import display


def make_prediction(data,
                     saved_model,
                     labels,
                     interactive,
                     interactive_x):

    '''Predictor

    WHAT: Makes predictions on a given dataset based on a saved
    model that have been previously trained with train().

    '''
    # storing label input string for later

    label_str = labels

    # loading model and transforming data
    loaded_model, X, flatten = load_model(saved_model)
    temp_data = transform_data(data, flatten, X)
    prediction = loaded_model.predict(temp_data)
    prediction = pd.DataFrame(prediction)

    # detecting if multi-class predictions
    pred_cols = prediction.shape[1]

    # handling multi-class prediction cases
    col_labels = []
    col_labels.append('Prediction')

    if pred_cols > 1:

        for i in range(pred_cols-1):
            col_labels.append('Prediction_' + str(i+1))

    # adding labels to predictions
    if labels is not False:

        labels = pd.DataFrame(data[labels])
        labels = labels.reset_index()
        labels = labels.drop('index', axis=1)

        col_labels.insert(0, label_str)

        prediction = df_merge(labels, prediction)

    prediction.columns = col_labels

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
                        left_on=label_str,
                        right_on=label_str)
        return temp

    else:

        return prediction
