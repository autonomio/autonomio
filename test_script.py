from autonomio.commands import data, train, test

# get the data
tweets = data('random_tweets')
tweets = tweets.head(500)
tr = train('text','neg',tweets,save_model='multi.json')
tr = train(1,'neg',tweets,dims=1)
tr = train([1,5],'neg',tweets,dims=4)

# run train and save model
te = test('text',tweets,'handle','model.json')
