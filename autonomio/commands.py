from prediction import *
from train_new import *

def train(X,Y,data,dims=300,epoch=5,flatten='mean',
       dropout=.2,layers=3,
       model='train',loss='binary_crossentropy',
       save_model=False,
       neuron_first='auto',neuron_last=1,
       batch_size=10,verbose=0):

    train = kuubio(X,Y,data)
    
def test(X,Y,data):
    
    make_prediction(data[X],data[Y])
