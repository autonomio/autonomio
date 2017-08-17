import pandas as pd

from transform_data import transform_data
from load_model import load_model


def make_prediction(data,
                    saved_model,
                    flatten='mean',
                    name=False,
                    validation=False):

    loaded_model, X = load_model(saved_model)

    signals = transform_data(data, flatten, X)

    if validation is False:

        predict = loaded_model.predict(signals)

        if name is not False:
            name = data[name]

            l = []
            i = 0

            for x in predict:
                l.append([x[0], name[i:i+1].values[0]])
                i += 1

            predict = pd.DataFrame(l)
            predict.columns = ['Value', 'Name']

        else:
            predict = pd.DataFrame(predict)
            predict.columns = ['Value']
            
        predict = predict.sort_values('Value', ascending=False)

        print(predict.head(10))
        print('--------------')
        print(predict.tail(10))

        return predict

    if validation is not False:

        if validation is True:
            n = len(signals) * .5
        else:
            n = len(signals) * validation

        n = int(n)

        signals = signals[n:]

        predictions = loaded_model.predict(signals)

        return predictions
