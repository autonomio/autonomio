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
