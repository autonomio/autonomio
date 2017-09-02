from autonomio.commands import data, train, predictor, wrangler, hyperscan
from autonomio.transform.transform_data import transform_data
from autonomio.transform.col_name_generator import col_name_generator
from autonomio.transform.nan_imputer import nan_imputer
from autonomio.plots.scatterz import scatterz
from autonomio.hyperparameters import load_parameters
from autonomio.hyperstats import hyper_descriptive
from autonomio.transform.onehot_encoding import onehot
from autonomio.transform.sohot_encoding import all_is_binary
from autonomio.transform.rescale import max_rescale
from autonomio.plots.duaparam import duaparam
from autonomio.plots.paramagg import paramagg
from autonomio.plots.quadparam import quadparam
from autonomio.plots.paramscatter import paramscatter
from autonomio.plots.paramgrid import paramgrid

import pandas as pd
import numpy as np

# datasets
temp = data('tweet_sentiment')
temp = data('election_in_twitter')
temp = data('sites_category_and_vec')
temp = data('bitcoin_price')
temp = data('programmatic_ad_fraud')
temp = col_name_generator(pd.DataFrame([1, 2]))

# create dataset for rest of the tests
temp = data('random_tweets')
temp = temp.head(100)

temp.to_msgpack('test_data.msgpack')
data('test_data.msgpack', 'file')

temp.to_json('test_data.json')
data('test_data.json', 'file')

temp2 = np.array(temp)
temp2 = temp2[:, 2:4]
temp2 = pd.DataFrame(temp2)

data('temp.x', 'file')

temp2.to_csv('test_data.csv')
data('test_data.csv', 'file', header=None)
data('test_data.csv')

temp1 = wrangler(df=temp, y='neg', vectorize='text')
temp1 = wrangler(df=temp, max_categories='max', to_string='text',
                 first_fill_cols='url', starts_with_col='location')
temp1 = wrangler(df=temp, max_categories=42,
                 vectorize=['text', 'user_tweets'])

X = transform_data(temp, flatten='none')
X = transform_data(temp, flatten='none', X=1)
Y = transform_data(temp, flatten='none', Y='neg')
X, Y = transform_data(temp, flatten='none', X=1, Y='neg')

# x variable input modes
tr = train(1, 'neg', temp, model='regression', flatten='mode')
tr = train([1, 5], 'neg', temp, model='regression',
           reg_mode='logistic', flatten='cat_string')
tr = train([1, 2, 3, 4, 5], 'neg', temp,
           model='regression',
           reg_mode='regularized',
           flatten='cat_numeric',
           shape_plot=True)

# y variable flattening mode
tr = train(1, 'quality_score', temp, flatten='median')
tr = train(1, 'quality_score', temp, flatten=6)
tr = train(1, 'quality_score', temp, flatten=.5)
tr = train(1, 'quality_score', temp, flatten='mean', shape_plot=True)

# model saving and loading
tr = train('text', 'neg', temp, save_model='test_model')
te = predictor(temp, 'test_model')

# for validation
tr = train(1, 'neg', temp, layers=1, validation=True)
tr = train(1, 'neg', temp, validation=.6)

tr = train(['reach_score', 'influence_score'],
           'neg',
           temp,
           save_model='strings')

te = predictor(temp,
               'strings',
               interactive=True,
               interactive_x='user_followers',
               labels='handle')

train()
train(model='lstm')

l = ['funnel',
     'brick',
     'triangle',
     'rhombus',
     'long_funnel',
     'diamond',
     'hexagon',
     'stairs',
     'pyramid']

