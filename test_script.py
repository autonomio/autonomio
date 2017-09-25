from autonomio.commands._wrapper import data
from autonomio.commands._wrapper import train
from autonomio.commands._wrapper import predictor
from autonomio.commands._wrapper import wrangler
from autonomio.commands._wrapper import hyperscan
from autonomio.transforms.transform_data import transform_data
from autonomio.transforms.col_name_generator import col_name_generator
from autonomio.transforms.nan_imputer import nan_imputer
from autonomio.transforms.sohot_encoding import all_is_binary
from autonomio.transforms.onehot_encoding import onehot
from autonomio.transforms.rescale import max_rescale
from autonomio._utils.hyperparameters import load_parameters
from autonomio._utils.hyperstats import hyper_descriptive
from autonomio.plots.duaparam import duaparam
from autonomio.plots.paramagg import paramagg
from autonomio.plots.quadparam import quadparam
from autonomio.plots.paramscatter import paramscatter
from autonomio.plots.paramgrid import paramgrid
from autonomio.plots.scatterz import scatterz

import pandas as pd
import numpy as np

# TABLE OF CONTENTS
# 1) data                line 31
# 2) wrangler            line 60
# 3) train               line 76
# 4) predictor           line 106
# 5) shapes              line 114
# 6) hyperscan           line 145
# 7) text_transformers   line 169
# 8) plots               line 187
# 9) helper scripts      line 210

# 1) data
temp = data('tweet_sentiment')
temp = data('election_in_twitter')
temp = data('sites_category_and_vec')
temp = data('bitcoin_price')
temp = data('programmatic_ad_fraud')
temp = data('random_tweets')

temp_employment = data('parties_and_employment')
temp_titanic = data('kaggle_titanic_train')

temp.to_msgpack('test_data.msgpack')
data('test_data.msgpack', 'file')

temp.to_json('test_data.json')
data('test_data.json', 'file')

temp = temp.head(100)

temp2 = np.array(temp)
temp2 = temp2[:, 2:4]
temp2 = pd.DataFrame(temp2)

data('temp.x', 'file')

temp2.to_csv('test_data.csv')
data('test_data.csv', 'file', header=None)
data('test_data.csv')

# 2) wrangler

temp['datetime'] = temp['created_at']

temp1 = wrangler(data=temp,
                 y='neg',
                 vectorize='text')

temp1 = wrangler(data=temp,
                 max_categories='max',
                 to_string='text',
                 fill_columns='url',
                 starts_with_col='location',
                 datetime_mode='sequence')

temp1 = wrangler(data=temp,
                 max_categories=42,
                 vectorize=['text', 'user_tweets'],
                 datetime_mode='drop')

# 3) train
tr = train(1, 'neg', temp, model='regression', flatten='mode')
tr = train([1, 5], 'neg', temp, model='regression',
           reg_mode='logistic', flatten='cat_string',
           early_stop=True, reduce_lr=True)
tr = train([1, 2, 3, 4, 5], 'neg', temp,
           model='regression',
           reg_mode='regularized',
           flatten='cat_numeric',
           learning_rate=0.1)

tr = train(1, 'quality_score', temp, flatten='median')
tr = train(1, 'quality_score', temp, flatten=6, early_stop=['val_acc'])
tr = train(1, 'quality_score', temp, flatten=.5, learning_rate=0.1)
tr = train(1, 'quality_score', temp, flatten='mean', metrics='accuracy')

tr = train('text', 'neg', temp, save_model='test_model')
te = predictor(temp, 'test_model')

tr = train(1, 'neg', temp, layers=1, validation=True)
tr = train(1, 'neg', temp, validation=.6, shape_plot=True)

try:
    train(1, 'neg', temp, neurons=[1])
except:
    pass

train(temp_employment.MUU,
      epoch=1,
      batch_size=512,
      model='lstm',
      normalize_window=False,
      learning_rate=0.1)
train(temp_employment.MUU,
      epoch=1,
      batch_size=512,
      model='lstm',
      normalize_window=True)

tr = train(['reach_score', 'influence_score'],
           'neg',
           temp,
           save_model='strings')

train()
train(model='lstm')

# 4) predicton

te = predictor(temp,
               'strings',
               interactive=True,
               interactive_x='user_followers',
               labels='handle')

# 5) shapes

l = ['funnel',
     'brick',
     'triangle',
     'pyramid',
     'rhombus',
     'long_funnel',
     'diamond',
     'hexagon',
     'stairs']

for i in l:

    if i in (l[0:4]):
        tr = train(1, 'neg', temp, shape=i, double_check=True, layers=15)

    elif i in (l[4:5]):
        tr = train(1, 'neg', temp, shape=i, neuron_max=1, layers=8)
        tr = train(1, 'neg', temp, shape=i, neuron_max=9, layers=4)

    if i in (l[5:7]):
        tr = train(1, 'neg', temp, shape=i, layers=13)
        tr = train(1, 'neg', temp, shape=i, layers=14)

    elif i in (l[7:9]):
        tr = train(1, 'neg', temp, shape=i, layers=4)
        tr = train(1, 'neg', temp, shape=i, layers=10)
        tr = train(1, 'neg', temp, shape=i, layers=11)
        tr = train(1, 'neg', temp, shape=i, layers=12)

# 6) hyperscan

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

# 7) text_transformers

X = transform_data(temp, flatten='none')
X = transform_data(temp, flatten='none', X=1)
Y = transform_data(temp, flatten='none', Y='neg')
X, Y = transform_data(temp, flatten='none', X=1, Y='neg')

b = nan_imputer(temp_titanic.Age)
b = nan_imputer(temp_titanic.Age, impute_mode='mean')
b = nan_imputer(temp_titanic.Age, impute_mode='median')
b = nan_imputer(temp_titanic.Age, impute_mode='common')
b = nan_imputer(temp_titanic.Age, impute_mode='mode')

c = all_is_binary(temp_titanic, 'Survived')

l = temp_titanic.Parch.tolist()
a = onehot(l)

temp3 = col_name_generator(pd.DataFrame([1, 2]))

# 8) plots

scatterz('influence_score', 'neg', temp, labels='handle')
scatterz('influence_score', 'neg', temp,
         labels='handle', yscale='log', xscale='log')

x = train(2, 'Survived', temp_titanic, flatten='none', hyperscan=True)

quadparam(x[1], 'test_acc', 'test_loss', 'train_acc', 'train_loss')
duaparam(x[1], 'test_acc', 80, 70)
paramscatter(x[1], 'train_acc', limit=5)
paramagg(x[1])
paramgrid(x[1], 'train_acc')
paramscatter(x[1], 'train_acc', sort=False)
paramgrid(x[1], 'train_acc')

temp2 = pd.DataFrame(['0', '0', '0'], columns=['0'])

try:
    paramgrid(temp2, '0')
except:
    pass

# 9) helper scripts

max_rescale([0, 1, 2], to_int=True)
max_rescale([0, 1, 2])

a = hyper_descriptive(temp_titanic, 'Age', 'SibSp')
a = hyper_descriptive(temp_titanic, 'Age', 'SibSp', mode='mean')
a = hyper_descriptive(temp_titanic, 'Age', 'SibSp', mode='std')
a = hyper_descriptive(temp_titanic, 'Age', 'SibSp', mode='min')
a = hyper_descriptive(temp_titanic, ['Age', 'Survived'], 'SibSp', mode='max')

load_parameters('categorical_losses')
