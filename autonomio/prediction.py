import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json
from vectorize_text import vectorize_text
from x_transform import x_transform

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
    X = map(int, X.split())
    f.close()
    
    return loaded_model, X

def make_prediction(data, saved_model, dims, validation=False):

    loaded_model, X = load_model(saved_model)

    x = x_transform(X, data)
    df_x = pd.DataFrame(x)

    X = df_x.astype('float32')
    X = np.array(X)
    signals = X[:,0:dims]

    if validation != False:
        if validation == True:
            n = len(signals) * .5
        else:
            n = len(signals) * validation
        
        n = int(n)

        signals = signals[n:]

    np.set_printoptions(suppress=True)

    predict = loaded_model.predict(signals)
    
      
    l = []
    i = 0

    for pred in predict:
                                      
        l.append([pred[0]])
        i+=1

    out = pd.DataFrame(l)
    out.columns = ['value']
    out = out.sort_values('value',ascending=False)

    print out.head(10)
    print ""
    print out.tail(10)
    
    
    return predict
