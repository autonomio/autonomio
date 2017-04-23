from autonomio.commands import data, train

# get the data
tweets = data('random_tweets')
tweets = tweets.head(500)

# run train and save model
tr = train('text','neg',tweets)
tr = train(1,'neg',tweets)
tr = train([1,5],'neg',tweets)

# run test
#te = test('text',tweets,'handle','model.json')
