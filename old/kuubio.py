from keras_diagram import ascii
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import model_from_json
from load_data import *
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('bmh')
%matplotlib inline
import warnings
warnings.filterwarnings("ignore")

import spacy as sp
import ascify as asc

def vectorize_text(data):
    
    '''
    OUTPUT:       a list of lists with the word vectors in lists
    
    USE EXAMPLE:  vectors = vectorize_text(list_with_strings)

    '''
    
    nlp = sp.load('en')
    
    c = len(data)
    
    l = []

    for i in range(c):

        asc_string = asc.Ascify(str(data[i])).ascify()
        uni_string = unicode(asc_string)
        vec_obj = nlp(uni_string)
        vector = vec_obj.vector
        l.append(vector)
        
    return l

def _transform_data(x_text,y_var,data):
    
    x = vectorize_text(data[x_text])
    
    y = [data[y_var]]
    
    try:
        
        if len(y) == 1:

            y = map(list, zip(*y))

        if len(y) == len(x):

            x1 = x   # we do this to retain the original y and x
            y1 = y

            df_x = pd.DataFrame(x1)
            df_y = pd.DataFrame(y1)

            df_y = pd.DataFrame(df_y[0] >= df_y[0].mean()).astype(int)
            #df_y = pd.DataFrame(df_y[0] >= 0.2).astype(int)  # convert to 1/0
    except:
        
        print "ERROR: something went"
        
    return df_x,df_y


def _load_model(filename):

    json_file = open(filename, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("model.h5")
    
    print("Loaded model from disk")
    return loaded_model
    

def kuubio(X,Y,data,dims=8,epoch=5,model='model',save_model=False):
    
    X,Y = _transform_data(X,Y,tweets)
    
    '''
    NOTE:  1) the data has to be in float or something that
              goes nicely in to 'float32'
           
           2) the data has to be in pandas dataframe 
              with no column names (other than int)
    '''
    
    if model != 'model':
        model = _load_model(model)
        
    np.random.seed(7)
    
    X = X.astype('float32')
    Y = Y.astype('float32')
    
    X = np.array(X)
    Y = np.array(Y)
    
    X = X[:,0:dims]
    #Y = Y[:,8]

    model = Sequential()
    model.add(Dense(dims+4, input_dim=dims, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', 
                  optimizer='adam', 
                  metrics=['accuracy'])
    history = model.fit(X, Y, epochs=epoch, batch_size=10)
    scores = model.evaluate(X, Y)
    
    #print(history.history.keys())
    print ""
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    print ""
    print(ascii(model))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=False)
    
    ax1.plot(history.history['acc'])
    ax2.plot(history.history['loss'])
    
    ax1.set_title('model accuracy')
    ax1.set_xlabel('epoch')
    ax1.set_ylabel('accuracy')
    
    ax2.set_title('model loss')
    ax2.set_xlabel('epoch')
    ax2.set_ylabel('loss')

    fig.set_size_inches(12,3)
    
    if save_model == True:
    
        model_json = model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        model.save_weights("model.h5")
        print("Saved model to disk")
        
    fig.show()