for i in l:

    if i in (l[0:3]):  # funnel, brick, triangle
        tr = train(1, 'neg', temp, shape=i, double_check=True)

    elif i in (l[3:4]):  # only rhombus
        tr = train(1, 'neg', temp, shape=i, neuron_max=1, layers=8)
        tr = train(1, 'neg', temp, shape=i, neuron_max=9, layers=4)

    if i in (l[4:6]):  # long_funnel, diamond
        tr = train(1, 'neg', temp, shape=i, layers=6)
        tr = train(1, 'neg', temp, shape=i, layers=5)

    elif i in (l[6:8]):  # hexagon, stairs
        tr = train(1, 'neg', temp, shape=i, layers=4)
        tr = train(1, 'neg', temp, shape=i, layers=6)
        tr = train(1, 'neg', temp, shape=i, layers=7)
        tr = train(1, 'neg', temp, shape=i, layers=8)

scatterz('influence_score', 'neg', temp, labels='handle')
scatterz('influence_score', 'neg', temp,
         labels='handle', yscale='log', xscale='log')

hyperscan('user_followers', 'neg', temp.head(10), epochs=3,
          batch_sizes=[5, 6],
          losses='logcosh',
          optimizers='adam',
          activations='elu')

hyperscan('user_followers', 'neg', temp.head(10), epochs=3,
          layers=[5, 6],
          losses='logcosh',
          optimizers='adam',
          shapes='funnel')

hyperscan('user_followers', 'neg', temp.head(10), epochs=3,
          losses='logcosh',
          activations='elu',
          shapes='funnel')

hyperscan('user_followers', 'neg', temp.head(10), epochs=3,
          optimizers='adam',
          activations='elu',
          shapes='funnel')

load_parameters('categorical_losses')

# check for a good result
temp = data('kaggle_titanic_train')

a = hyper_descriptive(temp, 'Age', 'SibSp')
a = hyper_descriptive(temp, 'Age', 'SibSp', mode='mean')
a = hyper_descriptive(temp, 'Age', 'SibSp', mode='std')
a = hyper_descriptive(temp, 'Age', 'SibSp', mode='min')
a = hyper_descriptive(temp, ['Age', 'Survived'], 'SibSp', mode='max')

b = nan_imputer(temp.Age)
b = nan_imputer(temp.Age, mode='mean')
b = nan_imputer(temp.Age, mode='median')
b = nan_imputer(temp.Age, mode='common')
b = nan_imputer(temp.Age, mode='mode')

c = all_is_binary(temp, 'Survived')

l = temp.Parch.tolist()
a = onehot(l)

df = wrangler(temp, y='Survived',
              first_fill_cols='Cabin',
              starts_with_col='Cabin',
              treshold=.8)

x = train([2, 3, 4, 5, 6, 7, 8, 9], 'Survived', df,
          flatten='none',
          epoch=150,
          dropout=0,
          batch_size=12,
          loss='logcosh',
          activation='elu',
          layers=6,
          shape='brick',
          hyperscan=True)

quadparam(x[1], 'test_acc', 'test_loss', 'train_acc', 'train_loss')
duaparam(x[1], 'test_acc', 80, 70)
paramscatter(x[1], 'train_acc', limit=5)
paramagg(x[1])
paramgrid(x[1], 'train_acc')

x2 = train([2, 3, 4, 5, 6, 7, 8, 9], 'Survived', df,
           flatten='none',
           epoch=3,
           dropout=0,
           batch_size=12,
           loss='logcosh',
           activation='elu',
           layers=6,
           shape='brick',
           hyperscan=True)

paramscatter(x2[1], 'train_acc', sort=False)
paramgrid(x2[1], 'train_acc')

temp2 = pd.DataFrame(['0', '0', '0'], columns=['0'])

try:
    paramgrid(temp2, '0')
except:
    pass

p = x[1][-10:]['train_acc'].mean()
if p < .8:
    print('bad result for titanic data')
    1/0

temp = data('parties_and_employment')
# test for lstm model
train(temp.MUU, epoch=1, batch_size=512, model='lstm', normalize_window=False)
train(temp.MUU,
      epoch=1,
      batch_size=512,
      model='lstm',
      normalize_window=True,
      shape_plot=True)

max_rescale([0, 1, 2], to_int=True)
max_rescale([0, 1, 2])
