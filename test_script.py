from autonomio.commands import data, train, test
import pandas as pd

# datasets
temp = data('tweet_sentiment')
temp = data('election_in_twitter')
temp = data('sites_category_and_vec')
temp = data('parties_and_employment')
temp = data('programmatic_ad_fraud')

# create dataset for rest of the tests
temp = data('random_tweets')
temp = temp.head(100)

# x variable input modes
tr = train(1,'neg',temp,dims=1)
tr = train([1,5],'neg',temp,dims=4)
tr = train(['reach_score','influence_score'],'neg',temp,dims=2)
tr = train([1,2,3,4,5],'neg',temp,dims=5)

# y variable flattening mode
tr = train(1,'quality_score',temp,dims=1,flatten='median')
tr = train(1,'quality_score',temp,dims=1,flatten=6)
tr = train(1,'quality_score',temp,dims=1,flatten=.5)
tr = train(1,'quality_score',temp,dims=1,flatten='mean')

# model saving and loading
tr = train('text','neg',temp,save_model='test_model')
te = test(temp,'test_model', labels='handle')

l = [	'funnel', 
        'brick',
        'triangle',
        'rhombus', 
        'long_funnel',  
        'diamond', 
        'hexagon',  
        'stairs']

for i in l:

    if i in (l[0:3]): #funnel, brick, triangle
        tr = train(1, 'neg', temp, dims=1, double_check=True)

    elif i in (l[3:4]): #only rhombus
        tr = train(1, 'neg', temp, dims=1, shape=i, neuron_max=1, layers=8)
        tr = train(1, 'neg', temp, dims=1, shape=i, neuron_max=9, layers=4)
        
	if i in (l[5:6]): #long_funnel, diamond
		tr = train(1, 'neg', temp, dims=1, shape=i, layers=6, validation=True)
		tr = train(1, 'neg', temp, dims=1, shape=i, layers=5, validation=.6)
        
    elif i in (l[6:8]): #hexagon, stairs
    	tr = train(1, 'neg', temp, dims=1, shape=i, layers=4)
    	tr = train(1, 'neg', temp, dims=1, shape=i, layers=6)
    	tr = train(1, 'neg', temp, dims=1, shape=i, layers=7)
    	tr = train(1, 'neg', temp, dims=1, shape=i, layers=8) 