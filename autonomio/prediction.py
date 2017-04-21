import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json
from vectorize_text import vectorize_text
from plots import distribution

def load_model(saved_model,saved_model_weights):
    
    json_file = open(saved_model, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(saved_model_weights)
    print("Loaded model from disk")
    
    return loaded_model

def make_prediction(X,data,name,saved_model):

    signals = data[X]
    name = data[name]

    part_string = saved_model.replace('.json','')
    saved_model_weights = part_string + '.h5'

    l=[]
    i=0
    loaded_model = _load_model(saved_model,saved_model_weights)
    np.set_printoptions(suppress=True)
    
    try: 
        if signals.shape[1] < 300:
            signals = pd.DataFrame(vectorize_text(signals))
    except:
    
        if type(signals) == list or len(signals.shape) > 1:

            s = signals[0][0]
            e = signals[1][0]

            signals = signals.ix[:,:300][:].values
            predict = loaded_model.predict(signals)

        else:

            signals = pd.DataFrame(vectorize_text(signals))
            predict = loaded_model.predict(signals.values)
                               
    for pred in predict:
                                      
        l.append([pred[0],name[i:i+1].values[0]])
        i+=1
        
    out = pd.DataFrame(l)
    out.columns = ['value','name']
    out = out.sort_values('value',ascending=False)
    
    distribution(out.value)
    print out.head(10)
    print ""
    print out.tail(10)
    
    return out
