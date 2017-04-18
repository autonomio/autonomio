import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json
from vectorize_text import *

def _load_model():
    
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    
    return loaded_model
    
def _distribution_plot(data):

    sns.set_style("white")
    plt.figure(figsize=(14, 4))
    plt.xlim(-0.005,1.0)
    sns.kdeplot(data,legend=False)
    sns.despine(right=False)

def make_prediction(signals,name):
    
    l=[]
    i=0
    loaded_model = _load_model()
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
                                      
        l.append([pred[0],name[i]])
        i+=1
        
    out = pd.DataFrame(l)
    out.columns = ['value','name']
    out = out.sort_values('value',ascending=False)
    
    _distribution_plot(out.value)
    print out.head(10)
    print ""
    print out.tail(10)
    
    return out
