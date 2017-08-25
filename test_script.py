from autonomio.commands import data, train, predictor, wrangler
from autonomio.transform_data import transform_data
from autonomio.load_data import load_data
from autonomio.col_name_generator import col_name_generator
from autonomio.plots import scatterz

import pandas as pd
import numpy as np

# datasets
temp = data('tweet_sentiment')
temp = data('election_in_twitter')
temp = data('sites_category_and_vec')
temp = data('parties_and_employment')
temp = data('programmatic_ad_fraud')
temp = data('kaggle_titanic_train')
temp = col_name_generator(temp)

# create dataset for rest of the tests
temp = data('random_tweets')
temp = temp.head(100)

temp.to_msgpack('test_data.msgpack')
data('test_data.msgpack','file')

temp.to_json('test_data.json')
data('test_data.json','file')

temp2 = np.array(temp)
temp2 = temp2[:,2:4]
temp2 = pd.DataFrame(temp2)

temp2.to_csv('test_data.csv')
data('test_data.csv','file')

temp1 = wrangler(df=temp,y='neg', vectorize='text')
temp1 = wrangler(df=temp,max_categories='max',to_string='text',first_fill_cols='url',starts_with_col='location')
temp1 = wrangler(df=temp,max_categories=42, vectorize=['text', 'user_tweets'])

X = transform_data(temp, flatten='none')
X = transform_data(temp, flatten='none', X=1)
Y = transform_data(temp, flatten='none', Y='neg')
X, Y = transform_data(temp, flatten='none', X=1, Y='neg')

# x variable input modes
tr = train(1,'neg',temp,model='regression',flatten='mode')
tr = train([1,5],'neg',temp,model='regression',reg_mode='logistic',flatten='cat_string')
tr = train([1,2,3,4,5],'neg',temp,model='regression',reg_mode='regularized',flatten='cat_numeric')

# y variable flattening mode
tr = train(1,'quality_score',temp,flatten='median')
tr = train(1,'quality_score',temp,flatten=6)
tr = train(1,'quality_score',temp,flatten=.5)
tr = train(1,'quality_score',temp,flatten='mean')

# model saving and loading
tr = train('text','neg',temp,save_model='test_model')
te = predictor(temp,'test_model')

#for validation
tr = train(1, 'neg', temp, layers=1, validation=True)
tr = train(1, 'neg', temp, validation=.6)

tr = train(['reach_score','influence_score'],'neg',temp,save_model='strings')
te = predictor(temp,'strings',x_plot='influence_score',y_plot='user_followers',labels='handle')

l = ['funnel',
     'brick',
     'triangle',
     'rhombus',
     'long_funnel',
     'diamond',
     'hexagon',
     'stairs']

for i in l:

    if i in (l[0:3]): #funnel, brick, triangle
        tr = train(1, 'neg', temp, shape=i, double_check=True)

    elif i in (l[3:4]): #only rhombus
        tr = train(1, 'neg', temp, shape=i, neuron_max=1, layers=8)
        tr = train(1, 'neg', temp, shape=i, neuron_max=9, layers=4)
        
    if i in (l[4:6]): #long_funnel, diamond
        tr = train(1, 'neg', temp, shape=i, layers=6)
        tr = train(1, 'neg', temp, shape=i, layers=5)
        
    elif i in (l[6:8]): #hexagon, stairs
        tr = train(1, 'neg', temp, shape=i, layers=4)
        tr = train(1, 'neg', temp, shape=i, layers=6)
        tr = train(1, 'neg', temp, shape=i, layers=7)
        tr = train(1, 'neg', temp, shape=i, layers=8) 

scatterz('influence_score', 'neg', temp, labels='handle')
scatterz('influence_score', 'neg', temp,labels='handle',yscale='log',xscale='log')