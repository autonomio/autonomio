from prediction import make_prediction
from train_new import kuubio
from plots import scatterz
from load_data import load_data
from transform_data import transform_data

import pandas as pd

def train(X,Y,data,
			dims=300,
			epoch=5,
			flatten='mean',
       		dropout=.2,
       		layers=3,
       		model='kuubio',
       		loss='binary_crossentropy',
       		optimizer='adam',
       		activation='relu',
       		activation_out='sigmoid',
       		save_model=False,
       		neuron_first='auto',
       		neuron_last=1,
       		batch_size=10,
       		verbose=0):

    '''
    NOTE:  1) the data has to be in float or something that
              goes nicely in to 'float32'
           
           2) the data has to be in pandas dataframe 
              with no column names (other than int)
    '''

    train = kuubio(X,Y,data,
					dims,
					epoch,
					flatten,
		       		dropout,
		       		layers,
		       		model,
		       		loss,
		       		optimizer,
		       		activation,
		       		activation_out,
		       		save_model,
		       		neuron_first,
		       		neuron_last,
		       		batch_size,
		       		verbose)

    return train

    
def test(X,data,labels,saved_model,y_scatter=False):
    

	if y_scatter == False:

	    test = make_prediction(X,data,labels,saved_model)
	else:

		test = make_prediction(X,data,labels,saved_model)
		data = pd.merge(test,data,left_on='name',right_on='handle')
		plot = scatterz('value',y_scatter,data,'name')

		temp = test,plot
		temp[1]

	return test,temp[1]

def data(name,mode='default'):

	'''
    'election_in_twitter'      
     Dataset consisting of 10 minute samples of 80 million tweets
    
    'sites_category_and_vec'   
     4,000 sites with word vectors and 5 categories
    
    'programmatic_ad_fraud'    
     Data from both buy and sell side and over 10 other sources
    
    'parties_and_employment'   
     9 years of monthly poll and unemployment numbers 
    
    'random_tweets'            
     20,000 tweets main intended for 
    '''	

	out = load_data(name,mode)

	return out
